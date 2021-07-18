from lingx.core.lang_model import get_nlp_object

from lingx.metrics.psycholingual.idt import get_idt_complexity
from lingx.metrics.psycholingual.dlt import get_dlt_complexity
from lingx.metrics.psycholingual.idt_dlt import get_idt_dlt_complexity

from lingx.core.lang_features import aggregate_tokens


def compare_sentences_lx(
                        sent_a, 
                        sent_b,
                        nlp,
                        complexity_type="idt_dlt", 
                        aggregation_type="sum"):


    if complexity_type == "idt":
        sent_a_tokens = get_idt_complexity(sent_a, nlp)
        sent_b_tokens = get_idt_complexity(sent_b, nlp)

        sent_a_result = aggregate_tokens(sent_a_tokens, aggregation_type)
        sent_b_result = aggregate_tokens(sent_b_tokens, aggregation_type)

    elif complexity_type == "dlt":
        sent_a_tokens = get_dlt_complexity(sent_a, nlp)
        sent_b_tokens = get_dlt_complexity(sent_b, nlp)

        sent_a_result = aggregate_tokens(sent_a_tokens, aggregation_type)
        sent_b_result = aggregate_tokens(sent_b_tokens, aggregation_type)

    if complexity_type == "idt_dlt":
        sent_a_tokens = get_idt_dlt_complexity(sent_a, nlp)
        sent_b_tokens = get_idt_dlt_complexity(sent_b, nlp)

        sent_a_result = aggregate_tokens(sent_a_tokens, aggregation_type)
        sent_b_result = aggregate_tokens(sent_b_tokens, aggregation_type)

    return (sent_b_result > sent_a_result, sent_a_tokens, sent_b_tokens)
