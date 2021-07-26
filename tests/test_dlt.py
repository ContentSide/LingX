from lingx.core.lang_model import get_nlp_object
from lingx.utils.lx import get_sentence_lx

def test_dlt():

    nlp_en = get_nlp_object("en", use_critt_tokenization = True, package="partut")

    input = [["The", "reporter", "who", "the", "senator", "who", "John", "met", "attacked"], ["disliked", "the", "editor", "."]]

    tokens_scores_list, aggregated_score = get_sentence_lx(
                                                        input,
                                                        nlp_en,
                                                        result_format="segment",
                                                        complexity_type="dlt", 
                                                        aggregation_type="sum")  # choose `sum`, `max` or `mean`

    tokens_scores_list_value = [['The', 0], ['reporter', 0], ['who', 0], ['the', 0], 
                                ['senator', 0], ['who', 0], ['John', 0], ['met', 2], 
                                ['attacked', 0], ['disliked', 0], ['the', 0], ['editor', 0], ['.', 0]]
    aggregated_score_value = 2

    assert tokens_scores_list == tokens_scores_list_value
    assert aggregated_score == aggregated_score_value
