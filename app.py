from flask import Flask, request, jsonify, render_template
from detc import detect_and_draw_box
import os
import base64

from IPython.display import Image, display
UPLOAD_FOLDER = 'C:\\Users\\dell\\Desktop\\Test_AI\\images\\'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__,static_url_path='', 
            static_folder='static',
            template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    image = request.files['file.jpg']
   
    filename=image.name
    
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))

    detect_and_draw_box(image.filename)
    
   
    
    return render_template('predict.html', code=image.filename )

if __name__ == "__main__":
    app.run(debug=True)
    
