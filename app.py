from pathlib import Path

from flask import Flask, render_template, request
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

app = Flask(__name__)

MODEL_DIR = Path(__file__).parent / "models" / "bert_agnews"
LABELS = ["World", "Sports", "Business", "Sci/Tech"]

tokenizer = None
model = None
load_error = None

if MODEL_DIR.exists():
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
        model.eval()
    except Exception as exc:
        load_error = str(exc)
else:
    load_error = (
        "The trained model is not available yet. "
        "Run notebooks/01_bert_text_classification.ipynb first."
    )


def predict_topic(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=64,
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probabilities = torch.softmax(outputs.logits, dim=1)[0]
    predicted_id = int(torch.argmax(probabilities).item())

    return LABELS[predicted_id], float(probabilities[predicted_id])


@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    prediction = None
    confidence = None
    error = load_error

    if request.method == "POST":
        text = request.form.get("text", "").strip()

        if not text:
            error = "Please enter a headline or short news article."
        elif model is None:
            error = load_error
        else:
            prediction, confidence = predict_topic(text)

    return render_template(
        "index.html",
        text=text,
        prediction=prediction,
        confidence=confidence,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)
