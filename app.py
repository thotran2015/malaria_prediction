from flask import Flask, render_template, request
from werkzeug import secure_filename
from predict import predict_cell

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/upload')
def upload_file():
   return render_template('index.html')

	
@app.route('/uploader', methods = ['GET', 'POST'])
def save_file():
   if request.method == 'POST':
      f = request.files['file']
      #print(secure_filename(f.filename))
      
      #f.save('./static/'+secure_filename(f.filename))
      print('file uploaded succesfully')
      diagnosis = predict_cell(secure_filename(f.filename))
      img_path = "../static/"+ secure_filename(f.filename)
      return render_template('result.html', img_path = img_path, diagnosis = diagnosis)
		
if __name__ == '__main__':
   app.run(debug = True)
