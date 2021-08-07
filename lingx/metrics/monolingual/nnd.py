# A module for calculating Nested Nouns Distance in a sentence

import numpy as np
from treelib import Tree, Node


from lingx.core.lang_features import is_a_noun, convert_dep2tree
from lingx.core.lang_model import get_doc



def get_nnd_from_noun_indicator(noun_indicator, tree, aggregator="mean", ploraity = False):
    scores = []

    if len(noun_indicator) > 1:
        for index in range(len(noun_indicator)-1):
            fst = noun_indicator[index]
            snd = noun_indicator[index+1]

            if tree.is_ancestor(fst, snd):
                score = fst-snd
            elif tree.is_ancestor(snd, fst):
                score = snd-fst
            else:
                score = 0

            if ploraity:
                scores.append(score)
            else:
                scores.append(abs(score))
    else:
        scores.append(0)

    if len(noun_indicator) > 0:
        if aggregator == "sum":
            nested_nouns_distance_score=np.sum(scores)
        elif aggregator == "mean":
            nested_nouns_distance_score=np.mean(scores)
        elif aggregator == "max":
            nested_nouns_distance_score=np.max(scores)
    else:
        nested_nouns_distance_score = 0 # The default value in case we have no NOUN

    return nested_nouns_distance_score, scores


def get_nnd_score(input, nlp, aggregator="sum", ploraity = False):
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

    sent_list_pairs = []
    for sent in doc.sentences:
        list_pairs=[]
        noun_indicator = []

        for word in sent.words:
            
            if is_a_noun(word):
                noun_indicator.append(word.id)

            if word.head == 0:
                list_pairs.append([word.head, word.id, "root", word.text])
            else:
                list_pairs.append([word.head, word.id, sent.words[word.head-1].text, word.text])
        sent_list_pairs.append([list_pairs,noun_indicator])


    score_lists=[]
    saved_score_lists=[]
    for list_pairs in sent_list_pairs:
        dep_tree = convert_dep2tree(list_pairs[0])
        nnd_score = get_nnd_from_noun_indicator(list_pairs[1], dep_tree, aggregator, ploraity)
        score_lists.append(nnd_score[0])
        saved_score_lists.append(nnd_score)


    if aggregator == "sum":
        nested_nouns_distance_score=np.sum(score_lists)
    elif aggregator == "mean":
        nested_nouns_distance_score=np.mean(score_lists)
    elif aggregator == "max":
        nested_nouns_distance_score=np.max(score_lists)

    # possible return values for further tests are nested_nouns_distance_score, saved_score_lists, sent_list_pairs
    return nested_nouns_distance_score


    