# Manipulate TPRDB study-tables and perform different operations on them.

import pandas as pd
import numpy as np
import glob

from lingx.utils.lx import get_sentence_lx, get_sentence_mono_lingual
from lingx.utils.critt.aligner import get_alignment_offset

from lingx.metrics.bilingual.bcr import get_bcr_score


def readTPRDBtables(studies, table_type, verbose=0, path="/data/critt/tprdb/TPRDB/"):
    df = pd.DataFrame()
    
    for study in studies:
        if(verbose) : print("Reading: " + path + study + table_type)
        for fn in glob.glob(path + study + table_type):
            if(verbose > 1) : print("Reading: " + fn)
            df = pd.concat([df, pd.read_csv(fn, sep="\t", dtype=None)], ignore_index=True)
        
    return(df)


def convert_st2segment(df_st):
    analysis_st = (
                    pd.pivot_table(
                                    df_st,
                                    index=["Part","Text","STseg"], 
                                    values=["SToken"], 
                                    aggfunc=lambda x: '//'.join(x)
                                   )
                                    .reset_index()
                    )
    analysis_st["SToken"] = analysis_st["SToken"].apply(lambda x: [x.split("//")])
    
    return analysis_st



def convert_tt2segment(df_tt):
    analysis_tt = (
                    pd.pivot_table(
                                    df_tt,
                                    index=["Part","Text","TTseg"], 
                                    values=["TToken"], 
                                    aggfunc=lambda x: '//'.join(x)
                                   )
                                    .reset_index()
                    )
    analysis_tt["TToken"] = analysis_tt["TToken"].apply(lambda x: [x.split("//")])
    
    return analysis_tt




def expand_table_psycholingual(df_analysis, nlp, token_column="SToken"):

    df = df_analysis.copy()

    operation_list_st = [
                        ["idt","max","IDT_MAX_ST"],
                        ["idt","mean","IDT_MEAN_ST"],
                        ["idt","sum","IDT_SUM_ST"],
                        ["dlt","max","DLT_MAX_ST"],
                        ["dlt","mean","DLT_MEAN_ST"],
                        ["dlt","sum","DLT_SUM_ST"],
                        ["idt_dlt","max","IDT_DLT_MAX_ST"],
                        ["idt_dlt","mean","IDT_DLT_MEAN_ST"],
                        ["idt_dlt","sum","IDT_DLT_SUM_ST"],
    ]

    operation_list_tt = [
                        ["idt","max","IDT_MAX_TT"],
                        ["idt","mean","IDT_MEAN_TT"],
                        ["idt","sum","IDT_SUM_TT"],
                        ["dlt","max","DLT_MAX_TT"],
                        ["dlt","mean","DLT_MEAN_TT"],
                        ["dlt","sum","DLT_SUM_TT"],
                        ["idt_dlt","max","IDT_DLT_MAX_TT"],
                        ["idt_dlt","mean","IDT_DLT_MEAN_TT"],
                        ["idt_dlt","sum","IDT_DLT_SUM_TT"],
    ]


    if token_column == "SToken":
        operation_list = operation_list_st
    elif token_column == "TToken":
        operation_list = operation_list_tt
    else:
        raise Exception("Set `token_column` to one of the following values: `SToken` or `TToken`.")



    for item in operation_list:

        func = lambda x : get_sentence_lx(
                                            x,
                                            nlp,
                                            result_format="segment",
                                            complexity_type=item[0], 
                                            aggregation_type=item[1]
                                        )[1]

        df[item[2]]=df[token_column].apply(func)
        df[item[2]]=df[token_column].apply(func)

    return df


def expand_table_monolingual(df_analysis, nlp, token_column="SToken"):

    df = df_analysis.copy()

    operation_list_st = [
                        ["le","mean","LE_MEAN_ST"],
                        ["le","max","LE_MAX_ST"],
                        ["le","sum","LE_SUM_ST"],
                        ["mbn","mean","MBN_MEAN_ST"],
                        ["mbn","max","MBN_MAX_ST"],
                        ["mbn","sum","MBN_SUM_ST"]
    ]


    operation_list_tt = [
                        ["le","mean","LE_MEAN_TT"],
                        ["le","max","LE_MAX_TT"],
                        ["le","sum","LE_SUM_TT"],
                        ["mbn","mean","MBN_MEAN_TT"],
                        ["mbn","max","MBN_MAX_TT"],
                        ["mbn","sum","MBN_SUM_TT"]
    ]


    if token_column == "SToken":
        operation_list = operation_list_st
    elif token_column == "TToken":
        operation_list = operation_list_tt
    else:
        raise Exception("Set `token_column` to one of the following values: `SToken` or `TToken`.")


    for item in operation_list:

        func = lambda x : get_sentence_mono_lingual(x, nlp, mono_lingual_type=item[0], aggregation_type=item[1])
        
        df[item[2]]=df[token_column].apply(func)

    return df


def expand_table_bilingual(analysis_st_tt, nlp_source, nlp_target):

    df = analysis_st_tt.copy()

    bcr_aggregation_list = ["sum", "max", "mean"]
    lx_aggregation_list = ["sum"]

    for first_agg in bcr_aggregation_list:
        for second_agg in bcr_aggregation_list:
            for lx in lx_aggregation_list:

                func = lambda x : get_bcr_score(
                                            nlp_source,
                                            nlp_target,
                                            complexity_type = "idt_dlt", # "idt", "dlt", "idt_dlt"
                                            input_source = x["SToken"],
                                            input_target = x["TToken"],
                                            source_target_alignments = x["alignment"],
                                            complexity_aggregation_function= lx,         # max, mean, sum
                                            first_aggregation_function= first_agg,       # max, mean, sum
                                            second_aggregation_function = second_agg,    # max, mean, sum
                                            robust=True,
                                            bcr_error_value=0
                                    )

                label = "BCR" +  "_" + lx.capitalize() +"_" + first_agg.capitalize() + "_" + second_agg.capitalize()
                df[label] = df.apply(func, axis=1)

    return df




def merge_st_tt(analysis_st, analysis_tt, alignments_offset):

    analysis_st_renamed = analysis_st.rename(columns = {"STseg":"TTseg"})
    analysis_st_renamed = analysis_st_renamed[["Part", "Text", "TTseg", "SToken"]]

    analysis_tt_extended = pd.merge(analysis_tt,
                                    analysis_st_renamed,
                                    on=["Part", "Text", "TTseg"], 
                                    how='left')

    analysis_tt_extended["alignment"] = analysis_tt_extended.apply(
                                                                    lambda x: get_alignment_offset(
                                                                                x["Part"], x["Text"], x["TTseg"], 
                                                                                alignments_offset),
                                                                    axis=1
                                                                    )

    return analysis_tt_extended



def adhoc_cleanup(analysis_st_tt):

    df = analysis_st_tt.copy()

    condition = (df["Part"]=="P07") & (df["Text"]==1)  & (df["TTseg"]==4)
    df = df.drop(df[condition].index)

    condition = (df["Part"]=="P07") & (df["Text"]==1)  & (df["TTseg"]==5)
    df = df.drop(df[condition].index)

    condition = (df["Part"]=="P07") & (df["Text"]==1)  & (df["TTseg"]==6)
    df = df.drop(df[condition].index)


    condition = (df["Part"]=="P01") & (df["Text"]==5)  & (df["TTseg"]==4)
    df = df.drop(df[condition].index)

    condition = (df["Part"]=="P01") & (df["Text"]==5)  & (df["TTseg"]==5)
    df = df.drop(df[condition].index)

    condition = (df["Part"]=="P01") & (df["Text"]==5)  & (df["TTseg"]==6)
    df = df.drop(df[condition].index)

    return df