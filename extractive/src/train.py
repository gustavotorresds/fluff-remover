import argparse
import numpy as np
import models

parser = argparse.ArgumentParser()
parser.add_argument("--train_path",
                    default="/home/ubuntu/word_model/data/preprocessed/train_embeddings.npz")
parser.add_argument("--val_path",
                     default="/home/ubuntu/word_model/data/preprocessed/val_embeddings.npz")
parser.add_argument("--learning_rate", default=0.001)
parser.add_argument("--model_type", default="lstm")
parser.add_argument("--weights", default=None)
# parser.add_argument("--input_shape", default=(None, 1000, 300))
parser.add_argument("--reg", default=0)
parser.add_argument("--batch_size", default=8)
parser.add_argument("--epochs", default=20)
parser.add_argument("--units", default=128) #try 128, 64, 32, 16, 8, 1
args = parser.parse_args()

input_shape = (500, 300)

def main():
    with np.load(args.train_path) as train_data:
        y_train = train_data["arr_0"]
        X_train = train_data["arr_1"]

    with np.load(args.val_path) as val_data:
        y_val = val_data["arr_0"]
        X_val = val_data["arr_1"]

    y_train = y_train[:, :, np.newaxis]
    print(y_train.shape)
    y_val = y_val[:, :, np.newaxis]
    print(y_train.shape)

    model = models.build_model(args.model_type, args.weights,input_shape, args.reg, args.learning_rate)
    try:
        model.fit(X_train, y_train, batch_size=args.batch_size, epochs=args.epochs, validation_data=(X_val, y_val))
    except KeyboardInterrupt:
        print("\nStopping training early, continuing to evaluation and model saving")

    print(model.evaluate(x=X_train, y=y_train))

    model.save("/home/ubuntu/word_model/models/weights2.h5")


if __name__ == "__main__":
    main()
