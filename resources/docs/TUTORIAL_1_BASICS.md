# Tutorial 1: Basics

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
This will run only download English and Chinese language models with calling following codes:

```python
import lingx.core.lang_model as lm

print("Downloading Language Models:")

lm.download_stanza_model("en", package="partut")
lm.download_stanza_model("zh-hans")
```

If other language models are needed one can add the desired language models by adding/removing the above code. The list of available [stanza language models](https://stanfordnlp.github.io/stanza/available_models.html) can be explored.

### Getting NLP Object

The following code can assign a NLP language model with the same language name and package that is already downloaded. Noticd that seting `use_critt_tokenization` to `True` will let the NLP object accept the already existing tokenized segment while setting it to `False` will let the the internal tokenizer do the tokenization on string level. 

```python
nlp = get_nlp_object("en", use_critt_tokenization = True, package="partut")

```

### Philosophy behind use_critt_tokenization?

The philosphy behind the `use_critt_tokenization` is swithching between two different kind of inputs smoothly:

In summary, if `use_critt_tokenization` is set to `True` one should input the segment in this format (Python's list of list format):

```console
[['token_1_of_sent_1', 'token_2_of_sent_1', ...],['token_1_of_sent_2', 'token_2_of_sent_2', ...]]
```
Here is an example 

```console
[['This', 'is', 'token.ization', 'done', 'my', 'way!'], ['Sentence', 'split,', 'too!']])  
```

While, if `use_critt_tokenization` is set to `False` one should input the segment in this format (Python's string format):

```console
"This is token.ization done my way!, Sentence split too!"
```

It is obvious since that the input is string and it is not already toknzied. That is why the internal Stanza tokenizer will be called under the hood. Notice that if an inconsistency happens between the `input` and `use_critt_tokenization` an error message will be prompted.

## Next

Now, let us look at how to get [Incomplete Dependency Theory(=IDT) Metric](TUTORIAL_2_IDT.md).
