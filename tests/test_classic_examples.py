from lingx.utils import download_lang_models
from lingx.core.lang_model import get_nlp_object
from lingx.utils.lx import compare_sentences_lx

nlp_en = get_nlp_object("en", use_critt_tokenization = False, package="partut")
nlp_zh = get_nlp_object("zh", use_critt_tokenization = False)


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
    "That that two plus two equals four surprised Jack astonished Ingrid."]
]

for sent in sentences:
    result = compare_sentences_lx(
                        sent[0], 
                        sent[1],
                        nlp=nlp_en,
                        complexity_type="idt_dlt", 
                        aggregation_type="sum")

    print()
    print(f"Sentence 1 : {result[1]}")
    print(f"Sentence 2 : {result[2]}")
    print(f"Fx(Sentence 2) > Fx(Sentence 1) : {result[0]}")
    print()