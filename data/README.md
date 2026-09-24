# Data

The project uses the public AG News dataset.

The actual CSV files are intentionally not committed to GitHub to keep the repository lightweight.

The notebook downloads the dataset with `requests` when required.

Expected local file after running the notebook:

```text
data/ag_news.csv
```

The dataset contains four news categories:

1. World
2. Sports
3. Business
4. Sci/Tech
