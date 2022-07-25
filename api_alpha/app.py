# Name : Crud_API
# Version : Alpha
# Creation date : 18/07/2022
# Author : Gerhard Eibl
# INFO : This is the main code of the API with the crud system.
# ---------------------------------------- #


import psycopg2
from flask import Flask, render_template, request, url_for, redirect, session
from auth import auth as auth_blueprint

app = Flask(__name__)
app.register_blueprint(auth_blueprint)

app.config['SECRET_KEY'] = 'thisisasecret'


# The function to connect with the DB.
def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='api_alpha',
                            user="postgres",
                            password="rootroot")

    return conn


# The index page route + controller which select all the wines in the DB.
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    if 'loggedin' in session:
        cur.execute('SELECT * FROM vins;')
        vins = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('index.html', vins=vins)
    return redirect(url_for('auth.login'))


# The get or post method route + controller which add in the Table vins a new wine.
@app.route('/create/', methods=['GET', 'POST'])
def create():
    if 'loggedin' in session:
        # Here I try the POST method, but have problems to add error handling.
        # I Bypass that by adding a try/except condition just printing a message on the console.
        # Flash working just fine in auth So I have no clue, still investigate on date 25/07/2022
        try:
            if request.method == 'POST':
                title = request.form['title']
                house = request.form['house']
                price = int(request.form['price'])
                review = request.form['review']
                conn = get_db_connection()
                cur = conn.cursor()
                cur.execute('INSERT INTO vins (title, house, price, review)'
                            'VALUES (%s, %s, %s, %s)',
                            (title, house, price, review))
                conn.commit()
                cur.close()
                conn.close()
                return redirect(url_for('index'))
        except:
            print("Attention il y a eu une erreur dans le formulaire")
        return render_template('create.html')
    return redirect(url_for('auth.login'))


# The get or post method route + controller which updates in the Table vins an existing wine by ID.
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    vin = []
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM vins WHERE id = %s", (str(id)))
        # Here we are storing in vins the results of the select method at top
        vins = cursor.fetchall()
        # Then we try a parsing and we understand we have only vins[o] so vi is one line only
        # And so we understand the for needed in the html code --->
        for vi in vins:
            print(vi[0], vi[1], vi[2], vi[3])
        conn.close()  # Closing here permits reexecute a cursor.fetchall() above
        # But this part is going to be deleted because no need anymore
        conn = get_db_connection()  # -----//
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vins WHERE id = %s", (str(id)))
        for row in cursor.fetchall():
            vin.append({"id": row[0], "title": row[1], "house": row[2], "price": row[3]})
            print(vin)
        conn.close()  # -----//
        # Above, we return as parameters the list vin and vins to the front side
        return render_template("update.html", vin=vin, vins=vins)
    if request.method == 'POST':
        title = request.form["title"]
        house = request.form["house"]
        price = int(request.form['price'])
        cursor.execute("UPDATE vins SET "
                       "title = %s, house = %s, price = %s "
                       "WHERE id = %s",
                       (title, house, price, id))
        conn.commit()
        conn.close()
        return redirect('/')


# The delete function route + controller, it deletes a wine by ID.
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM vins WHERE id = %s", (str(id)))
    conn.commit()
    conn.close()
    return redirect('/')
