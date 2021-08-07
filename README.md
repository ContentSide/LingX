![LingX](https://github.com/ContentSide/lingx/blob/master/resources/emblem/lingx.png)  
[![PyPI version](https://badge.fury.io/py/lingx.svg)](https://badge.fury.io/py/lingx)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
# LingX

**A library for introducing state-of-the-art metrics on measuring linguistic complexity developed by ContentSide and CRITT at Kent State University.**

---

**LingX is:**  

- A library for calculating some of the psycholinguistics complexity metrics.  
- A library for obtaining helpful metrics for translational process studies.  
- A library for different factors related to the text analysis.  
- A library with extended modules to easily integerate translational studies in CRITT TPR-DB.  

---

**How does LingX generally work?**

LingX calculates different token-based and segment-based mono-bilingual complexity metrics. It internaly parses a given text into a dependency grammar graph. Using the graph and other linguistic information such as part-of-speech tagging, it can caculates different psycholinguistics, linguistic and translational process metrics. See the reference section for detailed information.  

LingX uses [Stanza](https://stanfordnlp.github.io/stanza/) state-of-the-arts NLP library for different language-based tasks. Stanza is a collection of accurate and efficient tools for the linguistic analysis of many human languages. Stanza brings state-of-the-art NLP models to different languages.

## Quick Start

### Requirements and Installation

The project is based on Stanza 1.2.1 and Python 3.6+. If you do not have Python 3.6, install it first. Then, in your favorite virtual environment, simply do:

```
pip install lingx
```
If you are running project in Jupyter Notebook or Google Colab enviroments run the following command instead:  
```
!pip install lingx
```

### Example Usage

Let's run a simple token-based psycholingual incomplete complexity theory (IDT) metric as a test. All you need to do is to make import related methods and codes as follows:

```python
from lingx.utils import download_lang_models
from lingx.core.lang_model import get_nlp_object
from lingx.utils.lx import get_sentence_lx

nlp_en = get_nlp_object("en", use_critt_tokenization = False, package="partut")

input = "The reporter who the senator who John met attacked disliked the editor."

tokens_scores_list, aggregated_score = get_sentence_lx(
                                                       input,
                                                       nlp_en,
                                                       result_format="segment",
                                                       complexity_type="idt", 
                                                       aggregation_type="sum")

print(f"Tokens Scores List == {tokens_scores_list}")
print(f"Aggregated Score == {aggregated_score}")

```
This should print the incomplete complexity theory (IDT) metric list with related tokens and aggregated score using aggregated function `sum`:

```console
Tokens Scores List == [['The', 1], ['reporter', 2], ['who', 3], ['the', 4], ['senator', 3], ['who', 4], ['John', 5], ['met', 2], ['attacked', 2], ['disliked', 2], ['the', 3], ['editor', 1], ['.', 0]]
Aggregated Score == 32
```

## Tutorials

We provide a set of quick tutorials to get you started with the library:

* [Tutorial 1: Basics](resources/docs/TUTORIAL_1_BASICS.md)
* [Tutorial 2: Getting Incomplete Dependency Theory(=IDT) Metric](resources/docs/TUTORIAL_2_IDT.md)
* [Tutorial 3: Getting Dependency Locality Theory(=DLT) Metric](resources/docs/TUTORIAL_3_DLT.md)
* [Tutorial 4: Getting Combined IDT and DLT Metric](resources/docs/TUTORIAL_4_IDT_DLT.md)
* [Tutorial 5: Getting Left-Embededness Metric](resources/docs/TUTORIAL_5_LE.md)
* [Tutorial 6: Getting Nested Nouns Distance Metric](resources/docs/TUTORIAL_6_NND.md)
* [Tutorial 7: Getting Bilingual Complexity Ratio Metric](resources/docs/TUTORIAL_7_BCR.md)
* [Tutorial 8: Reading and Working with CRITT TPR-DB](resources/docs/TUTORIAL_8_CRITT.md)

The tutorials explain how the base metrics can be obtained. Let us know if anything is unclear.

## CRITT Translation Process Database (TPR-DB)
The CRITT Translation Process Database (TPR-DB) is released under [Creative Commons License (CC BY-NC-SA)](https://sites.google.com/site/centretranslationinnovation/tpr-db/license?authuser=0). Note that the available [EN-ZH_IMBst18](https://github.com/ContentSide/lingx/tree/master/resources/TPRDB/EN-ZH_IMBst18) database in this github belongs to CRITT TPR-DB.  

---

## Citing LingX

Please cite:

```
@inproceedings{Zou2021
  title={Syntactic Complexity and Translation Performance in English-to-Chinese Sight Translation},
  author={Zou, Longhui and Mirzapour, Mehdi and Jacquenet, Hélène},
  booktitle={Applied Linguistics and Professional Practice 2021},
  year={2021},
  publisher={Translational Data Analytics Institute, The Ohio State University}
}
```

For IDT-based and DLT-based complexities, please cite [this paper](https://hal.archives-ouvertes.fr/hal-02146506/document):

```
@incollection{mirzapour2020,
  title={Measuring Linguistic Complexity: Introducing a New Categorial Metric},
  author={Mirzapour, Mehdi and Prost, Jean-Philippe and Retor{\'e}, Christian},
  booktitle={Logic and Algorithms in Computational Linguistics 2018 (LACompLing2018)},
  pages={95--123},
  year={2020},
  publisher={Springer}
}
```

## Contact

Please email your questions or comments to [Mehdi Mirzapour](https://sites.google.com/view/mehdimirzapour/contact).

## [License](/LICENSE)

LingX is licensed under the following MIT License (MIT) Copyright © 2021 ContentSide and CRITT at Kent State University.
