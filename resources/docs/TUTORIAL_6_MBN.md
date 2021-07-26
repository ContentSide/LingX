# Tutorial 6: Getting Number of Modifiers Before Noun Metric

### Downloading Stanza Language Model

```python
import lingx.core.lang_model as lm

print("Downloading English Language Model:")

lm.download_stanza_model("en", package="partut")
```

### Getting Number of Modifiers Before Noun Metric

```python
from lingx.core.lang_model import get_nlp_object
from lingx.metrics.monolingual.mbn import get_mbn_score

nlp_en = get_nlp_object("en", use_critt_tokenization = False, package="partut")

input = "The reporter who the senator who John met attacked disliked the editor."

score = get_mbn_score(
                      input, 
                      nlp=nlp_en, 
                      aggregator="sum",  # choose `sum`, `max` or `mean`
                      ploraity = False)  # if set to `True` the score will be absolute.

print(f"Aggregated Score == {score}")
```
This should print the metric list with related tokens and aggregated score using aggregated function `sum`:

```console
Aggregated Score == 5
```
### Getting Number of Modifiers Before Noun Metric (with Tokenized Input)

```python
from lingx.core.lang_model import get_nlp_object
from lingx.metrics.monolingual.mbn import get_mbn_score

nlp_en = get_nlp_object("en", use_critt_tokenization = True, package="partut")

input = [["The", "reporter", "who", "the", "senator", "who", "John", "met", "attacked"], ["disliked", "the", "editor", "."]]

score = get_mbn_score(
                      input, 
                      nlp=nlp_en, 
                      aggregator="sum",  # choose `sum`, `max` or `mean`
                      ploraity = False)  # if set to `True` the score will be absolute.

print(f"Aggregated Score == {score}")
```
This should print the metric list with related tokens and aggregated score using aggregated function `sum`:

```console
Aggregated Score == 5
```

## Next

Now, let us look at how to get [Bilingual Complexity Ratio Metric](TUTORIAL_7_BCR.md)
