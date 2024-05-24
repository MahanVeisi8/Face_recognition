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

<table>
  <tr>
    <td><img src="asset/celeb_sample_img/Ali_daei/1.jpg" alt="Ali Daei" width="100"><br>0: Ali Daei</td>
    <td><img src="asset/celeb_sample_img/Alireza_beiranvand/1.jpg" alt="Alireza Beiranvand" width="100"><br>1: Alireza Beiranvand</td>
    <td><img src="asset/celeb_sample_img/Bahram_radan/1.jpg" alt="Bahram Radan" width="100"><br>2: Bahram Radan</td>
  </tr>
  <tr>
    <td><img src="asset/celeb_sample_img/Ebi/1.jpg" alt="Ebi" width="100"><br>3: Ebi</td>
    <td><img src="asset/celeb_sample_img/Golshifteh_farahani/1.jpg" alt="Golshifteh Farahani" width="100"><br>4: Golshifteh Farahani</td>
    <td><img src="asset/celeb_sample_img/Hayedeh/1.jpg" alt="Hayedeh" width="100"><br>5: Hayedeh</td>
  </tr>
  <tr>
    <td><img src="asset/celeb_sample_img/Homayoon_shajarian/1.jpg" alt="Homayoon Shajarian" width="100"><br>6: Homayoon Shajarian</td>
    <td><img src="asset/celeb_sample_img/Javad_razavian/1.jpg" alt="Javad Razavian" width="100"><br>7: Javad Razavian</td>
    <td><img src="asset/celeb_sample_img/Mehran_ghafourian/1.jpg" alt="Mehran Ghafourian" width="100"><br>8: Mehran Ghafourian</td>
  </tr>
  <tr>
    <td><img src="asset/celeb_sample_img/Mehran_modiri/1.jpg" alt="Mehran Modiri" width="100"><br>9: Mehran Modiri</td>
    <td><img src="asset/celeb_sample_img/Mohamad_esfehani/1.jpg" alt="Mohamad Esfehani" width="100"><br>10: Mohamad Esfehani</td>
    <td><img src="asset/celeb_sample_img/Reza_attaran/1.jpg" alt="Reza Attaran" width="100"><br>11: Reza Attaran</td>
  </tr>
  <tr>
    <td><img src="asset/celeb_sample_img/Sahar_dolatshahi/1.jpg" alt="Sahar Dolatshahi" width="100"><br>12: Sahar Dolatshahi</td>
    <td><img src="asset/celeb_sample_img/Seyed_jalal_hosseini/1.jpg" alt="Seyed Jalal Hosseini" width="100"><br>13: Seyed Jalal Hosseini</td>
    <td><img src="asset/celeb_sample_img/Taraneh_alidoosti/1.jpg" alt="Taraneh Alidoosti" width="100"><br>14: Taraneh Alidoosti</td>
  </tr>
  <tr>
    <td><img src="asset/celeb_sample_img/Googoosh/1.jpg" alt="Googoosh" width="100"><br>15: Googoosh</td>
    <td><img src="asset/celeb_sample_img/Mohsen_chavoshi/1.jpg" alt="Mohsen Chavoshi" width="100"><br>16: Mohsen Chavoshi</td>
    <td><img src="asset/celeb_sample_img/Mahan_veisi/1.jpg" alt="Mahan Veisi" width="100"><br>17: Mahan Veisi</td>
  </tr>
</table>

Each class has been accurately predicted by the ensemble model, with an overview of each class provided in the application.


![Sample Classification](static/path_to_sample_image.png)

Each class has been accurately predicted by the ensemble model, with an overview of each class provided in the application.

## Application Performance

After launching the application, you can upload images for classification. Here’s a demonstration of the application's performance:

![App Performance](static/path_to_application_gif.gif)

## Conclusion

This project showcases the integration of machine learning models into a web application, demonstrating practical deployment and interaction with a user interface. For further improvements, consider expanding the dataset, refining the model with more advanced techniques, or optimizing the web application for production environments.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
