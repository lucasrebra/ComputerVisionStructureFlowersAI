# Flower Classification Pipeline

## Project Overview

This repository contains a simple pipeline for classifying flower images.  It
includes utilities for downloading data from Google Drive, performing basic data
cleaning, training a convolutional neural network and evaluating the result.  It
is meant as a starting point for experimenting with computer vision workflows and
can be adapted to custom datasets by changing a few paths in the configuration
file.

## Requirements

- Python `>=3.6`
- `torch==1.10.0`
- `torchvision==0.11.1`
- `tensorflow==2.7.0`
- `scikit-learn==0.24.2`
- `pandas==1.3.3`
- `numpy==1.21.2`
- `matplotlib==3.4.3`
- `umap-learn==0.5.2`
- `hdbscan==0.8.28`

## Setup

Clone this repository and change into its directory:

```bash
git clone <repo-url>
cd ComputerVisionStructureFlowersAI
```

Create a virtual environment and install the requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

You can optionally install the package in editable mode:

```bash
pip install -e .
```

## Configuration

All dataset locations and the model save path are defined in
`prediction_model/config/config.py`.  Edit the following entries to match your
environment:

- `DATA_LOADING_CONFIG`: Google Drive folder id and the destination directory
  for raw images.
- `DATA_CLEANING_CONFIG`: location of raw data and where the processed dataset
  should be written.
- `TRAINING_CONFIG['model_save_path']`: path where the trained model will be
  stored.
- `EVALUATION_CONFIG['test_data_path']`: directory containing test images.

## Training

Run the full pipeline, which downloads data (if configured), cleans it, trains
the network and finally evaluates the results:

```bash
python -m prediction_model.training_pipeline
```

## Evaluating a Saved Model

To evaluate a model stored at the path specified in `config.py` using the test
dataset defined in `EVALUATION_CONFIG`:

```bash
python -m prediction_model.evaluation.evaluate_model
```

## Single Image Prediction

Edit `prediction_model/predict.py` to point `image_path` to your test image and
then run:

```bash
python prediction_model/predict.py
```

## Repository Structure

- `prediction_model/` – package with datasets utilities, model definitions,
  training pipeline and configuration.
- `tests/` – unit tests for the data and training modules (currently need work).
- `requirements.txt` – Python dependencies.
- `setup.py` – packaging metadata.

## Limitations

The project is a work in progress. Some tests fail due to missing dependencies
and several modules are incomplete. Paths in `config.py` must be updated before
running the pipeline.

## Contributions

Contributions are welcome and appreciated. If you have suggestions to improve this package or have found an error, please consider the following:

- Open an issue to discuss proposed changes or report an error.
- For direct changes, please fork the repository, make your changes, and send a pull request for review.

Before submitting a pull request, make sure your code follows the conventions established in the project and passes all existing tests. Additionally, consider adding tests for new features or fixes.

## Contact

For additional questions or inquiries about this project, please don't hesitate to contact me:

- **Name**: Lucas Rey Braga
- **Email**: lucasrebra
- **GitHub**: [lucasrebra](https://github.com/lucasrebra)

We appreciate your interest in this project and look forward to your contributions and feedback.
