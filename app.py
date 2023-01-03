from flask import Flask, request, render_template
import os
# from flask_bootstrap import Bootstrap
FOLDERS = os.path.join('static', 'imgs')
app= Flask(__name__)
# Bootstrap(app)

app.config['UPLOAD_FOLDER'] =  FOLDERS

@app.route('/')
@app.route('/home/')
def main():
    filename = os.path.join(app.config['UPLOAD_FOLDER'])
    return render_template("index.html")
@app.route('/')
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/')
@app.route('/services/')
def services():
    return render_template('services.html')

@app.route('/')
@app.route('/pricing/')
def pricing():
    return render_template('pricing.html')

@app.route('/')
@app.route('/contact/')
def contact():
    return render_template('contact.html')



if __name__=='__main__':
    app.run()