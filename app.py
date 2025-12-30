from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(os.getcwd(), request.path[1:])

# This is important for Vercel
if __name__ == "__main__":
    app.run()
