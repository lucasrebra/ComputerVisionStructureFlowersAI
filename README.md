# Prediction Model Package

## Description

This package enables the cleaning, training, and evaluation of image classification models, specialized in flower detection. It was designed to facilitate the process from data loading to obtaining a trained and evaluated model.

## Installation

To install the package, follow these steps:

```bash
git clone https://your-repository.git
cd prediction_model
pip install .
```

## Usage

The package can be used in the following way to train a model with your image data. Make sure your data is organized and the parameters in `config.py` are correctly set.

```python
from prediction_model.training_pipeline import run_training_pipeline

# Run the complete training pipeline
run_training_pipeline()
```

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
