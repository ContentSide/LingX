import stanza
import numpy as np
import lingx.core.lang_model as lm


print("Downloading Language Models:")
lm.download_stanza_model("en")
lm.download_stanza_model("zh-hans")