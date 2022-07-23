import xml.dom.minidom as minidom
import pandas as pd

# Settings
file_path = "/home/sebson/Documents/Exjobb/Sparv/sparv_old_data/export/xml_pretty/"    # File path
file_name = file_path + "text4_export.xml"                             # File path and name
allowed_tags = ["ADJ", "NOUN", "PROPN"]                                 # Allowed upos tags
partial_tokens = ["TME"]                                                # Which entities should include its tokens seperatly?
compare_SALDO = True                                                    # Only allow tokens where Stanza and SALDO baseform are the same
min_length_char = 10                                                    # Minimum number of characters in a word
min_length_syll = 4                                                     # Minimum number of syllables

# Globals
tokens_in = 0

def print_percent(tokens_out):
    #print("Total number of tokens before: {}".format(tokens_in))
    #print("Total number of tokens after:  {}".format(tokens_out))
    print("Amount of tokens removed:      {}%".format(100 - int(tokens_out*100/tokens_in)))

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
    global tokens_in
    curr_tag = token.attributes['upos'].value
    curr_word = token.attributes['stanza.baseform'].value

    if curr_tag not in allowed_tags:
        return False
    if compare_SALDO and token.attributes['stanza.baseform'].value != token.attributes['saldo.baseform'].value.replace('|',''):
        return False

    tokens_in += 1

    if len(curr_word) < min_length_char:
        return False
    if get_syll(curr_word) < min_length_syll:
        return False

    return True

def epi_cand_first_pass(file_name):
    global tokens_in
    file = minidom.parse(file_name)
    tokens = file.getElementsByTagName('token') #Needs to be segment.token
    epi_cands = []

    for token in tokens:
        curr_word = token.attributes['stanza.baseform'].value

        if token.parentNode.tagName == 'ne':
            temp_ne = ""

            for child in token.parentNode.childNodes:
                if child.nodeType == minidom.Node.ELEMENT_NODE:
                    temp_ne += child.attributes['stanza.baseform'].value + " "

            temp_ne = temp_ne.rstrip()

            if temp_ne not in epi_cands:
                epi_cands.append(temp_ne)
                tokens_in += 1

            if token.parentNode.attributes['type'].value in partial_tokens:
                continue

        if curr_word not in epi_cands and allowed_cand(token):
            epi_cands.append(curr_word)

    return sorted(epi_cands, key=str.casefold)

epi_cands = epi_cand_first_pass(file_name)
#print_percent(len(epi_cands))
print(epi_cands)
df = pd.DataFrame(epi_cands)
df[1] = " "
df.to_csv('obscure_phrases.csv', index=False, header = None)
