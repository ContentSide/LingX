from lingx.core.lang_model import get_nlp_object
from lingx.metrics.monolingual.le import get_le_score

def test_le():

    nlp_en = get_nlp_object("en", use_critt_tokenization = True, package="partut")

    input = [["The", "reporter", "who", "the", "senator", "who", "John", "met", "attacked"], ["disliked", "the", "editor", "."]]

    score = get_le_score(
                        input, 
                        nlp=nlp_en, 
                        aggregator="sum")  # choose `sum`, `max` or `mean`

    score_value = 7

    assert score == score_value
