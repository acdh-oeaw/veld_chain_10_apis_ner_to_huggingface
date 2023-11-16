# select, convert and publish to huggingface

This repo:
- has as source an internal gitlab data repo, and as target repo a huggingface dataset repo.
- selects one of several data options from the APIS NER datasets, which is simple 
and cleaned.
- converts the ASCII encoding to UTF-8 (since default json python library wrote as ASCII in the
  source repo).

