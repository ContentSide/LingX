import lingx.core.lang_model as lm


print("Downloading Language Models:")
lm.download_stanza_model("en", package="partut")
lm.download_stanza_model("zh-hans")