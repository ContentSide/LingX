![alt text](resources/ContentSide.png)  
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
# LingX

**A library for introducing state-of-the-art metrics on measuring linguistic complexity developed by ContentSide and CRITT at Kent State University.**

---

**LingX is:**  

- A library for calculating some of the psycholinguistics complexity metrics.  
- A library for obtaining helpful metrics for translational process studies.  
- A library for different factors related to the text analysis.  

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

### Example Usage

Let's run a simple token-based incomplete dependencies difficulty measure. All you need to do is to make import related methode as follows:

```python
from lingx.idt import get_nested_np_modifiers_score
from lingx.tools.critt 
```

This should print:

```console
from lingx.metrics.bilingual import get_nested_np_modifiers_score
from lingx.utils.critt 
```

## Tutorials

We provide a set of quick tutorials to get you started with the library:

* [Tutorial 1: Installation](/docs/TUTORIAL_1_BASICS.md)
* [Tutorial 2: Getting Psycholingual Metrics](/docs/TUTORIAL_2_PSYCHOLINGUAL.md)
* [Tutorial 3: Getting Monolingual Metrics](/docs/TUTORIAL_3_MONOLINGUAL.md)
* [Tutorial 4: Getting Bilingual Metrics](/docs/TUTORIAL_4_BILINGUAL.md)
* [Tutorial 5: Reading and Working with CRITT TPR-DB ](/docs/TUTORIAL_5_CRITT.md)

The tutorials explain how the base metrics can be obtained. Let us know if anything is unclear.



## Citing LingX

Please cite [the following paper]:

```
@inproceedings{
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
