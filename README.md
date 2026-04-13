# LSTM with Attention for Language Modeling

This project implements an LSTM-based language model with attention mechanism for text generation and language modeling tasks.

## Datasets

The project uses the following datasets:
- Penn Treebank (PTB) dataset
- WikiText-2 dataset
- Shakespeare text

## Features

- LSTM neural network with attention
- Support for multiple datasets
- Model training and inference
- Checkpoint saving and loading

## Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`

## Usage

### Training
Run the training script (assuming rnn.py contains the training logic):
```
python rnn.py
```

### Inference
Load the trained model from checkpoints and generate text.

## Files

- `rnn.py`: Main model implementation with LSTM and Attention
- `utils.py`: Utility functions for data loading and processing
- `checkpoints/`: Saved model checkpoints
- `data/`: Dataset files
- `logs/`: Training loss logs

## Configuration

Model hyperparameters can be adjusted in the `Config` class in `rnn.py`:

- `batch_size`: Batch size for training
- `embed_size`: Embedding dimension
- `hidden_size`: LSTM hidden state size
- `num_steps`: Sequence length for training
- `max_epochs`: Maximum training epochs
- `dropout`: Dropout rate
- `lr`: Learning rate
- `num_layers`: Number of LSTM layers


## Troubleshooting

- Ensure PyTorch is installed with CUDA support if using GPU
- Check that all dataset files are present in the `data/` directory
- If encountering import errors, verify the virtual environment is activated

## License


This project is for educational purposes.