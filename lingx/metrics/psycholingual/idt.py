# A module for calculating Incomplete Dependency Theory in a sentence (either in tokens or string format)

from lingx.core.lang_features import get_linguistic_features
from lingx.core.lang_features import aggregate_tokens
from lingx.core.lang_model import get_doc

def get_idt_complexity(input, nlp):

    idt_complexity=[]
    doc = get_doc(input, nlp)

    links , links_compact = get_linguistic_features(doc)
    

    for i in range(len(links_compact)):
        backward_links_above_index_i=[link for link in links if (link[1][0]<=i and link[0][0]>=(i+1))]
        forward_links_above_index_i=[link for link in links if (link[0][0]<=i and link[1][0]>=(i+1))]
        links_above_index_i=backward_links_above_index_i+forward_links_above_index_i
        idt_complexity.append([links[i][1][1], len(links_above_index_i)])

    return(idt_complexity)



def get_idt_score(input, nlp, result_format="token" , aggregation_type="sum"):
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
    token = get_idt_complexity(input, nlp)

    if result_format == "token":
        return token, None
    elif result_format == "segment":
        return token, aggregate_tokens(token, aggregation_type)
    else:
        raise Exception("Set `result_format` to `token` or `segment`.")



