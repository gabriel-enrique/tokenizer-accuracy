# Tokenizer Accuracy

Measure the accuracy of tokenizers on Bahasa Indonesia sentences.

> This repository stores the source code for the Natural Language Processing (2022/2023 Term 1) course first group project.

There are 2 tokenizer that are used for this test:

1. [Bahasa](https://github.com/andryluthfi/indonesian-postag)
1. [Aksara](https://github.com/ir-nlp-csui/aksara)

Those tokenizers will tokenize sentences from these 2 datasets:

1. [Indonesian-PUD](https://github.com/UniversalDependencies/UD_Indonesian-PUD)
1. [Indonesian-GSD](https://github.com/UniversalDependencies/UD_Indonesian-GSD)

Both tokenizer will not only tokenize the given sentence but will also stem, lemmatize, POS tag, and do other stuffs. Because of this, modifications are made such that the tokenizers will only produce the tokenization results in order to save time and computing resources.

The `aksara_tokenizer.py` module contains the algorithm to count the accuracy of a tokenization results, given the tokenization gold standard.

The whole process starting from preparing the dataset, tokenization, and accuracy scoring can be seen inside the `tokenization.ipynb` Jupyter Notebook.

