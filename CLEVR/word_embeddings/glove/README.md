## GloVe embeddings

Loads the pretrained GloVe embeddings (from embeddings.json). Vocabulary is stored in vocab.tsv. You can use Tensorboard for visualization of results.

### To run:

```
usage: CLEVR_glove.py [-h] ----embedding_file EMBEDDING_FILE --vocab_file VOCAB_FILE [--log_dir LOG_DIR]

required arguments:
  --embedding_file EMBEDDING_FILE     The file with embeddings
  --vocab_file VOCAB_FILE     The file with vocabulary

optional arguments:
  -h, --help                show this help message and exit
  --log_dir LOG_DIR         Summaries log directory
```


### To view embeddings:
In another terminal, run `tensorboard --logdir LOG_DIR` and go to localhost:6006 in your browser. To show the labels, click on the 'Load data' and upload VOCAB_FILE (tsv), which is in LOG_DIR


