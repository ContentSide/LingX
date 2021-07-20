# Manipulate TPRDB study-tables and perform different operations on them.

import pandas as pd
import numpy as np
import glob

from lingx.utils.lx import get_sentence_lx


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

    operation_list = [
                    ["idt","max","IDT_MAX"],
                    ["idt","mean","IDT_MEAN"],
                    ["idt","sum","IDT_SUM"],
                    ["dlt","max","DLT_MAX"],
                    ["dlt","mean","DLT_MEAN"],
                    ["dlt","sum","DLT_SUM"],
                    ["idt_dlt","max","IDT_DLT_MAX"],
                    ["idt_dlt","mean","IDT_DLT_MEAN"],
                    ["idt_dlt","sum","IDT_DLT_SUM"],
    ]


    for item in operation_list:

        func = lambda x : get_sentence_lx(
                                            x,
                                            nlp,
                                            result_format="segment",
                                            complexity_type=item[0], 
                                            aggregation_type=item[1]
                                        )

        def func_lx(x):
            return func(x)[1]

        df[item[2]]=df[token_column].apply(func_lx)
        df[item[2]]=df[token_column].apply(func_lx)

    return df