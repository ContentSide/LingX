# Tutorial 3: Getting Dependency Locality Theory(=DLT) Metric

### Downloading Stanza Language Model

```python
import lingx.core.lang_model as lm

print("Downloading English Language Model:")

lm.download_stanza_model("en", package="partut")
```

### Getting Segment-Level DLT-based Complexity

```python
from lingx.core.lang_model import get_nlp_object
from lingx.utils.lx import get_sentence_lx

nlp_en = get_nlp_object("en", use_critt_tokenization = False, package="partut")

input = "The reporter who the senator who John met attacked disliked the editor."

tokens_scores_list, aggregated_score = get_sentence_lx(
                                                       input,
                                                       nlp_en,
                                                       result_format="segment",
                                                       complexity_type="dlt", 
                                                       aggregation_type="sum")  # choose `sum`, `max` or `mean`

print(f"Tokens Scores List == {tokens_scores_list}")
print(f"Aggregated Score == {aggregated_score}")
```
This should print the metric list with related tokens and aggregated score using aggregated function `sum`:

```console
Tokens Scores List == [['The', 0], ['reporter', 0], ['who', 0], ['the', 0], ['senator', 0], ['who', 0], ['John', 0], ['met', 2], ['attacked', 0], ['disliked', 0], ['the', 0], ['editor', 0], ['.', 0]]
Aggregated Score == 2
```

### Getting Segment-Level IDT-based Complexity (with Tokenized Input)

```python
from lingx.core.lang_model import get_nlp_object
from lingx.utils.lx import get_sentence_lx

nlp_en = get_nlp_object("en", use_critt_tokenization = True, package="partut")

input = [["The", "reporter", "who", "the", "senator", "who", "John", "met", "attacked"], ["disliked", "the", "editor", "."]]

tokens_scores_list, aggregated_score = get_sentence_lx(
                                                       input,
                                                       nlp_en,
                                                       result_format="segment",
                                                       complexity_type="dlt", 
                                                       aggregation_type="sum")  # choose `sum`, `max` or `mean`

print(f"Tokens Scores List == {tokens_scores_list}")
print(f"Aggregated Score == {aggregated_score}")
```
This should print the metric list with related tokens and aggregated score using aggregated function `sum`:

```console
Tokens Scores List == [['The', 0], ['reporter', 0], ['who', 0], ['the', 0], ['senator', 0], ['who', 0], ['John', 0], ['met', 2], ['attacked', 0], ['disliked', 0], ['the', 0], ['editor', 0], ['.', 0]]
Aggregated Score == 2
```

### Getting Only Token-Level IDT-based Complexity (without Aggregated Score)

```python
from lingx.core.lang_model import get_nlp_object
from lingx.utils.lx import get_sentence_lx

nlp_en = get_nlp_object("en", use_critt_tokenization = False, package="partut")

input = "The reporter who the senator who John met attacked disliked the editor."

tokens_scores_list, _ = get_sentence_lx(
                                        input,
                                        nlp_en,
                                        result_format="token",
                                        complexity_type="dlt", 
                                        aggregation_type="sum")  # choose `sum`, `max` or `mean`

print(f"Tokens Scores List == {tokens_scores_list}")
```
This should print the metric list with related tokens only:

```console
Tokens Scores List == [['The', 0], ['reporter', 0], ['who', 0], ['the', 0], ['senator', 0], ['who', 0], ['John', 0], ['met', 2], ['attacked', 0], ['disliked', 0], ['the', 0], ['editor', 0], ['.', 0]]
```  

## Next

Now, let us look at how to get [Combined IDT and DLT Metric](TUTORIAL_4_IDT_DLT.md)
