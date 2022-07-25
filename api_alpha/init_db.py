# Name : Crud_API
# Version : Alpha
# Creation date : 18/07/2022
# Author : Gerhard Eibl
# INFO : This file serves to initialize a new Table vins + users and add data in vins.
# ----------------------------------------------------------------------------------- #

import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="api_alpha",
    # user=os.environ['DB_USERNAME'],
    # password=os.environ['DB_PASSWORD'])
    user="postgres",
    password="rootroot")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute command to create vins table
cur.execute('DROP TABLE IF EXISTS vins;')
cur.execute('CREATE TABLE vins (id serial PRIMARY KEY,'
            'title varchar (150) NOT NULL,'
            'house varchar (50) NOT NULL,'
            'price integer NOT NULL,'
            'review text,'
            'date_added date DEFAULT CURRENT_TIMESTAMP);')

# Execute command to create users table
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
            'fullname VARCHAR ( 100 ) NOT NULL,'
            'username VARCHAR ( 50 ) NOT NULL,'
            'password VARCHAR ( 255 ) NOT NULL,'
            'email VARCHAR ( 50 ) NOT NULL,'
            'date_added date DEFAULT CURRENT_TIMESTAMP);')

# Insert data into the table
cur.execute('INSERT INTO vins (title, house, price, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Petrus 2009',
             'Pomerol',
             1783,
             'A great classic!')
            )

cur.execute('INSERT INTO vins (title, house, price, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Gewurztraminner 2005',
             'Alsace',
             864,
             'Another great classic!')
            )

cur.execute('INSERT INTO vins (title, house, price, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Petrus 2005',
             'Bordeaux',
             2642,
             'Another great classic!')
            )

cur.execute('INSERT INTO vins (title, house, price, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Chateau neuf du pape 2012',
             'Clos de l-oratoire des papes',
             96,
             'Another great classic!')
            )

cur.execute('INSERT INTO vins (title, house, price, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Chateau neuf du pape 2002',
             'Clos de l-oratoire des papes',
             462,
             'Another great classic!')
            )

cur.execute('INSERT INTO vins (title, house, price, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Chateau neuf du pape 1998',
             'Clos de l-oratoire des papes',
             723,
             'Another great classic!')
            )

conn.commit()

# Close the cursor + the DB connexion
cur.close()
conn.close()
