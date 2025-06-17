from flask import Flask, render_template, request, redirect, url_for, session
import os
from PIL import Image

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session use
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024  # 200MB


UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'photos' not in request.files:
        return "No file part"

    session['uploaded_photos'] = []

    allowed_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.mp4', '.mov', '.avi', '.webm'}
    files = request.files.getlist('photos')
    for file in files:
        if file.filename != '':
            filename = file.filename
            ext = os.path.splitext(filename)[1].lower()

            if ext not in allowed_extensions:
                continue  # Skip unsupported

            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)

            if ext in {'.jpg', '.jpeg', '.png', '.gif', '.webp'}:
                # Convert unsupported image types to jpg
                try:
                    im = Image.open(save_path)
                    im.verify()
                except Exception as e:
                    print("Image failed to verify:", e)

            session['uploaded_photos'].append(filename)

    return redirect(url_for('gallery'))

@app.route('/gallery')
def gallery():
    photo_filenames = session.get('uploaded_photos', [])
    photo_paths = [url_for('static', filename=f'uploads/{name}') for name in photo_filenames]
    session.pop('uploaded_photos', None)
    return render_template('gallery.html', photos=photo_paths)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
