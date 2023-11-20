import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Embedding, GlobalAveragePooling1D
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder


def chat(question, data, model, encoder, tokenizer, max_len):
    inp = question
    result = model.predict(
        keras.preprocessing.sequence.pad_sequences(
            tokenizer.texts_to_sequences([inp]), truncating="post", maxlen=max_len
        )
    )
    tag = encoder.inverse_transform([np.argmax(result)])
    for i in data:
        if i["tag"] == tag:
            responseChat = np.random.choice(i["responses"])
            print("ChatBot:", responseChat)
            return responseChat
