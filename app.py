from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# This gets the absolute path to the directory this file is in
base_dir = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def home():
    return render_template('index.html')

# SECURE ROUTE FOR ROBOTS AND SITEMAP
@app.route('/robots.txt')
def robots():
    return send_from_directory(base_dir, 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(base_dir, 'sitemap.xml')

if __name__ == '__main__':
    app.run()
