# A module for calculating Distance Locality Theory in a sentence (either in tokens or string format)

from lingx.core.lang_features import get_linguistic_features
from lingx.core.lang_features import aggregate_tokens
from lingx.core.lang_model import get_doc


acceptable_discourse_referents = ["PROPN", "NOUN", "VERB"]


def get_longest_link(links, links_compact):
    backward_longest_links=[]

    for link in links:
        for indx in range(0,link[1][0]):
            if ([link[1][0], indx] in links_compact):
                backward_longest_links.append([link[1][0], indx])
                break

    return(backward_longest_links)


def get_dlt_complexity(input, nlp):
    """
    If input type is tokens the input should be in this format 
        [['token_1_of_sent_1', 'token_2_of_sent_1', ...],['token_1_of_sent_2', 'token_2_of_sent_2', ...]]
        Example : 
        [['This', 'is', 'token.ization', 'done', 'my', 'way!'], ['Sentence', 'split,', 'too!']])  

    If input type is string the input should be a simple standard python string 
    """
    doc = get_doc(input, nlp)

    links , links_compact = get_linguistic_features(doc)
    backward_longest_links=get_longest_link(links, links_compact)

    dlt_complexity_partial=[]
    for link in backward_longest_links:
        accepted_pos=[]
        for indx in range(link[0]-1,link[1]-1,-1):
            pos=links[indx][1][2]
            if pos in acceptable_discourse_referents: 
                accepted_pos.append(pos)
        dlt_complexity_partial.append([link[0], len(accepted_pos)])
    
    dlt_complexity=[]
    token_indices=[indx for indx, _ in dlt_complexity_partial]

    for i in range(len(links_compact)):
        if i not in token_indices:
            dlt_complexity.append([links[i][1][1], 0])
        else:
            dlt_complexity.append([links[i][1][1], *[pair[1] for pair in dlt_complexity_partial if pair[0]==i]])
    
    return(dlt_complexity)




def get_dlt_score(input, nlp, result_format="token" , aggregation_type="sum"):
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
    token = get_dlt_complexity(input, nlp)

    if result_format == "token":
        return token, None
    elif result_format == "segment":
        return token, aggregate_tokens(token, aggregation_type)
    else:
        raise Exception("Set `result_format` to `token` or `segment`.")