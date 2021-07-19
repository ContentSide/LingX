import numpy as np

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
            return None

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