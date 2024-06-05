from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from sklearn.preprocessing import LabelEncoder
import json
import numpy as np

app = Flask(__name__)

# Load the trained model
model = load_model('my_model_NLP.h5')

# Load tokenizer from JSON
with open('tokenizer.json', 'r') as f:
    tokenizer_json = f.read()
tokenizer = tokenizer_from_json(tokenizer_json)

# Load label encoder from JSON
with open('label_encoder.json', 'r') as f:
    label_encoder_json = f.read()
label_encoder = LabelEncoder()
label_encoder.classes_ = np.array(json.loads(label_encoder_json))

max_sequence_length = 40

# Initialize chat history
chat_history = []

# Define a function to predict intents
def predict_intent(text):
    tokenized_text = tokenizer.texts_to_sequences([text])
    padded_text = pad_sequences(tokenized_text, maxlen=max_sequence_length)
    predictions = model.predict(padded_text)
    predicted_index = np.argmax(predictions)
    predicted_label = label_encoder.inverse_transform([predicted_index])[0]
    return predicted_label

@app.route('/', methods=['GET', 'POST'])
def home():
    global chat_history
    
    if request.method == 'POST':
        user_input = request.form['user_input']
        
        # Append user input to chat history
        chat_history.append("You: " + user_input)
        
        # Get response from chatbot
        chatbot_response = predict_intent(user_input)
        
        # Append chatbot response to chat history
        chat_history.append("Chatbot: " + chatbot_response)
        
        return render_template('index.html', chat_history=chat_history)
    
    return render_template('index.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)
