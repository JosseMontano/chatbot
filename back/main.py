""" LIBRARIES FLASK """
from flask import Flask, jsonify
from controllers.chat import chat
from flask_cors import CORS

""" LIBRARIES MODEL """
import json
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Embedding,GlobalAveragePooling1D
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

""" CONFIG BASIC FLASK """
app = Flask(__name__)
CORS(app, resources={
     "*": {"origins": ["http://localhost:5173", "exp://192.168.1.13:19000"]}})


""" GET FILE DATA """
with open('./data/intents.json') as file:
    data = json.load(file)


""" GET THE DATA """
training_sentences = [] #TRAINING DATA
training_labels = [] #DESTINE LABELS TO EACH TRAINING DATA
labels = []
responses = []
for intent in data['intents']:
    for patterns in intent['patterns']:
        training_sentences.append(patterns)
        training_labels.append(intent['tag'])
    responses.append(intent['responses'])
        
    if intent['tag'] not in labels: #if there ain't th tag, just add it
        labels.append(intent['tag'])


""" 
"LabelEncoder()" PROVIDED POR SCIKIT LEARN TO CONVERT TRAINGING LABELS IN A FORMAT THAT 
THE MODEL WILL UNDERSTAND
 """           
encoder= LabelEncoder()
encoder.fit(training_labels)
training_labels = encoder.transform(training_labels)



""" 
Tokenizer: allow limit the zise of us vocabulary to a determined number
OOV: Try the tokens that don't exist in the vocabulary in the moment of the inference
pad sequences: is used to make all the training text sequences into the same size..
 """


vocab_size = 1000
embedding_dim = 16
max_len = 20
oov_token = "<OOV>"

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(training_sentences)
padded_sequences = pad_sequences(sequences, truncating='post', maxlen=max_len)





""" 
Sequential: model class of keras to define the neuronal Network architecture
"""

num_classes = len(labels)
model = Sequential()
model.add(Embedding(vocab_size, embedding_dim, input_length=max_len))
model.add(GlobalAveragePooling1D())
model.add(Dense(16, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', 
                optimizer='adam', metrics=['accuracy'])

model.summary()

""" TRAINING THE MODEL """
epochs = 500
history = model.fit(padded_sequences, np.array(training_labels), epochs=epochs)




@app.route('/')
def hello_world():
    return 'Hello, from flask!'

@app.route('/api/chat/<string:question>', methods=['GET'])
def ChatBot(question):
    resFunction = chat(question, data, model, encoder, tokenizer, max_len)
    msg = resFunction
    return jsonify({"message": msg})


if __name__ == '__main__':
    app.run(debug=True)