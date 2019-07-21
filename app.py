from flask import Flask, render_template, request
#from flask_uploads import UploadSet, configure_uploads,IMAGES
from werkzeug import secure_filename
from predict import predict_cell
from predict import load_model
import os
from keras.preprocessing import image
import numpy as np

UPLOAD_FOLDER = 'static'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#photos = UploadSet('photos', IMAGES)

#app.config['UPLOADED_PHOTOS_DEST'] = '.'
#configure_uploads(app, photos)

loaded_model = load_model()

@app.route('/')
@app.route('/index')
@app.route('/upload')
def upload_file():
   return render_template('index.html', diagnosis = 'Cell is Uninfected')

@app.route('/uploader', methods = ['GET', 'POST'])
def save_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      f.save(file_path)
      os.rename(file_path, './static/output.png')
      #f.save('./static/'+secure_filename(f.filename))
      cell = image.load_img('./static/output.png', target_size = (64,64))
      matrix = np.array([image.img_to_array(cell)/255.0])
      return loaded_model.summary()
   
#predict_cell('./static/'+secure_filename(f.filename), loaded_model)

##@app.route('/uploader', methods = ['GET', 'POST'])
##def save_file():
##   print('hi')
##   if request.method == 'POST':
##      f = request.files['file']
##      #print(secure_filename(f.filename))
##      
##      f.save('../static/'+secure_filename(f.filename))
##      print('file uploaded succesfully')
##      diagnosis = predict_cell(secure_filename(f.filename))
##      img_path = "../static/"+ secure_filename(f.filename)
##      return render_template('result.html', img_path = img_path, diagnosis = diagnosis)
		
if __name__ == '__main__':
   app.run(debug = True)
