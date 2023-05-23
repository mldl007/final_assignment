from flask import Flask, render_template, request
from flask_cors import cross_origin, CORS
import spacy
import os
from utils.text_summarizer import summarize_text


app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)


@app.route("/")
@cross_origin()
def index():
    """
    displays the index.html page
    """
    return render_template("index.html")


@app.route("/", methods=["POST"])
@cross_origin()
def text_summarization():
    try:
        text = request.form["text_input"]
        nlp = spacy.load(os.path.join(".", "en_core_web_sm-3.4.1"))
        doc = nlp(text)
        n_sents = 0
        for d in doc.sents:
            n_sents += 1
        if n_sents < 3:
            text = ""
            result = '<p style="color: red;">Input should at least have 3 sentences</p>'
        else:
            result = summarize_text(text, nlp, factor=1.2)
            if len(result) == 0:
                result = summarize_text(text, nlp, factor=1)
            if len(result) == 0:
                result = summarize_text(text, nlp, factor=0.8)
            result = f'<h3>Summary</h3><p style="color: black;">{result}</p>'
    except Exception as e:
        result = f'Error: {e}'
    return render_template("index.html", result=result, input=text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
