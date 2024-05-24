# Celebrity Face Recognition Using TensorFlow and Keras

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1egf7l4c_riqb2pxKrEM3nz9kksP3ljyB?usp=sharing)
![Python](https://img.shields.io/badge/Python-3.8-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.4-brightgreen)
![Keras](https://img.shields.io/badge/Keras-2.4.3-red)
![Status](https://img.shields.io/badge/status-active-green)

This repository hosts a Jupyter Notebook that documents the end-to-end process of building a celebrity face recognition model. The project utilizes TensorFlow and Keras for building an ensemble of convolutional neural networks (CNNs) to classify images into distinct **iranian** celebrity categories based on their facial features.


## Setup

**Running the Notebook in Google Colab**
- The notebook is designed for easy execution in Google Colab, requiring no additional setup other than a Google account and internet access.😊
  
The code is designed to run in a Python environment with essential machine learning and simulation libraries. You can execute the notebook directly in Google Colab using the badge link provided, which includes a pre-configured environment with all necessary dependencies.


## Preprocessing

### Data Loading and Image Resizing

Images stored in directories named after each celebrity are loaded and resized to a uniform dimension of 224x224 pixels—ideal for CNN input. Each image is labeled based on its parent directory, aligning with the respective celebrity's name. This automated labeling facilitates straightforward training and validation:

### Visualizing the Data

To verify that images are correctly loaded and to understand the dataset's composition, we display a sample of the images. This visualization step checks the integrity of the image loading and resizing process and offers a quick glimpse into the data's variety and quality:

![Sample Images Visualization](asset/first_data.jpg)

### Data Augmentation

To enhance model robustness and mitigate overfitting, training images undergo augmentation. Transformations such as rotations, shifts, shearing, flipping, and brightness adjustments are applied. These augmentations help the model generalize better by simulating various real-world conditions:

```python
ImageDataGenerator(
    rotation_range=90,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.30,
    horizontal_flip=True,
    fill_mode='nearest',
    brightness_range=[0.8, 1.2]
)
```

![Data Augmentation](asset/augmentation.jpg)

### Splitting the Data

To ensure effective training and unbiased evaluation, the dataset is divided into training, validation, and test sets using stratified sampling. This method helps maintain an equal distribution of classes across each set, crucial for training unbiased and generalized models:

```python
X_train, X_temp, y_train, y_temp = train_test_split(images, labels, test_size=0.15, random_state=10, stratify=labels)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=10, stratify=y_temp)
```

The distribution of classes in each dataset part is visualized to confirm uniformity and appropriate representation:

<table>
  <tr>
    <td>Train Distribution<br><img src="asset/data_dist1.png" alt="Training Distribution" width="240px"></td>
    <td>Validation Distribution<br><img src="asset/data_dist2.png" alt="Validation Distribution" width="240px"></td>
    <td>Test Distribution<br><img src="asset/data_dist3.png" alt="Test Distribution" width="240px"></td>
  </tr>
</table>



### Data Normalization and Preparation

After partitioning the data, each image's pixel values are normalized to a range of 0 to 1 to facilitate efficient training. This normalization process aids in achieving faster convergence during model training. Furthermore, image labels are converted into one-hot encoded vectors to suit the model's categorical classification needs. These steps ensure the data is in the optimal format for feeding into our neural network, setting a strong foundation for robust model performance.

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


