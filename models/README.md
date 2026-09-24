# Models

The trained model is intentionally not committed because model weights can make a Git repository unnecessarily large.

After running the notebook, the fine-tuned model will be saved here:

```text
models/bert_agnews/
```

The folder will contain the tokenizer files and PyTorch model weights required by `app.py`.

Base checkpoint:

```text
google/bert_uncased_L-2_H-128_A-2
```

This compact BERT checkpoint is selected for CPU-friendly experimentation.
