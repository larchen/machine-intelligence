## Word2vec embeddings pretrained Google News 

Loads word2vec vector model pretrained Google News and filters embeddings for words used in CLEVR questions and answers. You can use Tensorboard for visualization of results.

The `word2vec` pre-trained **Google News** corpus (3 billion running words) word vector model (3 million 300-dimension English word vectors) can be downloaded from:

The official [word2vec website](https://code.google.com/archive/p/word2vec/):  
[GoogleNews-vectors-negative300.bin.gz](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing)

Or manually:

wget -c "https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz"

### To run:

```
usage: python CLEVR_google_news [-h] --embedding_file EMBEDDING_BINARY_FILE [--vocab_file VOCAB_FILE --log_dir LOG_DIR]

required arguments:
  --embedding_file EMBEDDING_BINARY_FILE     The binary file containing embeddings (default: ./GoogleNews-vectors-negative300.bin.gz)

optional arguments:
  -h, --help                show this help message and exit
  --vocab_file VOCAB_FILE     The file with vocabulary
  --log_dir LOG_DIR         Summaries log directory (default: logs/)
```


### To view embeddings:
In another terminal, run `tensorboard --logdir LOG_DIR` and go to localhost:6006 in your browser. To show the labels, click on the 'Load data' and upload metadata.tsv, which is in LOG_DIR

