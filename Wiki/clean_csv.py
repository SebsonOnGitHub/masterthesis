#!/usr/bin/env python

import pandas as pd
import math

def isnan(value):
    try:
        return math.isnan(float(value))
    except:
        return False

def good_leaf(key, name):
    bad_categories = ["Wiki", "wiki", "Artiklar", "artiklar", "Robotskapade", "robotskapade", "Enwp", "Ej_uppdaterad", "Förgreningssidor",
                    "Förgreningssidor", "Mallar_som", "Navigationsrutor_med", "Cswp", "Dewp", "Att_göra", "Dolda_kategorier", "Ugglan",
                    "Navigationsrutor", "navigationsrutor" , "kategori", "Kategori", "stubb", "Mall", "mall", "Sidor", "sidor",
                    "Utskrift", "utskrift"]
    max_sentence_length = 4

    if key == name:
        return False

    if name.isupper():
        return False

    if len(name.split('_')) > max_sentence_length:
        return False

    for category in bad_categories:
        if category in name:
            return False

    return True

df_page = pd.read_csv('combined_sorted.csv', dtype=str, header = None)
dict = {}

for i in range(len(df_page)):
    for column in range(1, 30):
        key = df_page.iloc[i, 0]
        value = df_page.iloc[i, column]

        if isnan(value):
            break

        if good_leaf(key, value):
            if key not in dict.keys():
                dict[key] = [key, value]
            elif len(dict[key]) < 40:
                dict[key] += [value]

df_new = pd.DataFrame.from_dict(dict, orient='index')

df_new.to_csv('page_to_category_sorted.csv', index=False, header = None)
