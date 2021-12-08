"""
This is Finanal assignment: Python Web Application Creation and Deployment
"""
from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    ''' english_to_french endpoint '''
    text_to_translate = request.args.get('text_to_translate')
    # Write your code here
    french_text = translator.english_to_french(text_to_translate)
    # return "Translated text to French"
    return french_text

@app.route("/frenchToEnglish")
def french_to_english():
    ''' french_to_english endpoint '''
    text_to_translate = request.args.get('text_to_translate')
    # Write your code here
    english_text = translator.french_to_english(text_to_translate)
    # return "Translated text to English"
    return english_text

@app.route("/")
def render_index_page():
    ''' render page index.html ('/') '''
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
