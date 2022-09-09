import sys
import pandas as pd
import math
import random
from treelib import Node, Tree

global df_wiki

def make_tree(root_name, depth, print_tree):
    global tree
    global node_names

    tree = Tree()
    node_names = []
    root_node = node(root_name, depth, None)

    #print(node_names)

    if print_tree:
        tree.show()

def get_children(target_page_name, depth, parent_node):
    temp_list = []

    if depth > 0:
        page_categories = categories(target_page_name)

        for cat in page_categories:
            temp_list.append(node(cat, depth - 1, parent_node))

    return temp_list

def categories(target):
    temp_list = []

    df_row = df_wiki.loc[df_wiki[0] == target]

    if df_row.empty:
        return temp_list

    for i in range(1, len(df_row.columns)):
        value = df_row.iloc[0, i]

        if isnan(value):
            return temp_list

        if value not in node_names:
            node_names.append(value)
            temp_list.append(value)

    return temp_list

def isnan(value):
    try:
        return math.isnan(float(value))
    except:
        return False

def get_epithet():
    bad_epithets = ["Avlidna", "avlidna", "Födda", "födda", "Män", "Kvinnor", "Levande"]

    for name in node_names:
        is_good_epithet = True

        for category in bad_epithets:
            if category in name:
                is_good_epithet = False
                break

        if is_good_epithet:
            return name

    if node_names is None:
        return node_names[0]
    else:
        return None

class node:
    def __init__(self, name, depth, parent_node):
        self.id = id(self)
        self.name = name
        self.parent = parent_node

        if parent_node:
            tree.create_node(name, self.id, parent=parent_node.id)
        else:
            tree.create_node(name, self.id)

        self.children = get_children(name, depth, self)

print("Reading database...")
df_wiki = pd.read_csv('/home/sebson/Documents/Exjobb/Wiki/wikipedia.csv', dtype=str, header = None)
print("Database read.\n")
print("Creating epithets...")

if len(sys.argv) > 2:
    depth = int(sys.argv[1])
    search_term = ""

    for i in range(2, len(sys.argv)):
        search_term += sys.argv[i] + "_"

    root_name = search_term[:-1]

    if not any(c.isupper() for c in search_term):
        root_name = root_name.capitalize()

    make_tree(root_name, depth, True)
    print(get_epithet())
else:
    df_phrases = pd.read_csv('obscure_phrases_suc3.csv', header = None)
    depth = 1
    save_iters = 40

    for index, row in df_phrases.iterrows():
        if row[1] == " ":
            root_name = row[0].replace(" ", "_")

            if not any(c.isupper() for c in root_name):
                root_name = row[0].capitalize()

            print(root_name)
            make_tree(root_name, depth, False)

            if len(node_names) > 0:
                df_phrases.at[index, 1] = get_epithet()
            else:
                df_phrases.at[index, 1] = "NaN"

            if (index+1) % save_iters == 0:
                df_phrases.to_csv('obscure_phrases_suc3_with_epithets.csv', index=False, header = None)
                #print("CSV saved.")

    df_phrases.to_csv('obscure_phrases_suc3_with_epithets.csv', index=False, header = None)
    #print("CSV saved.")
