from lingx.core.lang_model import get_nlp_object
from lingx.utils.lx import get_sentence_lx

def test_idt_dlt():

    nlp_en = get_nlp_object("en", use_critt_tokenization = True, package="partut")

    input = [["The", "reporter", "who", "the", "senator", "who", "John", "met", "attacked"], ["disliked", "the", "editor", "."]]

    tokens_scores_list, aggregated_score = get_sentence_lx(
                                                        input,
                                                        nlp_en,
                                                        result_format="segment",
                                                        complexity_type="idt_dlt", 
                                                        aggregation_type="sum")  # choose `sum`, `max` or `mean`

    tokens_scores_list_value =[['The', 1], ['reporter', 1], ['who', 2], ['the', 3], 
                               ['senator', 2], ['who', 3], ['John', 4], ['met', 3], 
                               ['attacked', 0], ['disliked', 2], ['the', 3], ['editor', 1], ['.', 0]]
    aggregated_score_value = 25

    assert tokens_scores_list == tokens_scores_list_value
    assert aggregated_score == aggregated_score_value
