# Machine Intelligence

Larry Chen's project as internship in Machine Intelligence team, IBM Research, Almaden

Contains TF-based scripts and ipython notebooks related to CLEVR and VQA.

Detailed descriptions and usages of particular scripts are placed in subdirectories

## Main folder

#### CLEVR/CLEVR_questions.ipynb
Notebook displaying the statistics of CLEVR train.

## Word embeddings

#### CLEVR/word_embeddings/CLEVR_word2vec.py
Trains word2vec on CLEVR questions and answers, stores results (vocabulary) in metadata.tsv. You can use Tensorboard for visualization of results.

#### CLEVR/word_embeddings/glove/CLEVR_glove.py
Loads the pretrained GloVe embeddings (from embeddings.json). Vocabulary is stored in vocab.tsv. You can use Tensorboard for visualization of results.

#### CLEVR/word_embeddings/glove/CLEVR_glove.py


This repository hosts the `word2vec` pre-trained **Google News** corpus (3 billion running words) word vector model (3 million 300-dimension English word vectors). 

It is mirroring the data from the official [word2vec website](https://code.google.com/archive/p/word2vec/):  
[GoogleNews-vectors-negative300.bin.gz](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing)

The motivation was to provide an easy (programmatical) way to download the model file via `git clone` instead of accessing the Google Drive link.

You will need to install [git lfs](https://git-lfs.github.com/) to be able to clone this.
