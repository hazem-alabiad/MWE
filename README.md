# Arabic Verbal Multiword Expressions (VMWEs) and LLMs

## Introduction and motivation

Arabic has an increadible degree of flexibiility which makes it difficult to analuyze by machines. So far, many of the NLP tasks such as Named Entity Recognition (NER) and continous MWE are solved, we still struggle with discontinous VMWEs.
In this project, we aim to test and evaluate how accurately  LLM can catch these VMWEs especially when they have lots of intervening words in between (discontinuisity).

## Data

PARSEME-AR 1.3

## Research Questions

1. How well the SOTA LLMs can catch VMWEs in Arabic?
2. Does the intervening words downgrade the performance of the LLM detecting VMWEs (discontinuity )?
3. Does providing a few shots help the LLM detect the VMWEs better compared to zero-shot?
