![alt text](resources/ContentSide.png)  
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
# LingX

**A library for introducing state-of-the-art metrics on measuring linguistic complexity developed by ContentSide and CRITT at Kent State University.**

---

**LingX is:**  

- A library for measuring linguistic complexity.  
- A library for measuring translational process studies.  
- A library for calculating some of the psycholinguistics metrics.  
- A library under-development for different factors related to the text analysis.  

---

**How does LingX generally work?**

LingX calculates different token-based and segment-based mono-bilingual complexity metrics. It internaly parses a given text into a dependency grammar graph. Using the graph and other linguistic information such as part-of-speech tagging, it can caculates different psycholinguistics, linguistic and translational process difficulties. See the reference section for detailed information. 

LingX uses [Stanza](https://stanfordnlp.github.io/stanza/) state-of-the-arts NLP library for different language-based tasks. Stanza is a collection of accurate and efficient tools for the linguistic analysis of many human languages. Stanza brings state-of-the-art NLP models to different languages.

## Quick Start

### Requirements and Installation

The project is based on Stanza 1.2.1 and Python 3.6+. If you do not have Python 3.6, install it first. Then, in your favorite virtual environment, simply do:

```
pip install lingx
```

### Example Usage

Let's run a simple token-based incomplete dependencies difficulty measure. All you need to do is make import related methode as follows:

```python
from lingx.idt import get_nested_np_modifiers_score
from lingx.tools.critt 
```

This should print:

```console
from lingx.idt import get_nested_np_modifiers_score
from lingx.tools.critt 
```