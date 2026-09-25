# Project Roadmap & Research Framework

### **1. Short Project Roadmap**

Your project pipeline moves from dataset parsing to prompt engineering, multi-model execution, and error analysis:

1. **Data Preprocessing & Dataframe Conversion:** Parse raw PARSEME-AR 1.3 `.cupt` files using `conllu`. Map multi-label semicolons and column 10/11 (`parseme:mwe`) to extract sentences, MWE gold-standard dictionaries, MWE types (**LVC.full**, **VID**, **IAV**, **LVC.cause**), and exact token indices.
2. **Exploratory Data Analysis (EDA):** Quantify total sentences (6,091), total MWEs (3,841), category distribution, and identify the subset of **discontinuous MWEs** (1,606 cases, ~42% of all MWEs) containing intervening tokens.
3. **Prompt Engineering & Formatting (`src/prompter.py`):** Construct **Zero-Shot** and **Few-Shot** prompt templates. Enforce valid JSON output, incorporate explicit warnings regarding non-adjacent/discontinuous tokens, and instruct models to extract base forms.
4. **Model Execution & Benchmarking:** Run automated inference across different LLM architectures—comparing proprietary generalist models (**GPT-4o**, **Claude 3.5 Sonnet**), open-source baselines (**Llama-3**), and Arabic-centric models (**Jais**, **AceGPT**).
5. **Evaluation & Gap-Length Analysis:** Calculate Information Extraction (IE) metrics—**Precision**, **Recall**, and **F1-Score**—under both **Exact Match** and **Partial Match** rules. Plot F1-score performance decay as a function of **gap size** (number of intervening tokens) to explain LLM failures.

---

### **2. Main Research Questions (RQs) & Core Goals**

* **Primary Project Goal:** Evaluate the capability and limitations of modern Large Language Models in extracting complex, discontinuous Arabic Verbal Multiword Expressions from text without manual syntactic parsing.

* **Key Research Questions:**
  * **RQ1 (Extraction Accuracy):** How accurately can state-of-the-art generalist LLMs extract complex Arabic verbal expressions (**LVCs** and **VIDs**) compared to open-source and language-specialized baselines?
  * **RQ2 (Impact of Discontinuity & Gap Size):** To what extent does the presence and length of **intervening tokens (discontinuity)** degrade model F1-scores compared to continuous expressions?
  * **RQ3 (Prompting & Opacity):** Does providing **few-shot, grammatically structured prompts** improve an LLM’s extraction accuracy on semantically opaque idioms (**VIDs**) versus syntactically predictable light verb constructions (**LVCs**)?

---

### **3. Closely Related Studies to Cite and Compare Against**

1. **Arabic PARSEME Corpus & Guidelines:**
   * **Hadj Mohamed et al. (LREC 2022)** – [Annotating Verbal Multiword Expressions in Arabic: Assessing the Validity of a Multilingual Annotation Procedure](https://aclanthology.org/2022.lrec-1.240/)
     * *Relevance:* The foundational paper extending PARSEME guidelines to Modern Standard Arabic using the Prague Arabic Dependency Treebank (PADT). It provides the benchmark annotation rules for Arabic LVCs, VIDs, and IAVs and notes that Arabic has a high rate of discontinuous VMWEs (17.3% with gaps > 3 tokens).
2. **Discontinuous MWE Neural Identification:**
   * **Rohanian et al. (NAACL 2019)** – [Bridging the Gap: Attending to Discontinuity in Identification of Multiword Expressions](https://aclanthology.org/N19-1273/)
     * *Relevance:* A key neural baseline paper specifically addressing discontinuous token gaps using Graph Convolutional Networks (GCNs) over dependency trees combined with self-attention. Comparing your LLM prompt results against their gap-size performance curves provides strong academic context.
3. **Joint Syntactic Parsing & Arabic MWE Extraction:**
   * **Green, de Marneffe, and Manning (Computational Linguistics 2013)** – [Parsing Models for Identifying Multiword Expressions](https://aclanthology.org/J13-1002/)
     * *Relevance:* Explores Tree Substitution Grammars (TSGs) and factored lexicons for joint parsing and MWE extraction in Arabic and French, showing that syntactic context outperforms traditional $n$-gram surface statistics.
4. **PARSEME Shared Task Benchmarks:**
   * **Savary et al. (2017) / Ramisch et al. (2018, 2020)** – [The PARSEME Shared Task on Automatic Identification of Verbal Multiword Expressions](https://parsemefr.lis-lab.fr/parseme-st-guidelines/)
     * *Relevance:* Establishes the international evaluation framework, defining per-MWE and per-token precision/recall metrics for evaluating VMWE extraction systems.
5. **Arabic MWE Repositories & Pattern Matching:**
   * **Hawwari, Bar, and Diab (2012)** – [Building an Arabic Multiword Expressions Repository](https://aclanthology.org/W12-1004/)
     * *Relevance:* Curates 4,200+ Arabic MWEs categorized by Verb-Noun (VNC) and Verb-Particle (VPC) constructions and evaluates pattern matching across inflected gaps.
