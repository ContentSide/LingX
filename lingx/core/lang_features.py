import numpy as np
from treelib import Tree, Node

def get_linguistic_features(doc):
    links=[]
    links_compact=[] 
    sent_counter=0
    acc=0

    for sent in doc.sentences:
        sent_counter+=acc
        acc=len(sent.words)
        for word in sent.words:
            if word.head > 0:
                links.append([[sent_counter+word.head-1, sent.words[word.head-1].text, sent.words[word.head-1].upos], [sent_counter+word.id-1, word.text, word.upos]])
                links_compact.append([sent_counter+word.head-1, sent_counter+word.id-1])
                    
            else:
                links.append([[sent_counter+word.id-1, word.text, word.upos], [sent_counter+word.id-1, word.text, word.upos]])
                links_compact.append([sent_counter+word.id-1, sent_counter+word.id-1])

    return links, links_compact


def aggregate_tokens(tokens_complexity, aggregation_type="sum"):

    list_tokens_complexity=[token[1] for token in tokens_complexity]

    if len(list_tokens_complexity)>0:

        if aggregation_type=="sum":
            return np.sum(list_tokens_complexity)
        elif aggregation_type=="min":
            return np.min(list_tokens_complexity)
        elif aggregation_type=="max":
            return np.max(list_tokens_complexity)
        elif aggregation_type=="mean":
            return np.average(list_tokens_complexity)
        else:
            raise Exception("Set `aggregation_type` to one of the values `sum`, `mean`, `min` or `max`.")

    else:
        return 0

def is_aux_a_main_verb(word):
    if word.upos=="AUX" and  word.deprel=="aux":
        return False
    elif word.upos=="AUX" and  word.deprel!="aux":
        return True
    else:
        return False

def is_a_main_verb(word):
    if word.upos=="VERB":
        return True
    else:
        return False

def is_a_noun(word):
    if word.upos=="NOUN" or word.upos=="PROPN":
        return True
    else:
        return False


def convert_dep2tree(list_pairs):
    tree = Tree()
    tree.create_node("root", 0)
    pairs = list_pairs.copy()

    while (len(pairs)):
        for item in tree.leaves():
            planned_to_be_deleted=[]
            for pair in pairs:
                if item.identifier == pair[0]:
                    tree.create_node(pair[3], pair[1], parent=pair[0])
                    planned_to_be_deleted.append(pair)
            
            for pair in planned_to_be_deleted:
                pairs.remove(pair)
    return(tree)