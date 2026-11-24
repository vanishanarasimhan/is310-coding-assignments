# Exploring the Top 500 Novels

This folder contains my IS 310 Exploring and Visualizing Culture homework. I used the **Top 500 “Greatest” Novels** dataset from Responsible Datasets in Context to look at which original languages appear most often in a library-based list of novels.

## Files

- `novel_languages_eda.ipynb`: Pandas exploration and an Altair bar chart with hover tooltips.

## How to run

1. Open a terminal in this folder.
2. Install the packages (preferably in your own virtual environment):
   ```bash
   python3 -m pip install pandas altair notebook
   ```
3. Start Jupyter with `jupyter notebook`.
4. Open `novel_languages_eda.ipynb` and choose **Run All**.

The notebook downloads the CSV from the project's public GitHub repository when it runs, so an internet connection is needed. Do not commit virtual environment folders such as `.venv`.

## Data source

Anna Preus and Aashna Sheth, [Top 500 “Greatest” Novels](https://www.responsible-datasets-in-context.com/posts/top-500-novels/top-500-novels.html), Responsible Datasets in Context. The dataset is shared under CC BY 4.0.

CSV used: https://raw.githubusercontent.com/melaniewalsh/responsible-datasets-in-context/refs/heads/main/datasets/top-500-novels/top-500-novels-metadata_2025-01-11.csv
