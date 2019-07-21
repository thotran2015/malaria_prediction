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


def predict_cell(img_path):
    cell = image.load_img('../static/'+img_path, target_size = (64,64))

    # load json and create model
    json_file = open('resnet_architecture.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    #load weights into new model
    loaded_model.load_weights("resnet_weights.h5")
    #with open('model.pkl', 'rb') as handle:
 #       model = pickle.load(handle)
    #m = Model(inputs = loaded_model.input, outputs = loaded_model.output)
    #print( loaded_model.summary())
    t = np.array([image.img_to_array(cell)/255.0])
    #img_raw = tf.read_file('./img/'+img_path)
    #img_tensor = tf.image.decode_image(img_raw)
    #print(img_tensor.shape)
    #img_final = tf.image.resize(img_tensor, [64, 64])
    #img_final = img_final/255.0
        #return loaded_model.predict(t)
    if np.argmax(loaded_model.predict(t), axis = -1) == 0:
        print('cell is bad')
        K.clear_session()
        return "Cell is parasitized"
    else:
        K.clear_session()
        return "Cell is uninfected"
    

