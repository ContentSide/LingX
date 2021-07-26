# Tutorial 4: Getting Left-Embededness Metric 

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

Now, let us look at how to get [Number of Modifiers Before Noun Metric](TUTORIAL_6_MBN.md)
