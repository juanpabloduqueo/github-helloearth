from flask import Flask, render_template, json
import os
import database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()

# Routes 

@app.route('/')
def root():
    return render_template("machines.j2")

@app.route('/machines')
def bsg_people():
    query = "SELECT * FROM Machines;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("machines.j2", machines=results)

@app.route('/locations')
def bsg_people():
    query = "SELECT * FROM Locations;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("locations.j2", locations=results)



# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3246))
    app.run(port=port, debug=True)