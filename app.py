from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# This route tells Flask to serve robots.txt and sitemap.xml from the root folder
@app.route('/<path:filename>')
def static_proxy(filename):
    if filename in ['robots.txt', 'sitemap.xml']:
        return send_from_directory(os.getcwd(), filename)
    return "File Not Found", 404

if __name__ == '__main__':
    app.run(debug=True)