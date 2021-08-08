from lingx.core.lang_model import get_nlp_object
from lingx.metrics.monolingual.nnd import get_nnd_score

def test_mbn():

    nlp_en = get_nlp_object("en", use_critt_tokenization = True, package="partut")

    input = [["The", "reporter", "who", "the", "senator", "who", "John", "met", "attacked"], ["disliked", "the", "editor", "."]]

    score = get_nnd_score(
                        input, 
                        nlp=nlp_en, 
                        aggregator="sum",  # choose `sum`, `max` or `mean`
                        ploraity = False)  # if set to `True` the score will be absolute.

    score_value = 5

    assert score == score_value
