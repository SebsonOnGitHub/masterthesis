import xml.dom.minidom as minidom
import pandas as pd

# Settings
file_path = "/home/sebson/Documents/Exjobb/Sparv/export/xml_pretty/"    # File path
file_name = file_path + "suc3_0_export.xml"                             # File path and name
allowed_tags = ["ADJ", "NOUN", "PROPN"]                                 # Allowed upos tags
partial_tokens = ["TME"]                                                # Which entities should include its tokens seperatly?
compare_SALDO = True                                                    # Only allow tokens where Stanza and SALDO baseform are the same
min_length_char = 6                                                     # Minimum number of characters in a word
min_length_syll = 2                                                     # Minimum number of syllables

def get_syll(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']
    num_syll = 0
    last_letter_vowel = False

    for letter in word:
        if letter in vowels:
            if not last_letter_vowel:
                num_syll += 1
            last_letter_vowel = True
        else:
            last_letter_vowel = False

    return num_syll

def allowed_cand(token):
    curr_tag = token.attributes['upos'].value
    curr_word = token.attributes['stanza.baseform'].value

    if curr_tag not in allowed_tags:
        return False
    if compare_SALDO and token.attributes['stanza.baseform'].value != token.attributes['saldo.baseform'].value.replace('|',''):
        return False

    if len(curr_word) < min_length_char:
        return False
    if get_syll(curr_word) < min_length_syll:
        return False

    return True

def get_decendents(root_node):
    decendents = []

    for child in root_node.childNodes:
        if child.nodeType == minidom.Node.ELEMENT_NODE:
            if child.tagName == 'segment.token':
                decendents.append(child)
            else:
                decendents.extend(get_decendents(child))

    return decendents


def epi_cand_first_pass(tokens):
    epi_cands = []
    obscure_count = 0

    for token in tokens:
        try:
            curr_word = token.attributes['stanza.baseform'].value
        except KeyError:
            continue

        if token.parentNode.parentNode.tagName == 'swener.ne':
            parent_ne = token.parentNode.parentNode
            temp_ne = ""

            for decendent in get_decendents(parent_ne):
                temp_ne += decendent.firstChild.nodeValue + " "

            temp_ne = temp_ne.rstrip()

            if len(temp_ne) > 2 and '\"' not in temp_ne and '\'' not in temp_ne:
                obscure_count += 1
                if temp_ne not in epi_cands:
                    epi_cands.append(temp_ne)

            if token.parentNode.parentNode.attributes['type'].value in partial_tokens:
                continue

        if allowed_cand(token):
            obscure_count += 1
            if curr_word not in epi_cands:
                epi_cands.append(curr_word)

    #print("Minimum word length:            " + str(min_length_char))
    #print("Minimum number of syllables:    " + str(min_length_syll))
    #print("Number of tokens:               " + str(len(tokens)))
    #print("Number of obscure phrases:      " + str(obscure_count))
    #print("Percentage of obscure phrases:  " + str(round(obscure_count/len(tokens), 2)*100) + "%\n")

    return sorted(epi_cands, key=str.casefold)


#file = minidom.parse(file_path + "suc3_0_export.xml")
#tokens = file.getElementsByTagName('segment.token')
#while min_length_syll <= 5:
#    while min_length_char <= 14:
#        epi_cands = epi_cand_first_pass(tokens)
#        min_length_char += 1
#    min_length_char = 0
#    min_length_syll += 1

file = minidom.parse(file_name)
tokens = file.getElementsByTagName('segment.token')
epi_cands = epi_cand_first_pass(tokens)
#print(epi_cands)
df = pd.DataFrame(epi_cands)
df[1] = " "
df.to_csv('obscure_phrases_suc3_0.csv', index=False, header = None)
