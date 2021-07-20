from lingx.core.lang_model import get_nlp_object


from lingx.utils.lx import compare_sentences_lx
from lingx.utils.lx import get_sentence_lx


from lingx.metrics.monolingual.le import get_le_score
from lingx.metrics.monolingual.mbn import get_mbn_score
from lingx.metrics.bilingual.bcr import get_bcr_score

from lingx.utils.critt.aligner import generate_alignment_pipelines
from lingx.utils.critt.tables import readTPRDBtables
from lingx.utils.critt.tables import convert_st2segment , convert_tt2segment
from lingx.utils.critt.tables import expand_table_psycholingual



nlp_en = get_nlp_object("en", use_critt_tokenization = True, package="partut")
nlp_zh = get_nlp_object("zh", use_critt_tokenization = True)


sentences = [
    ["The reporter who the senator who I met attacked disliked the editor.",
    "The reporter who the senator who John met attacked disliked the editor."],
    ["The reporter who sent the photographer to the editor hoped for a good story.",
    "The reporter who the photographer sent to the editor hoped for a good story."],
    ["The horse raced past the barn.", 
    "The horse raced past the barn fell."],
    ["The dog that chased the cat that saw the rat barked.", 
    "The cheese that the rat that the cat saw ate stank."],
    ["Jack was surprised that two plus two equals four.", 
    "The fact that two plus two equals four surprised Jack."],
    ["Ingrid was astonished that Jack was surprised that two plus two equals four.", 
    "The fact that that two plus two equals four surprised Jack astonished Ingrid."],
    ["Frank was bothered that Ingrid was astonished that Jack was surprised that two plus two equals four.", 
    "The fact that that that that that two plus two equals four surprised Jack astonished Ingrid bothered Frank."],
    ["John gave Bill the painting that Mary hated.", 
    "John gave the painting that Mary hated to Bill."],
    ["That two plus two equals four surprised Jack.",
    "That that two plus two equals four surprised Jack astonished Ingrid."],
    ["",""]
]

# tokens= [['This', 'is', 'token.ization', 'done', 'my', 'way!'], ['Sentence', 'split,', 'too!']]
# le = get_le_score(tokens, nlp=nlp_en, aggregator="max")
# mbn = get_mbn_score(tokens, nlp=nlp_en, aggregator="max")

# print(le, mbn)

# for sent in sentences:
#     result = compare_sentences_lx(
#                         sent[0], 
#                         sent[1],
#                         nlp=nlp_en,
#                         complexity_type="idt_dlt", 
#                         aggregation_type="sum")

#     print(result[0])
#     print(result[1])
#     print(result[2])
#     le = get_le_score(sent[0], nlp=nlp_en, aggregator="mean")
#     mbn = get_mbn_score(sent[1], nlp=nlp_en, aggregator="mean")
#     print(le, mbn)
#     print("__________________")


# tokens_source = [['It', 'has', 'the', 'right', 'members', 'and', 'the', 'right', 'mandate', '.']]
# tokens_target = [['在', '今年', '的', '四月', '阿布特', '部长', '跟', '安倍', '部长', '同意', '为', '增强', '经济发展', '增强', '后', '合作', '，', '并且', '为', '太平洋', '地区', '的', '和平', '和', '稳定', '增强', '合作', '。']]


# source_target_alignments = [
    
#     [[5, 9], [5, 6, 188]], 
    
#     [[8], [11]]
    
#     ]


# bcr_score = get_bcr_score(
#                                 nlp_source = nlp_en,
#                                 nlp_target = nlp_zh,
#                                 complexity_type = "idt_dlt", # "idt", "dlt", "idt_dlt"
#                                 input_source = tokens_source,
#                                 input_target = tokens_target,
#                                 source_target_alignments = source_target_alignments,
#                                 complexity_aggregation_function= "sum",    # max, mean, sum
#                                 first_aggregation_function= "sum",         # max, mean, sum
#                                 second_aggregation_function = "sum",       # max, mean, sum
#                                 robust=False,
#                                 bcr_error_value=0)
    

# print(bcr_score)



# input = [['It', 'has', 'the', 'right'], ['members', 'and', 'the', 'right', 'mandate', '.']]


# score = get_sentence_lx(
#                     input,
#                     nlp_en,
#                     result_format="segment",
#                     complexity_type="idt_dlt", 
#                     aggregation_type="sum")


# print(score)


path_to_tprdb = "resources/TPRDB/EN-ZH_IMBst18/"
df_sg = readTPRDBtables(['Tables/'], "*sg", verbose=1, path=path_to_tprdb)
df_st = readTPRDBtables(['Tables/'], "*st", verbose=1, path=path_to_tprdb)
df_tt = readTPRDBtables(['Tables/'], "*tt", verbose=1, path=path_to_tprdb)

alignments_offset = generate_alignment_pipelines(df_st, df_tt)


analysis_st = convert_st2segment(df_st)
analysis_tt = convert_tt2segment(df_tt)


analysis_st = expand_table_psycholingual(analysis_st[:5], nlp_en, token_column="SToken")
analysis_tt = expand_table_psycholingual(analysis_tt[:5], nlp_zh, token_column="TToken")

print(analysis_st)
print(analysis_tt)