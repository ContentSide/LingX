# A module for calculating Bilingual Complexity Ratio in a give source and target texts

import numpy as np

from lingx.utils.lx import get_sentence_lx
from lingx.core.lang_model import get_doc



def has_misalignment(input_source, input_target, source_target_alignments):

    # set `side` as 0 for verification of source indexes
    # set `side` as 1 for verification of target indexes
    def report_index_error(tokens_input, source_target_alignments, side):   
        error_tag = False
        len_list=[]

        if isinstance(tokens_input, str):
            tokens_input = [tokens_input.split(" ")]


        for item in tokens_input:
            len_list.append(len(item))
        length=sum(len_list)


        for item in source_target_alignments:
            for number in item[side]:
                if number >= length:
                    error_tag = True
                    break

        return error_tag

    source_err_flag = report_index_error(input_source, source_target_alignments, side=0)
    target_err_flag = report_index_error(input_target, source_target_alignments, side=1)

    return (source_err_flag or target_err_flag)





def get_bcr_score_(
                    tokens_source_complexity,
                    tokens_target_complexity,
                    source_target_alignments,
                    first_aggregation_function= "sum",    # max, mean, sum
                    second_aggregation_function = "sum"   # max, mean, sum
                    ):

    scores=[]
    for item in source_target_alignments:
        left_scores=[]
        right_scores=[]

        for left_item in item[0]:
            left_scores.append(tokens_source_complexity[left_item][1])

        for right_item in item[1]:
            right_scores.append(tokens_target_complexity[right_item][1])

        if first_aggregation_function == "sum":
            st_score=np.sum(left_scores)
            tt_score=np.sum(right_scores)
        elif first_aggregation_function == "mean":
            st_score=np.mean(left_scores)
            tt_score=np.mean(right_scores)
        elif first_aggregation_function == "max":
            st_score=np.max(left_scores)
            tt_score=np.max(right_scores)
        else:
            st_score=np.sum(left_scores)
            tt_score=np.sum(right_scores)

        scores.append(tt_score/st_score)


    if second_aggregation_function == "sum":
        bcr_score=np.sum(scores)
    elif second_aggregation_function == "mean":
        bcr_score=np.mean(scores)
    elif second_aggregation_function == "max":
        if scores!= []:
            bcr_score=np.max(scores)
        else:
            bcr_score=0
    else:
        bcr_score=np.sum(scores)

    return bcr_score





def get_bcr_score(
                    nlp_source,
                    nlp_target,
                    complexity_type, # IDT, DLT, IDT+DLT
                    input_source,
                    input_target,
                    source_target_alignments,
                    complexity_aggregation_function= "sum",    # max, mean, sum
                    first_aggregation_function= "sum",         # max, mean, sum
                    second_aggregation_function = "sum",       # max, mean, sum
                    robust=True,
                    bcr_error_value=0):




    has_error = has_misalignment(input_source, input_target, source_target_alignments)

    if has_error and robust:
        return (bcr_error_value)
    elif has_error and not robust:
        raise Exception("A misalignmet exist in input_source={}, input_target={} and alignment={}.".format(input_source, input_target, source_target_alignments))


    tokens_source_complexity , _ =  get_sentence_lx(
                                                input_source,
                                                nlp_source,
                                                result_format="token",
                                                complexity_type=complexity_type, 
                                                aggregation_type=complexity_aggregation_function
                                                )

    tokens_target_complexity , _ =  get_sentence_lx(
                                                input_target,
                                                nlp_target,
                                                result_format="token",
                                                complexity_type=complexity_type, 
                                                aggregation_type=complexity_aggregation_function
                                                )


    bcr_score = get_bcr_score_(
                                tokens_source_complexity,
                                tokens_target_complexity,
                                source_target_alignments,
                                first_aggregation_function,
                                second_aggregation_function
                               )
    
    return bcr_score


