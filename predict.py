#import pickle
#from keras.models import Model
from keras.models import model_from_json
#from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import numpy as np
import tensorflow as tf
from keras import backend as K

NUM_EPOCHS = 50
INIT_LR = 1e-1
BS = 64

#def predict_cell(img_path, loaded_model):
#    cell = image.load_img(img_path, target_size = (64,64))
#t = np.array([image.img_to_array(cell)/255.0])
#if np.argmax(loaded_model.predict(t), axis = -1) == 0:
#        print('cell is bad')
#        K.clear_session()
#        return "Cell is parasitized"
#    else:
#        K.clear_session()
#        return "Cell is uninfected"
    

##def transform_img(img):
##    # initialize the validation (and testing) data augmentation object
##    valAug = ImageDataGenerator(rescale=1 / 255.0)
##    testGen = valAug.flow_from_directory(
##	'img',
##	class_mode="categorical",
##	target_size=(64, 64),
##	color_mode="rgb",
##	shuffle=False,
##	batch_size=BS)
##    return testGen

def load_model():
    # load json and create model
    json_file = open('resnet_architecture.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    #load weights into new model
    loaded_model.load_weights("resnet_weights.h5")
    return loaded_model
    

def predict_cell(loaded_model, file_path):
    cell = image.load_img(file_path, target_size = (64,64))
    #cell = image.load_img('./static/output.png', target_size = (64,64))
    matrix = np.array([image.img_to_array(cell)/255.0])
    if np.argmax(loaded_model.predict(matrix), axis = -1) == 0:
        return "Cell is parasitized"
    else:
        return "Cell is uninfected"





