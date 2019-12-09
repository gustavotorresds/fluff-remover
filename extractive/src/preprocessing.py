import os
import argparse
import re
import pickle
import numpy as np
from gensim.models import KeyedVectors
import string
from keras.preprocessing.text import Tokenizer, text_to_word_sequence
from keras.preprocessing.sequence import pad_sequences
from nltk.tokenize import sent_tokenize


parser = argparse.ArgumentParser()
parser.add_argument("--train_path", 
        default="../data/raw/train.pickle")
parser.add_argument("--val_path",
        default="../data/raw/val.pickle")
parser.add_argument("--test_path",
        default="../data/raw/test.pickle")
args = parser.parse_args()

def load_train_data(train_path):
        assert os.path.exists(train_path)
        with open(train_path, "rb") as f:
                data = pickle.load(f)
                X = data["X"]
                y = data["y"]
        return X,y

def X_y_data_to_pairs(X, y):
        num_pairs = len(X)
        list_of_Xy_pairs = []

        for i in range(num_pairs):
                pair = (X[i], y[i])
                list_of_Xy_pairs.append(pair)
        return list_of_Xy_pairs

def tokenize(content_string):
        token_list = []
        punctuation = [".", "!", ",", "?", '"', "'"]

        for i in range(len(punctuation)):
                content_string = content_string.replace(punctuation[i], " " + punctuation[i] + " ")

        for token in content_string.split():
                token_list.append(token)

        return token_list

def compute_labels(fluffed, concise, max_num_words):
        labels = np.zeros((max_num_words,))
        i_fluffed = 0
        i_concise = 0

        while i_fluffed < len(fluffed) and i_concise < len(concise):
                if i_fluffed >= max_num_words:
                        break
                if fluffed[i_fluffed] == concise[i_concise]:
                        labels[i_fluffed] = 1
                        i_fluffed += 1
                        i_concise += 1
                else:
                        labels[i_fluffed] = 0
                        i_fluffed +=1
        

        return labels

def embed_words(X, word2vec_limit = 50000, NUM_WORDS=20000, max_num_words=500):
        model = KeyedVectors.load_word2vec_format("/home/ubuntu/word_model/GoogleNews-vectors-negative300.bin", binary=True)
        word_vectors = model.wv
        # embedded_words = np.zeros((max_num_words, 300))
        # tokenizer = Tokenizer(num_words=NUM_WORDS,filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n\'',lower=True)

       # print(len(X))
        embedded_documents = []
        for document in X:
                document_embedding = np.zeros((max_num_words, 300))
                for i, word in enumerate(document):
                        if i >= max_num_words:
                                break
                        if word in word_vectors.vocab:
                                document_embedding[i] = model[word]
                        else:
                                document_embedding[i] = np.random.uniform(
                                        -0.25, 0.25, word_vectors.vector_size)
                embedded_documents.append(document_embedding)

        """for i in range(len(X)):
                tokenizer.fit_on_texts(X[i])
                sequences = tokenizer.texts_to_sequences(X[i])
                for j, word in enumerate(tokenizer.word_index.items()):
                        if word in word_vectors.vocab:
                                v = model[word]
                        else:
                                v = np.random.uniform(-0.25, 0.25, word_vectors.vector_size)
                        # v  = model[word] if word in word_vectors.vocab else np.random.uniform(-0.25, 0.25, word_vectors.vector_size)
                        embedded_words[j] = v"""
                
                
               # vectors = [ for word in tokenizer.word_index.items()]
               # embedding_weights_vectors.append(vectors)
        #v = [np.array(e).transpose() for e in embedding_weights_vectors]
        # print(len(embedding_weights_vectors))
        # print(embedding_weights_vector[0].shape)
        #padded_embedded_vectors = pad_sequences(v)
        #padded_embedded_vectors = padded_embedded_vectors.transpose((0, 2, 1))
        return np.array(embedded_documents)
        

        #tokenizer = Tokenizer(num_words=NUM_WORDS,filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n\'',lower=True)
        #for i in range(len(X))                #tokenizer.fit_on_texts(X[i])
                #sequences = tokenizer.texts_to_sequences(X[i])
                #padded_sequences = pad_sequences(sequences)
                #vectors = [model[word] if word in word_vectors.vocab else np.random.uniform(-0.25, 0.25, word_vectors.vector_size) for word in X[i].split()]
                
                
        
        list_of_embeddings = []

        for i in range(len(X_tokens)):
                vectors = [model[word] for word in X_tokens[i]]

def process_split(split, data_path):
        X, y = load_train_data(data_path)
        """X_sentences = []
        for x in X:
                X_sentences += x.split(".")  # sent_tokenize(x)
        y_sentences = []
        for y_current in y:
                y_sentences += y_current.split(".")  # sent_tokenize(y_current)"""

        X_tokens = [text_to_word_sequence(e) for e in X]
        y_tokens = [text_to_word_sequence(e) for e in y]

        max_num_words = 500
        fluffed_labels = np.array(
                [compute_labels(x_c, y_c, max_num_words)
                 for x_c, y_c in zip(X_tokens, y_tokens)])
        embedded_words = embed_words(X_tokens, max_num_words)
        np.savez(
                "/home/ubuntu/word_model/data/preprocessed/{}_embeddings.npz".format(
                        split), fluffed_labels, embedded_words)


def main():
        process_split("train", args.train_path)
        process_split("val", args.val_path)
        process_split("test", args.test_path)

if __name__ == "__main__":
        main()
