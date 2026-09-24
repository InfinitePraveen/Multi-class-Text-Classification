# Multi-class Text Classification with BERT

Fine-tune a lightweight BERT model on the open-source **AG News** dataset to classify news articles into four topics:

- World
- Sports
- Business
- Sci/Tech

The project is intentionally designed for a CPU-only computer with limited disk space. The notebook downloads the dataset with `requests` and uses `google/bert_uncased_L-2_H-128_A-2`, a small BERT model, instead of a full-size BERT checkpoint.

## Project Highlights

- BERT-based multi-class text classification
- HuggingFace Transformers
- AG News open-source dataset
- CPU-friendly training
- Small training subset for quick experimentation
- Notebook-first workflow
- Flask web application for an interview-ready demo
- GitHub and LinkedIn links included in the web app
- No `src/` folder
- No separate preprocessing/module scripts
- Dataset and trained model are downloaded/generated only when needed

## Repository Structure

```text
Multi-class-Text-Classification/
│
├── data/
│   └── README.md
│
├── models/
│   └── README.md
│
├── notebooks/
│   └── 01_bert_text_classification.ipynb
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── CHANGELOG.md
├── CONTRIBUTE.md
├── README.md
├── requirements.txt
└── .gitignore
```

## Dataset

The project uses the **AG News** dataset, a public four-class news topic dataset.

To keep the repository small, the CSV is not committed. The notebook downloads it automatically using `requests`.

## Model

The notebook uses:

`google/bert_uncased_L-2_H-128_A-2`

This is a compact BERT checkpoint suitable for CPU experimentation. It retains the BERT architecture while being much smaller than `bert-base-uncased`.

The default notebook configuration uses a small subset of AG News so it can be trained on a normal CPU without requiring a GPU.

## Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Open the notebook:

```bash
jupyter notebook
```

Run:

```text
notebooks/01_bert_text_classification.ipynb
```

The notebook will:

1. Download AG News.
2. Keep a small CPU-friendly subset.
3. Tokenize the news text with BERT.
4. Fine-tune the BERT classifier.
5. Evaluate accuracy and a classification report.
6. Save the tokenizer and model under `models/bert_agnews/`.
7. Test predictions on new headlines.

## Run the Flask Demo

After successfully running the notebook and creating the model:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Enter a news headline or short article and the application will predict:

- World
- Sports
- Business
- Sci/Tech

The web application is deliberately simple so the main focus remains on the machine-learning project.

## CPU / Low-Disk Notes

The notebook is configured for a small experiment rather than maximum benchmark accuracy.

You can reduce:

```python
TRAIN_SAMPLES = 800
TEST_SAMPLES = 200
```

if your computer is slow.

For a stronger experiment, increase them gradually after confirming that the notebook runs successfully.

The model checkpoint is downloaded by HuggingFace when first needed, so it does not have to be stored in the Git repository.

## Skills Demonstrated

- Natural Language Processing
- BERT
- HuggingFace Transformers
- Text classification
- Tokenization
- Fine-tuning
- Model evaluation
- Flask deployment
- CPU-friendly machine learning

## Profiles

**GitHub:** https://github.com/InfinitePraveen

**LinkedIn:** https://www.linkedin.com/in/infinitepraveen/

## Contribution

See [CONTRIBUTE.md](CONTRIBUTE.md).

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
