import argparse
import pickle
import numpy as np
import models
import rouge
from keras.preprocessing.text import text_to_word_sequence


parser = argparse.ArgumentParser()
parser.add_argument("--data_path",
                    default="/home/ubuntu/word_model/data/preprocessed/test_embeddings.npz")
parser.add_argument("--raw_text",
                    default="/home/ubuntu/word_model/data/raw/test.pickle")
parser.add_argument("--val_raw",
                    default="/home/ubuntu/word_model/data/raw/val.pickle")
parser.add_argument("--val_path",
                    default="/home/ubuntu/word_model/data/preprocessed/val_embeddings.npz")
parser.add_argument("--weights", default="/home/ubuntu/word_model/models/weights2.h5")
args = parser.parse_args()

def main():
    with np.load(args.data_path) as data:
        y = data["arr_0"]
        X = data["arr_1"]

    model = models.build_model(units=128, weights=args.weights)
    preds = model.predict(X)
    binary_preds = 1 * (preds > 0.5)
    
    with open(args.raw_text, "rb") as f:
        data = pickle.load(f)
        X_text = data["X"]
        y_text = data["y"]
    print(X.shape, y.shape)
    print(len(X_text))
    print(len(y_text))
    X_tokens = [text_to_word_sequence(e) for e in X_text]
    y_tokens = [text_to_word_sequence(e) for e in y_text]

    print(len(X_tokens))

    all_preds = []
    all_gt = []
    for (j, document) in enumerate(X_tokens):
        predicted_words = [w for (i, w) in enumerate(document) if i < 500 and binary_preds[j, i, 0] != 0]
        all_preds.append(predicted_words)
        gt_words = [w for (i, w) in enumerate(document) if i < 500  and y[j, i] != 0]
        all_gt.append(gt_words)

    print(y[0, :10])

    print(all_gt[0][:10])
    print(y_tokens[0][:10])

    predicted_documents = [" ".join(e) for e in all_preds]
    gt_documents = [" ".join(e) for e in all_gt]

    #print(binary_preds)
    #print(all_preds[0])
    #print(all_gt[0])

    print(preds[1])
    print(binary_preds[1])
    #print(y_tokens[0])
    
    print("")
    
    print("pred doc 1")
    print(predicted_documents[0])
    print("ground truth doc 1")
    print(gt_documents[0])

    print("")
    
    print("pred doc 2")
    print(predicted_documents[1])
    print("ground truth doc 2")
    print(gt_documents[1])

    print("")
    
    print("pred doc 3")
    print(predicted_documents[2])
    print("ground truth doc 3")
    print(gt_documents[2])
     
    evaluator = rouge.Rouge(metrics=["rouge-n", "rouge-l"], max_n=2)
    scores = evaluator.get_scores(gt_documents, predicted_documents)
    for metric, result in scores.items():
        print(metric, result)


if __name__ == "__main__":
    main()
