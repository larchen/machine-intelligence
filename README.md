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

#### CLEVR/word_embeddings/google_news/CLEVR_google_news
Loads word2vec vector model pretrained Google News and filters embeddings for words used in CLEVR questions and answers. You can use Tensorboard for visualization of results.

## CLEVR baselines

#### CLEVR/rnn
Script using RNN (LSTM) for solving the QA task (i.e. using only questions from CLEVR). ("LSTM Q")

#### CLEVR/cnn
Script using CNN+RNN (LSTM) for solving the VQA task.



