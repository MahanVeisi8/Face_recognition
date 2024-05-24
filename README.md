# Face Recognition Project

This repository contains the source code for a celebrity face recognition system built with Flask and TensorFlow. It leverages a pre-trained ensemble model to classify images into predefined categories of Iranian celebrities. The project demonstrates how to build, train, and deploy a machine learning model for a practical application.

## Project Structure

- `preprocess and train`: Contains the Jupyter Notebook for preprocessing the data and training the ensemble model.
- `static`: Stores static files like CSS, images for the web app.
- `templates`: Holds HTML templates for rendering the web application.
- `test`: Includes test scripts or data for the application.
- `app.py`: The main Flask application file for running the web server.

## Quick Start

1. **Set Up Environment**:
   Ensure Python 3.8 and pip are installed. Install the required libraries:
   ```bash
   pip install flask tensorflow
   ```

2. **Run the Application**:
   Execute the Flask application by running:
   ```bash
   python app.py
   ```

3. **Access the Web Interface**:
   Open a web browser and go to `http://localhost:5000` to view the application.

## Model Training and Evaluation

For details on data preprocessing, model training, and evaluation, refer to the [`preprocess and train`](preprocess_and_train/README.md) directory. This section provides comprehensive instructions on preparing the dataset, training the ensemble model, and evaluating its performance with detailed accuracy metrics.

## Sample Classifications

The system can recognize the following celebrities:

- Ali Daei
- Alireza Beiranvand
- Bahram Radan
- ... (and other listed celebrities)

![Sample Classification](static/path_to_sample_image.png)

Each class has been accurately predicted by the ensemble model, with an overview of each class provided in the application.

## Application Performance

After launching the application, you can upload images for classification. Here’s a demonstration of the application's performance:

![App Performance](static/path_to_application_gif.gif)

## Conclusion

This project showcases the integration of machine learning models into a web application, demonstrating practical deployment and interaction with a user interface. For further improvements, consider expanding the dataset, refining the model with more advanced techniques, or optimizing the web application for production environments.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
