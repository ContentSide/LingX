# Tutorial 5: Getting Left-Embededness Metric 

### Downloading Stanza Language Model

```python
import lingx.core.lang_model as lm

print("Downloading English Language Model:")

lm.download_stanza_model("en", package="partut")
```

### Getting Left-Embededness Metric 

```python
from lingx.core.lang_model import get_nlp_object
from lingx.metrics.monolingual.le import get_le_score

nlp_en = get_nlp_object("en", use_critt_tokenization = False, package="partut")

input = "The reporter who the senator who John met attacked disliked the editor."

score = get_le_score(
                     input, 
                     nlp=nlp_en, 
                     aggregator="sum")  # choose `sum`, `max` or `mean`

print(f"Aggregated Score == {score}")
```
This should print the metric list with related tokens and aggregated score using aggregated function `sum`:

```console
Aggregated Score == 7
```
### Getting Left-Embededness Metric (with Tokenized Input)

```python
from lingx.core.lang_model import get_nlp_object
from lingx.metrics.monolingual.le import get_le_score

nlp_en = get_nlp_object("en", use_critt_tokenization = True, package="partut")

input = [["The", "reporter", "who", "the", "senator", "who", "John", "met", "attacked"], ["disliked", "the", "editor", "."]]

score = get_le_score(
                     input, 
                     nlp=nlp_en, 
                     aggregator="sum")  # choose `sum`, `max` or `mean`

print(f"Aggregated Score == {score}")
```
This should print the metric list with related tokens and aggregated score using aggregated function `sum`:

```console
Aggregated Score == 7
```

## Next

Now, let us look at how to get [Nested Nouns Distance Metric](TUTORIAL_6_NND.md)
