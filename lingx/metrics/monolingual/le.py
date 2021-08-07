# A module for calculating Left Embeddedness in a sentence

import numpy as np

from lingx.core.lang_features import is_aux_a_main_verb, is_a_main_verb
from lingx.core.lang_model import get_doc


def get_le_from_verb(verb_indicator, aggregator="sum"):
    
    drop_last_score = True
    false_place_holders = "".join(str(e) for e in verb_indicator).replace("False","X").split("True")

    if false_place_holders[-1] == '':
        false_place_holders.pop()
        drop_last_score = False
    if false_place_holders[0] == '':
        false_place_holders.pop(0)

    non_verb_counts = [len(item) for item in false_place_holders]

    if drop_last_score :
        non_verb_counts = non_verb_counts[:-1]

    if len(non_verb_counts) > 0:
        if aggregator == "sum":
            left_embeddedness_score=np.sum(non_verb_counts)
        elif aggregator == "mean":
            left_embeddedness_score=np.mean(non_verb_counts)
        elif aggregator == "max":
            left_embeddedness_score=np.max(non_verb_counts)
    else:
        left_embeddedness_score = 0 # The default value in case we have no VERB

    return left_embeddedness_score, non_verb_counts

def get_le_score(input, nlp, aggregator="sum"):
    """
    Argument `input`: 
    If input type is tokens the input should be in this format 
        [['token_1_of_sent_1', 'token_2_of_sent_1', ...],['token_1_of_sent_2', 'token_2_of_sent_2', ...]]
        Example : 
        [['This', 'is', 'token.ization', 'done', 'my', 'way!'], ['Sentence', 'split,', 'too!']])  

    If input type is string the input should be a simple standard python string 

    Argument `result_format`: has values `token` or `segment`
    Argument `aggregation_type` : has values `sum` , `mean` or `max`

    """

    doc = get_doc(input, nlp, ignore_empty_input=True)

    if doc==[]:
        return 0

    doc_verb_indicators=[]
    for sent in doc.sentences:
        verb_indicator=[]
        for word in sent.words:
                if is_aux_a_main_verb(word) or is_a_main_verb(word):
                    verb_indicator.append(True)
                else:
                    verb_indicator.append(False)     
        doc_verb_indicators.append(verb_indicator)

    score_lists=[]
    saved_score_lists=[]
    for verb_indicator in doc_verb_indicators:
        le_score = get_le_from_verb(verb_indicator,aggregator)
        score_lists.append(le_score[0])
        saved_score_lists.append(le_score)

    if aggregator == "sum":
        left_embeddedness_score=np.sum(score_lists)
    elif aggregator == "mean":
        left_embeddedness_score=np.mean(score_lists)
    elif aggregator == "max":
        left_embeddedness_score=np.max(score_lists)

    # possible values to return left_embeddedness_score, saved_score_lists, doc_verb_indicators
    return left_embeddedness_score