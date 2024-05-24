import os
import numpy as np
from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Initialize Flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load pre-trained model
model_path = 'model/ensemblev9'  # Adjust the path accordingly
model = load_model(model_path)

# Define class labels
class_labels = {
    0: 'Ali_Daei',
    1: 'Alireza_Beiranvand',
    2: 'Bahram_Radan',
    3: 'Ebi',
    4: 'Golshifteh_Farahani',
    5: 'Hayedeh',
    6: 'Homayoon_Shajarian',
    7: 'Javad_Razavian',
    8: 'Mehran_Ghafoorian',
    9: 'Mehran_Modiri',
    10: 'Mohamad_Esfehani',
    11: 'Reza_Attaran',
    12: 'Sahar_Dolatshahi',
    13: 'Seyed_Jalal_Hosseini',
    14: 'Taraneh_Alidoosti',
    15: 'Googoosh',
    16: 'Mohsen_Chavoshi',
    17: 'Mahan_Veisi'
}

def preprocess_image(img_path, target_size=(224, 224)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0 
    return img_array

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for image upload and classification
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        img_array = preprocess_image(filename)
        predictions = model.predict(img_array)
        predicted_class = class_labels[np.argmax(predictions)]
         # Provide a URL path for the image
        image_url = url_for('static', filename='uploads/' + file.filename)
        
        return render_template('index.html', prediction=predicted_class, image_url=image_url)
if __name__ == '__main__':
    app.run(debug=True)