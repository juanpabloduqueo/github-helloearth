# Sample Flask application for a BSG database, snapshot of BSG_people

from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os


app = Flask(__name__)

# database connection
# Template:
# app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
# app.config["MYSQL_USER"] = "cs340_OSUusername"
# app.config["MYSQL_PASSWORD"] = "XXXX" | last 4 digits of OSU id
# app.config["MYSQL_DB"] = "cs340_OSUusername"
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# database connection info
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs340_duqueocj"
app.config["MYSQL_PASSWORD"] = "7389"
app.config["MYSQL_DB"] = "cs340_duqueocj"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# Routes
# have homepage route to /machines by default for convenience, generally this will be your home route with its own template
''' ############################################################################################################################
MACHINES ROUTES
############################################################################################################################ '''

@app.route("/")
def home():
    return redirect("/machines")


# route for machines page
@app.route("/machines", methods=["POST", "GET"])
def machines():
    # Separate out the request methods, in this case this is for a POST
    # insert a machine into the Machines entity
    if request.method == "POST":
    # fire off if user presses the Add Machine button
        if request.form.get("Add_Machine"):
            # grab user form inputs
            year = request.form["year"]
            make = request.form["make"]
            model = request.form["model"]
            serial = request.form["serial"]
            # class is a python reserved word, so it was changed to clas. This has to be modified in the other files!!!!
            clas = request.form["class"]

            # This table does no accept null inputs
            # WE HAVE AN ISSUE WITH CLASS (it is an attribute but it is a python reserved word). SHOULD WE CHANGE THIS ATTRIBUTE NAME? MAYBE TO Category?
            query = "INSERT INTO Machines (year, make, model, serial, class) VALUES (%s, %s,%s,%s, %s);"
            cur = mysql.connection.cursor()
            # Must pay attention when writing clas instead of class!!!
            cur.execute(query, (year, make, model, serial, clas))
            mysql.connection.commit()

            # redirect back to people page
            return redirect("/machines")
    
    # Grab Machines data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the machines in Machines
        query = "SELECT machineId, year, make, model, serial, class FROM Machines"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_machine page passing our query data to the edit_machine template
        return render_template("machines.j2", data=data)

# route for delete functionality, deleting a machine from Machines,
# we want to pass the 'id' value of that machine on button click (see HTML) via the route
@app.route("/delete_machines/<int:machineId>")
def delete_machines(machineId):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM Machines WHERE machineId = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (machineId,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/machines")

# route for edit functionality, updating the attributes of a machine in Machines
# similar to our delete route, we want to the pass the 'id' value of that machine on button click (see HTML) via the route
@app.route("/edit_machines/<int:machineId>", methods=["POST", "GET"])
def edit_machines(machineId):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Machines WHERE machineId = %s" % (machineId)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_machines page passing our query data edit_machines template
        return render_template("edit_machines.j2", data=data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Machine' button
        if request.form.get("Edit_Machine"):
            # grab user form inputs
            year = request.form["year"]
            make = request.form["make"]
            model = request.form["model"]
            serial = request.form["serial"]
            # class is a python reserved word, so it was changed to clas. This has to be modified in the other files!!!!
            clas = request.form["class"]

            # This table does not accept null inputs
            query = "UPDATE Machines SET Machines.year = %s, Machines.make = %s, Machines.model = %s, Machines.serial = %s, Machines.class = %s  WHERE Machines.machineId = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (year, make, model, serial, clas, machineId))
            mysql.connection.commit()
            
            # redirect back to people page after we execute the update query
            return redirect("/machines")

''' ############################################################################################################################
LOCATIONS ROUTES
############################################################################################################################ '''

# route for locations page
@app.route("/locations", methods=["POST", "GET"])
def locations():
    # Separate out the request methods, in this case this is for a POST
    # insert a location into the Locations entity
    if request.method == "POST":
    # fire off if user presses the Add Location button
        if request.form.get("Add_Location"):
            # grab user form inputs
            locationId = request.form["locationId"]
            locationName = request.form["locationName"]
            address = request.form["address"]
            zipcode = request.form["zipcode"]
            state = request.form["state"]
            isClientLocation = request.form["isClientLocation"]

            # This table does not accept null inputs
            query = "INSERT INTO Locations (locationId, locationName, address, zipcode, state, isClientLocation) VALUES (%s, %s, %s,%s,%s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (locationId, locationName, address, zipcode, state, isClientLocation))
            mysql.connection.commit()

            # redirect back to people page
            return redirect("/locations")
    

    # Grab Locations data so we send it to our template to display [IS THIS NECESSARY TO LEAVE IT????]
    if request.method == "GET":
        # mySQL query to grab all the locations in Locations
        query = "SELECT locationId, locationName, address, zipcode, state, isClientLocation FROM Locations;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_machine page passing our query data to the edit_machine template (I DON´T THINK WE NEED EDIT FOR LOCATIONS) --> WE COULD DELETE THIS
        return render_template("locations.j2", data=data)


# route for delete functionality, deleting a location from Locations,
# we want to pass the 'id' value of that location on button click (see HTML) via the route
@app.route("/delete_locations/<int:locationId>")
def delete_locations(locationId):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM Locations WHERE locationId = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (locationId,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/locations")

''' ############################################################################################################################
MECHANICS ROUTES
############################################################################################################################ '''

# route for mechanics page
@app.route("/mechanics", methods=["POST", "GET"])
def mechanics():
    # Separate out the request methods, in this case this is for a POST
    # insert a mechanic into the Mechanics entity
    if request.method == "POST":
    # fire off if user presses the Add Location button
        if request.form.get("Add_Mechanic"):
            # grab user form inputs
            mechanicId = request.form["mechanicId"]
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            phone = request.form["phone"]
            email = request.form["email"]

            # This table does no accept null inputs
            query = "INSERT INTO Mechanics (mechanicId, firstName, lastName, phone, email) VALUES (%s, %s, %s,%s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (mechanicId, firstName, lastName, phone, email))
            mysql.connection.commit()

            # redirect back to mechanics page
            return redirect("/mechanics")
    

    # Grab Mechanics data so we send it to our template to display [IS THIS NECESSARY TO LEAVE IT????
    # ]
    if request.method == "GET":
        # mySQL query to grab all the machines in Machines
        query = "SELECT mechanicId, firstName, lastName, phone, email FROM Mechanics;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_machine page passing our query data to the edit_machine template (I DON´T THINK WE NEED EDIT FOR LOCATIONS) --> WE COULD DELETE THIS
        return render_template("mechanics.j2", data=data)


# route for delete functionality, deleting a mechanic from Mechanics,
# we want to pass the 'id' value of that Mechanic on button click (see HTML) via the route
@app.route("/delete_mechanics/<int:mechanicId>")
def delete_mechanics(mechanicId):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM Mechanics WHERE mechanicId = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (mechanicId,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/mechanics")

''' ############################################################################################################################
WORK ORDER ROUTES
############################################################################################################################ '''

# route for work orders page
@app.route("/workorders", methods=["POST", "GET"])
def workOrders():
    # Separate out the request methods, in this case this is for a POST
    # insert a work order into the WorkOrders entity
    if request.method == "POST":
        # fire off if user presses the Add Person button
        if request.form.get("Add_Work_Order"):
            # grab user form inputs
            machineId = request.form["serial"]
            locationId = request.form["locationId"]
            date = request.form["date"]
            description = request.form["description"]

            # account for null locationId
            if locationId == "0":
                # mySQL query to insert a new work order into WorkOrders with our form inputs
                # query = "INSERT INTO WorkOrders (machineId, date, description) VALUES ((SELECT machineId FROM Machines WHERE serial = %s), %s, %s)"  
                query = "INSERT INTO WorkOrders (machineId, date, description) VALUES (%s, %s, %s)"               
                cur = mysql.connection.cursor()
                cur.execute(query, (machineId, date, description))
                mysql.connection.commit()

            # no null inputs
            else:
                # query = "INSERT INTO WorkOrders (machineId, locationId, date, description) VALUES ((SELECT machineId FROM Machines WHERE serial = %s), %s, %s, %s)"
                query = "INSERT INTO WorkOrders (machineId, locationId, date, description) VALUES (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (machineId, locationId, date, description))
                mysql.connection.commit()

            # redirect back to people page
            return redirect("/workorders")

    # Grab workOrders data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the work orders in workOrders
        query = ("SELECT WorkOrders.workOrderId," 
        "Machines.model AS 'Machine Model', Machines.serial AS 'Machine Serial', Locations.locationName AS 'Location Name', WorkOrders.date AS 'Date', WorkOrders.description AS 'Description'"
        "FROM WorkOrders " 
        "INNER JOIN Machines ON WorkOrders.machineId = Machines.machineId " 
        "INNER JOIN Locations ON WorkOrders.locationId = Locations.locationId")
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # mySQL query to grab work order id/name data for our dropdown
        query2 = "SELECT workOrderId FROM WorkOrders"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        workOrderId_data = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("workorders.j2", data=data, workOrderIds=workOrderId_data)


# route for delete functionality, deleting a work order from WorkOrders,
# we want to pass the 'id' value of that work order on button click (see HTML) via the route
@app.route("/delete_workorder/<int:workOrderId>")
def delete_workorder(workOrderId):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM WorkOrders WHERE workOrderId = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (workOrderId,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/workorders")

''' ############################################################################################################################
WORK ORDER PRODUCTS ROUTES
############################################################################################################################ '''

# route for work order products page
@app.route("/productdetails/<int:workOrderId>", methods=["POST", "GET"])
def product_details(workOrderId):
    # Separate out the request methods, in this case this is for a POST
    # insert a work order into the WorkOrders entity
    if request.method == "POST":
        # fire off if user presses the Add Product to Work Order button
        if request.form.get("Add_Product"):
            # grab user form inputs
            productId = request.form["reference"]

            query = "INSERT INTO WorkOrderProducts (workOrderId, productId) VALUES (%s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (workOrderId, productId,))
            mysql.connection.commit()

            # redirect back to work orders page
            return redirect("/workorders")

    # Grab workOrderProducts data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the work orders in workOrderProducts
        query = ("SELECT WorkOrderProducts.workOrderProductId, Products.productId, Products.productName, Products.reference "
        "FROM WorkOrderProducts "
        "JOIN Products ON WorkOrderProducts.productId = Products.productId "
        "WHERE WorkOrderProducts.workOrderId = %s;")
        cur = mysql.connection.cursor()
        cur.execute(query, (workOrderId,))
        data = cur.fetchall()

        # # mySQL query to grab work order id/name data for our dropdown
        # query2 = "SELECT workOrderId FROM WorkOrders"
        # cur = mysql.connection.cursor()
        # cur.execute(query2)
        # workOrderId_data = cur.fetchall()

        # render work order products page passing our query data to the template
        return render_template("workorderproducts.j2", data=data)


# route for delete functionality, deleting a product from a work order,
# we want to pass the 'workOrderProductId' value of that product on button click (see HTML) via the route
@app.route("/productdetails/delete_product/<int:workOrderProductId>")
def delete_product(workOrderProductId):
    # mySQL query to delete the product with our passed id
    query = "DELETE FROM WorkOrderProducts WHERE workOrderProductId = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (workOrderProductId,))
    mysql.connection.commit()

    # redirect back to work orders page
    return redirect("/workorders")


''' ############################################################################################################################
WORK ORDER MECHANICS ROUTES
############################################################################################################################ '''

# WORK ORDER MECHANICS ROUTES
# route for work orders page
@app.route("/workordermechanics/<int:workOrderId>", methods=["POST", "GET"])
def workOrderMechanics(workOrderId):
    # Separate out the request methods, in this case this is for a POST
    # insert a work order into the WorkOrders entity
    if request.method == "POST":
        # fire off if user presses the Add Person button
        if request.form.get("Add_Work_Order_Mechanic"):
            # grab user form inputs
            workOrderMechanicId = request.form["workOrderMechanicId"]
            workOrderId = request.form["workOrderId"]
            mechanicId = request.form["mechanicId"]

            # account for null mechanicId
            if mechanicId == "":
                # mySQL query to insert a new work order into WorkOrders with our form inputs
                query = "INSERT INTO WorkOrderMechanics (workOrderMechanicId) VALUES (%s);"                
                cur = mysql.connection.cursor()
                cur.execute(query, (workOrderId))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "INSERT INTO WorkOrderMechanics (workOrderMechanicId, mechanicId) VALUES (%s, %s);"
                cur = mysql.connection.cursor()
                cur.execute(query, (workOrderId, mechanicId))
                mysql.connection.commit()

            # redirect back to work order mechanic page
            return redirect("/workordermechanics/<int:workOrderId>")

    # Grab workOrderMechanics data of the Work Order so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the work order mechanics in the work Order
        workOrderId = request.form["workOrderId"]
        query = ("SELECT Mechanics.firstName, Mechanics.lastName FROM WorkOrderMechanics \
                 JOIN Mechanics ON WorkOrderMechanics.mechanicId = Mechanics.mechanicId \
                 WHERE WorkOrderMechanics.workOrderId = '%s'" %(workOrderId))
        '''
        ("SELECT Mechanics.firstName, Mechanics.lastName FROM WorkOrderMechanics \
                 JOIN Mechanics ON WorkOrderMechanics.mechanicId = Mechanics.mechanicId \
                 WHERE WorkOrderMechanics.workOrderId = '%s'" %(workOrderId))
        '''
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # mySQL query to grab work order id/name data for our dropdown
        query2 = "SELECT Mechanics.email FROM Mechanics"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        workOrderId = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("workordermechanics.j2", data=data, workOrderId=workOrderId)

@app.route("/delete_workordermechanics/<int:workOrderMechanicId>")
def delete_workorderMechanics(workOrderMechanicId):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM WorkOrderMechanics WHERE workOrderMechanicId = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (workOrderMechanicId,))
    mysql.connection.commit()

    # redirect back to work order mechanics
    return redirect("/workorderMechanics")




# route for delete functionality, deleting a work order from WorkOrders,
# we want to pass the 'id' value of that work order on button click (see HTML) via the route
@app.route("/delete_workorder/<int:workOrderId>")
def delete_workorder(workOrderId):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM WorkOrders WHERE workOrderId = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (workOrderId,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/workorders")


# Listener
# change the port number if deploying on the flip servers
if __name__ == "__main__":
    app.run(port=3246, debug=True)

"""
# route for people page
@app.route("/people", methods=["POST", "GET"])
def people():
    # Separate out the request methods, in this case this is for a POST
    # insert a person into the bsg_people entity
    if request.method == "POST":
        # fire off if user presses the Add Person button
        if request.form.get("Add_Person"):
            # grab user form inputs
            fname = request.form["fname"]
            lname = request.form["lname"]
            homeworld = request.form["homeworld"]
            age = request.form["age"]

            # account for null age AND homeworld
            if age == "" and homeworld == "0":
                # mySQL query to insert a new person into bsg_people with our form inputs
                query = "INSERT INTO bsg_people (fname, lname) VALUES (%s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (fname, lname))
                mysql.connection.commit()

            # account for null homeworld
            elif homeworld == "0":
                query = "INSERT INTO bsg_people (fname, lname, age) VALUES (%s, %s,%s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (fname, lname, age))
                mysql.connection.commit()

            # account for null age
            elif age == "":
                query = "INSERT INTO bsg_people (fname, lname, homeworld) VALUES (%s, %s,%s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (fname, lname, homeworld))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "INSERT INTO bsg_people (fname, lname, homeworld, age) VALUES (%s, %s,%s,%s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (fname, lname, homeworld, age))
                mysql.connection.commit()

            # redirect back to people page
            return redirect("/people")

    # Grab bsg_people data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the people in bsg_people
        query = "SELECT bsg_people.id, fname, lname, bsg_planets.name AS homeworld, age FROM bsg_people LEFT JOIN bsg_planets ON homeworld = bsg_planets.id"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # mySQL query to grab planet id/name data for our dropdown
        query2 = "SELECT id, name FROM bsg_planets"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        homeworld_data = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("people.j2", data=data, homeworlds=homeworld_data)


# route for delete functionality, deleting a person from bsg_people,
# we want to pass the 'id' value of that person on button click (see HTML) via the route
@app.route("/delete_people/<int:id>")
def delete_people(id):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM bsg_people WHERE id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/people")


# route for edit functionality, updating the attributes of a person in bsg_people
# similar to our delete route, we want to the pass the 'id' value of that person on button click (see HTML) via the route
@app.route("/edit_people/<int:id>", methods=["POST", "GET"])
def edit_people(id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM bsg_people WHERE id = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # mySQL query to grab planet id/name data for our dropdown
        query2 = "SELECT id, name FROM bsg_planets"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        homeworld_data = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("edit_people.j2", data=data, homeworlds=homeworld_data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Person' button
        if request.form.get("Edit_Person"):
            # grab user form inputs
            id = request.form["personID"]
            fname = request.form["fname"]
            lname = request.form["lname"]
            homeworld = request.form["homeworld"]
            age = request.form["age"]

            # account for null age AND homeworld
            if (age == "" or age == "None") and homeworld == "0":
                # mySQL query to update the attributes of person with our passed id value
                query = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = NULL, bsg_people.age = NULL WHERE bsg_people.id = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (fname, lname, id))
                mysql.connection.commit()

            # account for null homeworld
            elif homeworld == "0":
                query = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = NULL, bsg_people.age = %s WHERE bsg_people.id = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (fname, lname, age, id))
                mysql.connection.commit()

            # account for null age
            elif age == "" or age == "None":
                query = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = %s, bsg_people.age = NULL WHERE bsg_people.id = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (fname, lname, homeworld, id))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "UPDATE bsg_people SET bsg_people.fname = %s, bsg_people.lname = %s, bsg_people.homeworld = %s, bsg_people.age = %s WHERE bsg_people.id = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (fname, lname, homeworld, age, id))
                mysql.connection.commit()

            # redirect back to people page after we execute the update query
            return redirect("/people")
"""

