# Standard library imports
import os
import sys

# Third-party imports for data handling and analysis
import numpy as np

# TensorFlow and Keras for deep learning
import tensorflow as tf
from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential, Model, load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import lion_tf
from lion_tf import Lion



model_path = os.path.join(os.environ['MODEL_DIR'], os.environ['MODEL_NAME'])
test_path = os.environ['TEST_DIR']
#image_path = 'neuroflux_016_S_6708_MR_Axial_T2_Star__br_raw_20190404142958727_22_S812851_I1151023.jpg'

IMG_SIZE = (224, 224)


# Predict phase
def predict_phase(image_path):

    # Load the saved model with custom optimizer
    model = load_model(model_path, custom_objects={'Lion': Lion()})

    # Define the labels
    class_labels = ['EO', 'IO', 'IPTE', 'LO', 'PTE']
    IMG_SIZE = (224, 224)  

    # Load the image
    img = load_img(image_path, target_size=IMG_SIZE)

    # Convert the image to a numpy array
    img_array = img_to_array(img)

    # Rescale the image
    img_array = img_array / 255.0

    # Expand the dimensions to match the shape that the model expects
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    confidence = np.max(predictions[0]) * 100


    print(f"The MRI scan most likely belongs to {class_labels[predicted_class]} with a {confidence:.2f}% confidence.")


print('Argument List:', str(sys.argv))

if len(sys.argv) > 1 :
    image_path = os.path.join(test_path, str(sys.argv[1]))
    predict_phase(image_path)
else :
    print("Veillez renseignez le nom de l'image à tester")

