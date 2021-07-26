# Tutorial 4: Getting Combined IDT and DLT Metric  

### Downloading Stanza Language Model

```python
import lingx.core.lang_model as lm

print("Downloading English Language Model:")

lm.download_stanza_model("en", package="partut")
```

### Getting Segment-Level Combined IDT-DLT-based Complexity

```python
from lingx.core.lang_model import get_nlp_object
from lingx.utils.lx import get_sentence_lx

nlp_en = get_nlp_object("en", use_critt_tokenization = False, package="partut")

input = "The reporter who the senator who John met attacked disliked the editor."

tokens_scores_list, aggregated_score = get_sentence_lx(
                                                       input,
                                                       nlp_en,
                                                       result_format="segment",
                                                       complexity_type="idt_dlt", 
                                                       aggregation_type="sum")  # choose `sum`, `max` or `mean`

print(f"Tokens Scores List == {tokens_scores_list}")
print(f"Aggregated Score == {aggregated_score}")
```
This should print the metric list with related tokens and aggregated score using aggregated function `sum`:

```console
Tokens Scores List == [['The', 1], ['reporter', 2], ['who', 3], ['the', 4], ['senator', 3], ['who', 4], ['John', 5], ['met', 4], ['attacked', 2], ['disliked', 2], ['the', 3], ['editor', 1], ['.', 0]]
Aggregated Score == 34
```

### Getting Segment-Level Combined IDT-DLT-based Complexity (with Tokenized Input)

```python
from lingx.core.lang_model import get_nlp_object
from lingx.utils.lx import get_sentence_lx

nlp_en = get_nlp_object("en", use_critt_tokenization = True, package="partut")

input = [["The", "reporter", "who", "the", "senator", "who", "John", "met", "attacked"], ["disliked", "the", "editor", "."]]

tokens_scores_list, aggregated_score = get_sentence_lx(
                                                       input,
                                                       nlp_en,
                                                       result_format="segment",
                                                       complexity_type="idt_dlt", 
                                                       aggregation_type="sum")  # choose `sum`, `max` or `mean`

print(f"Tokens Scores List == {tokens_scores_list}")
print(f"Aggregated Score == {aggregated_score}")
```
This should print the metric list with related tokens and aggregated score using aggregated function `sum`:

```console
Tokens Scores List == [['The', 1], ['reporter', 1], ['who', 2], ['the', 3], ['senator', 2], ['who', 3], ['John', 4], ['met', 3], ['attacked', 0], ['disliked', 2], ['the', 3], ['editor', 1], ['.', 0]]
Aggregated Score == 25
```

### Getting Only Token-Level Combined IDT-DLT-based Complexity (without Aggregated Score)

```python
from lingx.core.lang_model import get_nlp_object
from lingx.utils.lx import get_sentence_lx

nlp_en = get_nlp_object("en", use_critt_tokenization = False, package="partut")

input = "The reporter who the senator who John met attacked disliked the editor."

tokens_scores_list, _ = get_sentence_lx(
                                        input,
                                        nlp_en,
                                        result_format="token",
                                        complexity_type="idt_dlt", 
                                        aggregation_type="sum")  # choose `sum`, `max` or `mean`

print(f"Tokens Scores List == {tokens_scores_list}")
```
This should print the metric list with related tokens only:

```console
Tokens Scores List == [['The', 1], ['reporter', 2], ['who', 3], ['the', 4], ['senator', 3], ['who', 4], ['John', 5], ['met', 4], ['attacked', 2], ['disliked', 2], ['the', 3], ['editor', 1], ['.', 0]]
```  

## Next

Now, let us look at how to get [Left-Embededness Metric](TUTORIAL_5_LE.md)
