# Tutorial 1: Basics
---

### Requirements and Installation

The project is based on Stanza 1.2.1 and Python 3.6+. If you do not have Python 3.6, install it first. Then, in your favorite virtual environment, simply do:

```
pip install lingx
```
If you are running project in Jupyter Notebook or Google Colab enviroments run the following command instead:  
```
!pip install lingx
```

### Downloading Stanza Language Models

Here are the codes:

```python
from lingx.utils import download_lang_models
```
This will run only download English and Chinese language models with under the hood codes:

```python
import lingx.core.lang_model as lm

print("Downloading Language Models:")

lm.download_stanza_model("en", package="partut")
lm.download_stanza_model("zh-hans")
```

If other language models are needed one can add the above code with consulting [the stanza language model pages](https://stanfordnlp.github.io/stanza/available_models.html).


The following code can assign a NLP language model with the same language name and package that is already downloaded. Noticd that seting `use_critt_tokenization` to `True` will let the NLP object accept the already existing tokenized segment while setting it to `False` will let the the internal tokenizer do the tokenization on string level. 

```python
nlp = get_nlp_object("en", use_critt_tokenization = True, package="partut")

```


## Next

Now, let us look at how to get [Incomplete Dependency Theory(=IDT) Metric](resources/docs/TUTORIAL_2_IDT.md).
