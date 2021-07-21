"""
The module is about CRITT TPR-DB alignment.

The most important function in this module is `generate_alignment_pipelines`

It takes as the inputs ST and TT dataframes and returns alignment dictionary in the following format

{"P08_5_3":
            [   
                [[5, 9], [5, 6, 18]],  
                [[8], [11]]
            ]
}

Note that as for the Participant=08 , Text=5 , Segment=3 in the above 
example the source tokens [5,9] is aligned with target tokens [5,6,18]
and the source token [8] is aligned with target token [11] 

"""


import pandas as pd


def generate_orginal_alignment_list(target_dataframe):

    df = target_dataframe[['Id','TToken','Text', 'TTseg', 'Part', 'STid']]
    df["Part_Text_TTseg"] = df.apply(lambda x : str(x['Part']) + "_" + str(x['Text']) + "_" + str(x['TTseg']), axis=1)
    df = df[['Id', 'Part_Text_TTseg', 'STid','TToken']]
    df.columns = ['TTid', 'Part_Text_TTseg', 'STid','TToken']

    alignments_original={}

    for item in list(df["Part_Text_TTseg"].unique()):
        ptt = df[df["Part_Text_TTseg"] == item]
        alignments_original[item]=[]
        for value in list(ptt["STid"].unique()):
            if value != "---" :
                ttids = ptt[ptt["STid"]==value]
                st = [int(item) for item in value.split("+")]
                tt = list(ttids["TTid"])
                alignments_original[item].append([ st, tt ])

    return alignments_original


def get_offset_list(source_dataframe, target_dataframe):


    df_tt_filtered = target_dataframe[['Id','TToken','Text', 'TTseg', 'Part', 'STid']]
    df_tt_filtered["Part_Text_TTseg"] = df_tt_filtered.apply(lambda x : str(x['Part']) + "_" + str(x['Text']) + "_" + str(x['TTseg']), axis=1)
    df_tt_filtered = df_tt_filtered[['Id', 'Part_Text_TTseg', 'STid','TToken']]
    df_tt_filtered.columns = ['TTid', 'Part_Text_TTseg', 'STid','TToken']


    df_st_filtered = source_dataframe[['Id','SToken','Text', 'STseg', 'Part', 'TTid']]
    df_st_filtered["Part_Text_STseg"] = df_st_filtered.apply(lambda x : str(x['Part']) + "_" + str(x['Text']) + "_" + str(x['STseg']), axis=1)
    df_st_filtered = df_st_filtered[['Id', 'Part_Text_STseg', 'TTid','SToken']]
    df_st_filtered.columns = ['STid', 'Part_Text_STseg', 'TTid','SToken']

    offset_list={}

    for item in list(df_tt_filtered["Part_Text_TTseg"].unique()):
        pttt = df_tt_filtered[df_tt_filtered["Part_Text_TTseg"] == item]
        ptst = df_st_filtered[df_st_filtered["Part_Text_STseg"] == item]
        offset_list[item]=[]
        offset_list[item].append((ptst["STid"].min(),pttt["TTid"].min()))

    return offset_list


def generate_reindexed_alignment_list(alignments_original, offset_list):

    alignments_offset={}

    for item in alignments_original:
        alignments_offset[item]=[]
        st_offset = offset_list[item][0][0]
        tt_offset = offset_list[item][0][1]
        
        for align in alignments_original[item]:
            ss_items = []
            tt_items = []
            for left_item in align[0]:
                left_item -= st_offset
                ss_items.append(left_item)
            for right_item in align[1]:
                right_item -= tt_offset
                tt_items.append(right_item)

            alignments_offset[item].append([ss_items,tt_items])

    return alignments_offset


def generate_alignment_pipelines(df_st, df_tt):

    alignments_original = generate_orginal_alignment_list(df_tt)
    offset_list = get_offset_list(df_st, df_tt)
    alignments_offset =  generate_reindexed_alignment_list(alignments_original, offset_list)

    return alignments_offset


def get_alignment_offset(part, text, ttseg, alignments_offset):
    global_id = str(part) + "_" + str(text) + "_" + str(ttseg)

    for item in alignments_offset:
        if item == global_id:
            return alignments_offset[item]
    return None