# A module for calculating Incomplete Dependency and Distance Locality Theories in a sentence (either in tokens or string format)

from lingx.metrics.psycholingual.idt import get_idt_complexity
from lingx.metrics.psycholingual.dlt import get_dlt_complexity
from lingx.core.lang_features import aggregate_tokens



def calc_idt_dlt_complexity(self, tokens):
    tokens=[" " if t=="" else t for t in tokens]
    combined_complexity=[]
    
    idt_calc=self.calc_idt_complexity(tokens)
    dlt_calc=self.calc_dlt_complexity(tokens)

    for pair in zip(idt_calc,dlt_calc):
        combined_complexity.append([pair[0][0], pair[0][1]+pair[1][1]]) 

    return(combined_complexity)


def get_idt_dlt_complexity(input, nlp):

    combined_complexity = []
    
    idt = get_idt_complexity(input, nlp)
    dlt = get_dlt_complexity(input, nlp)

    for pair in zip(idt, dlt):
        combined_complexity.append([pair[0][0], pair[0][1]+pair[1][1]]) 

    return(combined_complexity)


def get_idt_dlt_score(input, nlp, result_format="token" , aggregation_type="sum"):
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
    token = get_idt_dlt_complexity(input, nlp)

    if result_format == "token":
        return token, None
    elif result_format == "segment":
        return token, aggregate_tokens(token, aggregation_type)
    else:
        raise Exception("Set `result_format` to `token` or `segment`.")