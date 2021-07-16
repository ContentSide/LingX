from lingx.metrics.psycholingual.idt import get_idt_complexity
from lingx.metrics.psycholingual.dlt import get_dlt_complexity
from lingx.metrics.psycholingual.idt_dlt import get_idt_dlt_complexity

from lingx.core.lang_model import get_nlp_object

nlp_en = get_nlp_object("en", use_critt_tokenization = True)
idt = get_idt_complexity( 
                        [['This', 'is', 'token.ization', 'done', '', 'way!'], ['Sentence', 'split,', 'too!']], 
                        nlp_en
                        )
print(idt)

nlp_en = get_nlp_object("en", use_critt_tokenization = False)
idt = get_dlt_complexity( 
                        "This is tokenization done my way! Sentence split too!",
                        nlp_en
                        )
print(idt)


nlp_en = get_nlp_object("en", use_critt_tokenization = False)
dlt = get_idt_dlt_complexity( 
                        "The reporter who the senator who John met attacked disliked the editor",
                        nlp_en
                        )
print(dlt)

dlt = get_idt_dlt_complexity( 
                        "The reporter who the senator who I met attacked disliked the editor",
                        nlp_en
                        )
print(dlt)

nlp_en = get_nlp_object("en", use_critt_tokenization = True)
dlt = get_dlt_complexity( 
                        [['This', 'is', 'token.ization', 'done', '', 'way!'], ['Sentence', 'split,', 'too!']], 
                        nlp_en
                        )
print(dlt)