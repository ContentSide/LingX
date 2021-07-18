import stanza

def download_stanza_model(stanza_model, package="default"):
    stanza.download(stanza_model, package=package)


def get_nlp_object(stanza_model, use_critt_tokenization = True, package="default"):

    if use_critt_tokenization:
        nlp = stanza.Pipeline(stanza_model, package=package, processors='tokenize, pos, lemma, depparse', tokenize_pretokenized=True)
    else:
        nlp = stanza.Pipeline(stanza_model, package=package,  processors='tokenize, pos, lemma, depparse', tokenize_pretokenized=False)

    return nlp



