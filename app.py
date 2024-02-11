# from flask import Flask, render_template, request
# from PyPDF2 import PdfReader
# from nltk.tokenize import sent_tokenize
# from nltk.corpus import stopwords
# from nltk.probability import FreqDist
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')


# app = Flask(__name__)

# def text_summary(text):
#     sentences = sent_tokenize(text)
#     words = [word for sent in sentences for word in sent.split() if word.lower() not in stopwords.words('english')]
#     freq_dist = FreqDist(words)
#     ranking = {}
#     for i, sent in enumerate(sentences):
#         for word in sent.split():
#             if word.lower() in freq_dist:
#                 if sent not in ranking:
#                     ranking[sent] = freq_dist[word.lower()]
#                 else:
#                     ranking[sent] += freq_dist[word.lower()]
#     summary_sentences = sorted(ranking, key=ranking.get, reverse=True)[:3]  # Extract top 3 sentences
#     summary = ' '.join(summary_sentences)
#     return summary

# def extract_text_from_pdf(file_path):
#     with open(file_path, "rb") as f:
#         reader = PdfReader(f)
#         page = reader.pages[0]
#         text = page.extract_text()
#     return text

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         if "text" in request.form:
#             input_text = request.form["text"]
#             result = text_summary(input_text)
#             return render_template("result.html", input_text=input_text, summary=result)
#         elif "file" in request.files:
#             input_file = request.files["file"]
#             file_path = "uploaded_file.pdf"
#             input_file.save(file_path)
#             extracted_text = extract_text_from_pdf(file_path)
#             summary = text_summary(extracted_text)
#             return render_template("result.html", input_text=extracted_text, summary=summary)
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import nltk

app = Flask(__name__)

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def text_summary(text):
    sentences = sent_tokenize(text)
    words = [word for sent in sentences for word in sent.split() if word.lower() not in stopwords.words('english')]
    freq_dist = FreqDist(words)
    ranking = {}
    for i, sent in enumerate(sentences):
        for word in sent.split():
            if word.lower() in freq_dist:
                if sent not in ranking:
                    ranking[sent] = freq_dist[word.lower()]
                else:
                    ranking[sent] += freq_dist[word.lower()]
    summary_sentences = sorted(ranking, key=ranking.get, reverse=True)[:3]  # Extract top 3 sentences
    summary = ' '.join(summary_sentences)
    return summary

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "text" in request.form:
            input_text = request.form["text"]
            result = text_summary(input_text)
            return render_template("result.html", input_text=input_text, summary=result)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
