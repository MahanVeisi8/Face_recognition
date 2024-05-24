# Celebrity Face Recognition Using TensorFlow and Keras

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1egf7l4c_riqb2pxKrEM3nz9kksP3ljyB?usp=sharing)
![Python](https://img.shields.io/badge/Python-3.8-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.4-brightgreen)
![Keras](https://img.shields.io/badge/Keras-2.4.3-red)
![Status](https://img.shields.io/badge/status-active-green)

This repository hosts a Jupyter Notebook that documents the end-to-end process of building a celebrity face recognition model. The project utilizes TensorFlow and Keras for building an ensemble of convolutional neural networks (CNNs) to classify images into distinct **iranian** celebrity categories based on their facial features.

## Table of Contents
- [Project Overview](#project-overview)
- [Setup Instructions](#setup-instructions)
- [Notebook Details](#notebook-details)
  - [Data Preprocessing](#data-preprocessing)
  - [Model Training](#model-training)
  - [Evaluation and Analysis](#evaluation-and-analysis)
- [Results](#results)
- [Contributing](#contributing)

## Project Overview

The notebook includes detailed steps for data handling, preprocessing, model training, and evaluation. It covers the following key aspects:
- Setting up the environment and importing necessary libraries.
- Loading and preprocessing image data.
- Splitting data into training, validation, and test sets.
- Data augmentation to enhance model robustness.
- Building and training an ensemble model using architectures like MobileNetV2 and InceptionV3.
- Evaluating model performance and analyzing misclassifications.

## Setup

**Running the Notebook in Google Colab**
- The notebook is designed for easy execution in Google Colab, requiring no additional setup other than a Google account and internet access.😊
  
The code is designed to run in a Python environment with essential machine learning and simulation libraries. You can execute the notebook directly in Google Colab using the badge link provided, which includes a pre-configured environment with all necessary dependencies.



# Data Preprocessing

Data preprocessing is a crucial first step in any machine learning workflow, ensuring that the data fed into the model is clean, appropriately formatted, and enhanced to improve model performance. This project involves several preprocessing steps, from initial data loading and visualization to more complex manipulations like augmentation and normalization.


## Data Loading and Image Resizing

This step involves loading the images from structured directories named after each celebrity, resizing them to uniform dimensions (224x224 pixels), and labeling them based on their directory names to facilitate their use in training a convolutional neural network.

- ![Data Loading and Resizing](asset/first_data.png)

## Visualizing the Data

To ensure that images are correctly loaded and to understand the dataset's composition, a sample of images is displayed. This helps verify the integrity of the image loading and resizing process.

```python
# Display a grid of sample images
fig, axes = plt.subplots(7, 6, figsize=(18, 21))
# Display code
```

**Image Placeholder:**
- ![Sample Images Grid](path/to/sample_images_grid.png)

## Data Augmentation

To enhance model robustness and prevent overfitting, the training images are augmented using a variety of transformations, such as rotations, shifts, shearing, flipping, and brightness adjustments. These transformations simulate different lighting conditions, orientations, and partial occlusions the model might encounter in practical scenarios.

```python
# Setup ImageDataGenerator for augmentation
datagen = ImageDataGenerator(rotation_range=90, width_shift_range=0.1, ...)
```

**Image Placeholder:**
- ![Data Augmentation](path/to/data_augmentation.png)

## Splitting the Data

The images are split into training, validation, and test sets. This is essential for training the model effectively and evaluating its performance on unseen data. Stratified sampling is used to maintain the distribution of classes across these sets.

```python
# Splitting the data into training, validation, and test sets
X_train, X_val, X_test, y_train, y_val, y_test = train_test_split(...)
```

**Image Placeholder:**
- ![Data Split and Distribution](path/to/data_split_distribution.png)




## Model Training

The project utilizes a combination of different CNN architectures, leveraging pretrained models like MobileNetV2 for feature extraction and custom layers for classification. The training process is detailed with strategies for handling overfitting, such as early stopping and dropout layers.

## Evaluation and Analysis

After training, the model is evaluated on a held-out test set. The performance metrics such as accuracy and loss are plotted over epochs. The notebook also includes a section for visualizing incorrect predictions to analyze the model's weaknesses and potential biases.

## Results

The notebook provides graphs and metrics that demonstrate the model's performance. For instance:
- Training and validation accuracy/loss graphs.
- Test set accuracy.
- Examples of correct and incorrect predictions.

## Contributing

Contributions to this project are welcome! Please feel free to fork the repository, make your changes, and submit a pull request. You can also open issues for bugs you've noticed or features you think would make a valuable addition to the project.


