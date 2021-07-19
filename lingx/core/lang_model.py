import stanza

def download_stanza_model(stanza_model, package="default"):
    stanza.download(stanza_model, package=package)


def get_nlp_object(stanza_model, use_critt_tokenization = True, package="default"):

    if use_critt_tokenization:
        nlp = stanza.Pipeline(stanza_model, package=package, processors='tokenize, pos, lemma, depparse', tokenize_pretokenized=True)
    else:
        nlp = stanza.Pipeline(stanza_model, package=package,  processors='tokenize, pos, lemma, depparse', tokenize_pretokenized=False)

    return nlp, use_critt_tokenization
    

# In order to avoid following stanza libraray error this subroutine should be run
# AssertionError: id and text should be included for the token
def convert_blank2space(input):

    tokens_list=[]
    for items in input:
        tokens=[]
        for token in items:
            if token == "":
                tokens.append(" ")
            else:
                tokens.append(token)
        tokens_list.append(tokens)
    
    return tokens_list


# `use_critt_tokenization` argument is problematic in general 
# the following procedure handles the complexity
def get_doc(input, nlp, ignore_empty_input=False):
    
    ignore_empty_list = [
                            "", 
                            [], 
                            [[]]
                        ]

    if ignore_empty_input and input in ignore_empty_list:
            return []

    if nlp[1] and isinstance(input, list):
        input = convert_blank2space(input)
        doc = nlp[0](input)
    elif nlp[1] and (not isinstance(input, list)):
        raise Exception("You have set `use_critt_tokenization` to True but not used real tokens (in list_of_list format) as segment!")
    elif (not nlp[1]) and isinstance(input, str):
        doc = nlp[0](input)
    elif (not nlp[1]) and (not isinstance(input, str)):
        raise Exception("You have set `use_critt_tokenization` to False but not used real string as sentence!")

    return(doc)




