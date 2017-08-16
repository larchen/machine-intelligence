import os
import sys
import json
import argparse

import numpy as np
import tensorflow as tf
import gensim
from tensorflow.contrib.tensorboard.plugins import projector

FLAGS = None

def build_embedding_matrix(embedding_file, vocab_file):
  # Load the word2vec pretrained on Google news corpus.
  print ("Loading the binary vector embeddings, this might take a while...")
  model = gensim.models.KeyedVectors.load_word2vec_format(embedding_file, binary=True)
  # Get vocabulary from external file.
  vocabulary = [word.strip() for word in open(vocab_file)]
  # Create empty embedding - with embedding size of 300 (as original model embeddings are of size 300).
  embedding = np.zeros((len(vocabulary), 300))
  for i, word in enumerate(vocabulary):
    try:
      # Find the word in the model.
      vec = model.word_vec(word).reshape(1, 300)
      # Add vector to embedding.
      embedding[i] = vec
    except KeyError:
      print('\"%s\" has no word vector' %(word))
  return embedding

def build_and_run_graph(word_vectors):
  graph = tf.Graph()
  config = projector.ProjectorConfig()

  with graph.as_default():  
    embedding_tensor = tf.Variable(word_vectors, name='google_news_embeddings')
    
    embedding = config.embeddings.add()
    embedding.tensor_name = embedding_tensor.name
    # embedding.metadata_path = FLAGS.vocab_file

    init = tf.global_variables_initializer()

  with tf.Session(graph=graph) as session:
    init.run()

    summary_writer = tf.summary.FileWriter('logs', session.graph)
    projector.visualize_embeddings(summary_writer, config)
    saver = tf.train.Saver()

    saver.save(session, os.path.join(FLAGS.log_dir, 'model.ckpt'), 0)


def main(_):
  if tf.gfile.Exists(FLAGS.log_dir):
    tf.gfile.DeleteRecursively(FLAGS.log_dir)
  tf.gfile.MakeDirs(FLAGS.log_dir)

  embedding = build_embedding_matrix(FLAGS.embedding_file, FLAGS.vocab_file)
  build_and_run_graph(embedding)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--embedding_file', type=str, default='./GoogleNews-vectors-negative300.bin',
                      help='Path to the google embedding file')
  parser.add_argument('--vocab_file', type=str, default='./vocab.tsv',
                      help='Path to CLEVR vocab file')
  parser.add_argument('--log_dir', type=str, default='logs/',
                      help='Summaries log directory')
  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
