from flask import Flask, render_template, request, send_file
import qrcode
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['data']
        img = qrcode.make(text)

        # Unique filename
        filename = f"qr_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        filepath = os.path.join("static", filename)
        img.save(filepath)

        return render_template('index.html', qr_code=filename)

    return render_template('index.html', qr_code=None)

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join("static", filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
