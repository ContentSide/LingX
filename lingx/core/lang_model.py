import stanza

def download_stanza_model(stanza_model):
    stanza.download(stanza_model)


def get_nlp_object(stanza_model, use_critt_tokenization = True):

    if use_critt_tokenization:
        nlp = stanza.Pipeline(stanza_model, processors='tokenize, pos, lemma, depparse', tokenize_pretokenized=True)
    else:
        nlp = stanza.Pipeline(stanza_model, processors='tokenize, pos, lemma, depparse', tokenize_pretokenized=False)

    return(nlp)



