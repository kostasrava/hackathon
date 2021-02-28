import os
from flask import Flask, render_template, request

# import our OCR function
from imageToTxt import KeyVerify

# define a folder to store and later serve the images
UPLOAD_FOLDER = '/uploads/'

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#home page
@app.route('/')
def home_page():
    return render_template('index.html')

#ID upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        file = request.files['file']
        keybool = KeyVerify(file)

        if keybool == True:
            return render_template('upload.html',
                                    msg='This is a valid ID',
                                    extracted_text=keybool,
                                    img_src=UPLOAD_FOLDER + file.filename)
        elif keybool == False:
            return render_template('upload.html',
                                    msg="This isn't a valid ID",
                                    extracted_text=keybool,
                                    img_src=UPLOAD_FOLDER + file.filename)

    elif request.method == 'GET':
        return render_template('upload.html')


if __name__ == '__main__':
    app.run()
