import numpy as np
from lingx.core.lang_model import get_nlp_object
from lingx.metrics.bilingual.bcr import get_bcr_score

def test_bcr():

    nlp_en = get_nlp_object("en", use_critt_tokenization = True, package="partut")
    nlp_zh = get_nlp_object("zh", use_critt_tokenization = True)

    tokens_source = [['It', 'has', 'the', 'right', 'members', 'and', 'the', 'right', 'mandate', '.']]
    tokens_target = [['在', '今年', '的', '四月', '阿布特', '部长', '跟', '安倍', '部长', 
                    '同意', '为', '增强', '经济发展', '增强', '后', '合作', '，', '并且', 
                    '为', '太平洋', '地区', '的', '和平', '和', '稳定', '增强', '合作', '。']]


    source_target_alignments = [

        [[5, 9], [5, 6, 18]], 

        [[8], [11]]

        ]


    score = get_bcr_score(
                        nlp_source = nlp_en,
                        nlp_target = nlp_zh,
                        complexity_type = "idt_dlt", # "idt", "dlt", "idt_dlt"
                        input_source = tokens_source,
                        input_target = tokens_target,
                        source_target_alignments = source_target_alignments,
                        complexity_aggregation_function= "sum",    # max, mean, sum
                        first_aggregation_function= "sum",         # max, mean, sum
                        second_aggregation_function = "sum",       # max, mean, sum
                        robust=True,  # if set to `False` the error will be reported in case of alignment mismatch 
                        bcr_error_value=np.nan)  # if `robust` set to `True` the error will NOT be 
                                                    # reported and the `bcr_error_value` will be reported instead

    score_value = 8.7

    assert score_value >= score
