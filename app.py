from flask import Flask, render_template, request,jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Crislator.html')

@app.route('/translate', methods=['POST'])
def translate():

    data = request.get_json()
    texto_a_traducir = data['text']
    traduccion = GoogleTranslator(source='es', target="en"). translate(texto_a_traducir)
    return jsonify({'translatedText' : traduccion})

if __name__ =='__main__':
    app.run(debug=True)