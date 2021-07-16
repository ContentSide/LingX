from lingx.core.lang_features import get_linguistic_features, convert_blank2space


def get_idt_complexity(input, nlp):
    """
    If input type is tokens the input should be in this format 
        [['token_1_of_sent_1', 'token_2_of_sent_1', ...],['token_1_of_sent_2', 'token_2_of_sent_2', ...]]
        Example : 
        [['This', 'is', 'token.ization', 'done', 'my', 'way!'], ['Sentence', 'split,', 'too!']])  

    If input type is string the input should be a simple standard python string 
    """
    idt_complexity=[]
    if isinstance(input, list):
        input = convert_blank2space(input)
    doc = nlp(input)
    links , links_compact = get_linguistic_features(doc)
    

    for i in range(len(links_compact)):
        backward_links_above_index_i=[link for link in links if (link[1][0]<=i and link[0][0]>=(i+1))]
        forward_links_above_index_i=[link for link in links if (link[0][0]<=i and link[1][0]>=(i+1))]
        links_above_index_i=backward_links_above_index_i+forward_links_above_index_i
        idt_complexity.append([links[i][1][1], len(links_above_index_i)])

    return(idt_complexity)