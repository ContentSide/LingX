# Tutorial 8: Reading and Working with CRITT TPR-DB

This is the exact ALAPP 2021 paper's experiment using EN-ZH_IMBst18 CRITT TPR-DB available in the github. The jupyter notebook can be found [here](../ALAPP2021/ALAPP_2021_Paper.ipynb).


### Install LingX

```python
!pip install lingx
```


### Downloading Stanza Language Models

```python
import lingx.core.lang_model as lm

print("Downloading Language Models:")

lm.download_stanza_model("en", package="partut")
lm.download_stanza_model("zh-hans")
```

### Import Libraries

```python
import lingx.utils.download_lang_models
from lingx.core.lang_model import get_nlp_object

nlp_en = get_nlp_object("en", use_critt_tokenization = True, package="partut")
nlp_zh = get_nlp_object("zh", use_critt_tokenization = True)

from lingx.utils.critt.aligner import generate_alignment_pipelines

from lingx.utils.critt.tables import readTPRDBtables
from lingx.utils.critt.tables import convert_st2segment , convert_tt2segment
from lingx.utils.critt.tables import expand_table_psycholingual , expand_table_monolingual , expand_table_bilingual
from lingx.utils.critt.tables import merge_st_tt , expand_table_error
```

### Convert ST an TT to Segment DataFrames

```python
!git clone https://github.com/ContentSide/lingx.git
path_to_tprdb = "/content/lingx/resources/TPRDB/EN-ZH_IMBst18/"

df_sg = readTPRDBtables(['Tables/'], "*sg", verbose=1, path=path_to_tprdb)
df_st = readTPRDBtables(['Tables/'], "*st", verbose=1, path=path_to_tprdb)
df_tt = readTPRDBtables(['Tables/'], "*tt", verbose=1, path=path_to_tprdb)

alignments_offset = generate_alignment_pipelines(df_st, df_tt)

analysis_st = convert_st2segment(df_st)
analysis_tt = convert_tt2segment(df_tt)

analysis_st
```

### Calculate Metrics

```python
import numpy
import time

start_time = time.time()

analysis_st = expand_table_psycholingual(analysis_st, nlp_en, token_column="SToken")
analysis_tt = expand_table_psycholingual(analysis_tt, nlp_zh, token_column="TToken")

analysis_st =  expand_table_monolingual(analysis_st, nlp_en, token_column="SToken")
analysis_tt =  expand_table_monolingual(analysis_tt, nlp_zh, token_column="TToken")

analysis_st_tt = merge_st_tt(analysis_st, analysis_tt, alignments_offset)
analysis_st_tt = expand_table_bilingual(analysis_st_tt, nlp_en, nlp_zh, robust=True, bcr_error_value=numpy.nan)


print(analysis_st_tt)
print(analysis_st_tt.columns)

print("Running Time (Min): ",round((time.time() - start_time)/60,0))
```

### Connect the Metric Results to Human-level Analysis

```python
error_file_path = "/content/lingx/resources/TPRDB/EN-ZH_IMBst18/HumanEvaluations/errors.csv"
analysis_st_tt = expand_table_error(analysis_st_tt, error_file_path)

analysis_st_tt.columns
```

### Filter Table on Numeric Measures

```python
table = analysis_st_tt[[
                       'IDT_MAX_TT', 'IDT_MEAN_TT','IDT_SUM_TT', 'DLT_MAX_TT', 'DLT_MEAN_TT', 'DLT_SUM_TT',
                        'IDT_DLT_MAX_TT', 'IDT_DLT_MEAN_TT', 'IDT_DLT_SUM_TT', 'LE_MEAN_TT',
                        'LE_MAX_TT', 'LE_SUM_TT', 'NND_MEAN_TT', 'NND_MAX_TT', 'NND_SUM_TT',
                        'SToken', 'IDT_MAX_ST', 'IDT_MEAN_ST', 'IDT_SUM_ST', 'DLT_MAX_ST',
                        'DLT_MEAN_ST', 'DLT_SUM_ST', 'IDT_DLT_MAX_ST', 'IDT_DLT_MEAN_ST',
                        'IDT_DLT_SUM_ST', 'LE_MEAN_ST', 'LE_MAX_ST', 'LE_SUM_ST', 'NND_MEAN_ST',
                        'NND_MAX_ST', 'NND_SUM_ST', 'Alignment', 'BCR_SUM_SUM_SUM',
                        'BCR_SUM_SUM_MAX', 'BCR_SUM_SUM_MEAN', 'BCR_SUM_MAX_SUM',
                        'BCR_SUM_MAX_MAX', 'BCR_SUM_MAX_MEAN', 'BCR_SUM_MEAN_SUM',
                        'BCR_SUM_MEAN_MAX', 'BCR_SUM_MEAN_MEAN', 'SessionSeg', 'Any',
                        'Accuracy', 'Fluency', 'Style', 'Critical', 'Minor'
                        ]]
```

### Correlation Matrix

```python
report = table.corr(method="spearman")
report[['Any','Accuracy','Fluency','Style','Critical','Minor']]
```

### P-values Matrix

```python
from scipy.stats import kendalltau, pearsonr, spearmanr

def kendall_pval(x,y):
    return kendalltau(x,y)[1]

def pearsonr_pval(x,y):
    return pearsonr(x,y)[1]

def spearmanr_pval(x,y):
    return spearmanr(x,y)[1]
```

```python
report = table.corr(method=spearmanr_pval)
# report.to_csv("report.csv")

report = report[['Any','Accuracy','Fluency','Style','Critical','Minor']]
report = report<=0.05
report = report.replace(True, "(*)")
report = report.replace(False, "")
report
```