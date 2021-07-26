# Tutorial 7: Getting Bilingual Complexity Ratio Metric

### Downloading Stanza Language Model

```python
import lingx.core.lang_model as lm

print("Downloading Language Models:")

lm.download_stanza_model("en", package="partut")
lm.download_stanza_model("zh-hans")
```

### Getting Bilingual Complexity Ratio Metric

```python
from lingx.utils import download_lang_models
from lingx.core.lang_model import get_nlp_object

nlp_en = get_nlp_object("en", use_critt_tokenization = True, package="partut")
nlp_zh = get_nlp_object("zh", use_critt_tokenization = True)

from lingx.utils.critt.aligner import generate_alignment_pipelines

from lingx.utils.critt.tables import readTPRDBtables
from lingx.utils.critt.tables import convert_st2segment , convert_tt2segment
from lingx.utils.critt.tables import expand_table_psycholingual , expand_table_monolingual , expand_table_bilingual
from lingx.utils.critt.tables import merge_st_tt , expand_table_error
```
This should print the metric list with related tokens and aggregated score using aggregated function `sum`:

```console
Aggregated Score == 8.67
```
Note that we can also provide string format input for arguments `tokens_source` and `tokens_target`, instead of list of list format. This is described in previous tutorials.

## Next

Now, let us look at how to [Read and Work with CRITT TPR-DB ](TUTORIAL_8_CRITT.md)