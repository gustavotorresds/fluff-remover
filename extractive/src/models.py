from  tensorflow import keras
from tensorflow.keras import layers, regularizers, optimizers, models, losses

def build_model(model_type="lstm",
                weights=None,
                units=128,
                input_shape=None,
                reg=0,
                learning_rate=0.001):

    if weights:
        return models.load_model(weights)
    else:
        regularizer = regularizers.l2(reg)
        model = keras.Sequential()
        model.add(layers.LSTM(units=units,
                              input_shape=input_shape,
                              return_sequences=True,
                              kernel_regularizer=regularizer,
                              recurrent_regularizer=regularizer))

        model.compile(optimizer=optimizers.Adam(learning_rate=learning_rate),
                      loss=losses.BinaryCrossentropy())
        return model
    
