from flask import Flask, request, render_template
import os
import psycopg2
# from flask_bootstrap import Bootstrap
FOLDERS = os.path.join('static', 'imgs')
app= Flask(__name__)
# Bootstrap(app)


def get_db_connection():
    conn = psycopg2.connect(host='database-2.ciluhbuaflhg.us-west-2.rds.amazonaws.com',
                            database='flask',
                            user='postgres',
                            password='admin123')
    
    return conn

app.config['UPLOAD_FOLDER'] =  FOLDERS

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home/', methods=('GET', 'POST'))
def main():
    filename = os.path.join(app.config['UPLOAD_FOLDER'])
    if request.method == 'POST':
        name = request.form.get("name")
        companyName = request.form.get("cname")
        email = request.form.get('email')
        comments = request.form.get('comment')

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO bookdemo (Name, email, company_name, comment)'
                    'VALUES (%s, %s, %s, %s)',
                    (name, email, companyName, comments))
        conn.commit()
        cur.close()
        conn.close()
        # return render_template("index.html")
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
@app.route('/contact/', methods=('GET', 'POST'))
def contact():
    # filename = os.path.join(app.config['UPLOAD_FOLDER'])
    if request.method == 'POST':
        name = request.form.get("name")
        companyName = request.form.get("cname")
        email = request.form.get('email')
        comments = request.form.get('comment')

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO bookdemo (Name, email, company_name, comment)'
                    'VALUES (%s, %s, %s, %s)',
                    (name, email, companyName, comments))
        conn.commit()
        cur.close()
        conn.close()
    return render_template('contact.html')

@app.route('/')
@app.route('/careers/')
def careers():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM careers;')
    books = cur.fetchall()
    cur.close()
    conn.close()    
    
    return render_template('careers.html', books=books)



if __name__=='__main__':
    app.run()