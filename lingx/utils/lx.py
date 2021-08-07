from lingx.core.lang_model import get_nlp_object

from lingx.metrics.psycholingual.idt import get_idt_score
from lingx.metrics.psycholingual.dlt import get_dlt_score
from lingx.metrics.psycholingual.idt_dlt import get_idt_dlt_score
from lingx.metrics.monolingual.le import get_le_score
from lingx.metrics.monolingual.nnd import get_nnd_score

from lingx.core.lang_features import aggregate_tokens


def compare_sentences_lx(
                        sent_a, 
                        sent_b,
                        nlp,
                        complexity_type="idt_dlt", 
                        aggregation_type="sum"):


    if complexity_type == "idt":
        result_a = get_idt_score(sent_a, nlp, result_format="segment" , aggregation_type=aggregation_type)
        result_b = get_idt_score(sent_b, nlp, result_format="segment" , aggregation_type=aggregation_type)

    elif complexity_type == "dlt":
        result_a = get_dlt_score(sent_a, nlp, result_format="segment" , aggregation_type=aggregation_type)
        result_b = get_dlt_score(sent_b, nlp, result_format="segment" , aggregation_type=aggregation_type)

    if complexity_type == "idt_dlt":
        result_a = get_idt_dlt_score(sent_a, nlp, result_format="segment" , aggregation_type=aggregation_type)
        result_b = get_idt_dlt_score(sent_b, nlp, result_format="segment" , aggregation_type=aggregation_type)

    return (result_b[1] > result_a[1], result_a[0], result_b[0])




def get_sentence_lx(
                    input,
                    nlp,
                    result_format="token",
                    complexity_type="idt_dlt", 
                    aggregation_type="sum"):

    if complexity_type == "idt":
        score = get_idt_score(input, nlp, result_format=result_format , aggregation_type=aggregation_type)
    elif complexity_type == "dlt":
        score = get_dlt_score(input, nlp, result_format=result_format , aggregation_type=aggregation_type)
    elif complexity_type == "idt_dlt":
        score = get_idt_dlt_score(input, nlp, result_format=result_format , aggregation_type=aggregation_type)
    else:
        raise Exception("Set `complexity_type` to one of the following values: `idt` , `dlt` or `idt_dlt`.")
    
    return score



def get_sentence_mono_lingual(
                                input, nlp,
                                mono_lingual_type="le",  # 'le' or 'nnd'
                                aggregation_type="sum"):

    if mono_lingual_type == "le":
        score = get_le_score(input, nlp, aggregation_type)
    elif mono_lingual_type == "nnd":
        score = get_nnd_score(input, nlp, aggregation_type)
    else:
        raise Exception("Set `mono_lingual_type` to one of the following values: `le` or `nnd`.")
    
    return score
