# Project Step 6 (Portfolio Assignment - Group)
# Juan Pablo Duque and Marco Scandroglio
# Code Citation:
# Date: 03/20/2023
# Code adapted from Exploration 7 Course Content (Flask Starter App):
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app


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
app.config["MYSQL_USER"] = "cs340_scandrom"
app.config["MYSQL_PASSWORD"] = "5497"
app.config["MYSQL_DB"] = "cs340_scandrom"
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
            query = "INSERT INTO Machines (year, make, model, serial, class) VALUES (%s, %s, %s, %s, %s);"
            cur = mysql.connection.cursor()
            # Must pay attention when writing clas instead of class!!!
            cur.execute(query, (year, make, model, serial, clas))
            mysql.connection.commit()

            # redirect back to people page
            return redirect("/machines")
    
    # Grab Machines data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the machines in Machines
        query = "SELECT Machines.machineId, Machines.year AS 'Year', Machines.make AS 'Make', Machines.model AS 'Model', Machines.serial AS 'Serial', Machines.class AS 'Class' FROM Machines;"
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
        # mySQL query to grab the info of the machine with our passed id
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
            query = "UPDATE Machines SET Machines.year = %s, Machines.make = %s, Machines.model = %s, Machines.serial = %s, Machines.class = %s  WHERE Machines.machineId = %s;"
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
            locationName = request.form["locationName"]
            address = request.form["address"]
            zipcode = request.form["zipcode"]
            state = request.form["state"]
            isClientLocation = request.form["isClientLocation"]

            # This table does not accept null inputs
            query = "INSERT INTO Locations (locationName, address, zipcode, state, isClientLocation) VALUES (%s, %s, %s, %s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (locationName, address, zipcode, state, isClientLocation))
            mysql.connection.commit()

            # redirect back to people page
            return redirect("/locations")
    

    # Grab Locations data so we send it to our template to display [IS THIS NECESSARY TO LEAVE IT????]
    if request.method == "GET":
        # mySQL query to grab all the locations in Locations
        query = "SELECT Locations.locationId, Locations.locationName AS 'Location Name', Locations.address AS 'Address', Locations.zipcode AS 'Zipcode', Locations.state AS 'State', Locations.isClientLocation AS 'Client Location' FROM Locations;"
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
    query = "DELETE FROM Locations WHERE locationId = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query, (locationId,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/locations")

# route for edit functionality, updating the attributes of a location in Locations
# similar to our delete route, we want to the pass the 'id' value of that location on button click (see HTML) via the route
@app.route("/edit_locations/<int:locationId>", methods=["POST", "GET"])
def edit_locations(locationId):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Locations WHERE locationId = %s;" % (locationId)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_locations page passing our query data edit_locations template
        return render_template("edit_locations.j2", data=data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Location' button
        if request.form.get("Edit_Location"):
            # grab user form inputs
            locationName = request.form["locationName"]
            address = request.form["address"]
            zipcode = request.form["zipcode"]
            state = request.form["state"]
            isClientLocation = request.form["isClientLocation"]

            # This table does not accept null inputs
            query = "UPDATE Locations SET Locations.locationName = %s, Locations.address = %s, Locations.zipcode = %s, Locations.state = %s, Locations.isClientLocation = %s  WHERE Locations.locationId = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query, (locationName, address, zipcode, state, isClientLocation, locationId))
            mysql.connection.commit()
            
            # redirect back to locations page after we execute the update query
            return redirect("/locations")

''' ############################################################################################################################
PRODUCTS ROUTES
############################################################################################################################ '''

# route for mechanics page
@app.route("/products", methods=["POST", "GET"])
def products():
    # Separate out the request methods, in this case this is for a POST
    # insert a mechanic into the Mechanics entity
    if request.method == "POST":
    # fire off if user presses the Add Location button
        if request.form.get("Add_Product"):
            # grab user form inputs
            productName = request.form["productName"]
            reference = request.form["reference"]
            brand = request.form["brand"]
            description = request.form["description"]

            # This table does no accept null inputs
            query = "INSERT INTO Products (productName, reference, brand, description) VALUES (%s, %s,%s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (productName, reference, brand, description))
            mysql.connection.commit()

            # redirect back to mechanics page
            return redirect("/products")
    

    # Grab Products data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the machines in Machines
        query = "SELECT productId, productName AS 'Product Name', reference AS 'Reference', brand AS 'Brand', description AS 'Description' FROM Products;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_machine page passing our query data to the edit_machine template (I DON´T THINK WE NEED EDIT FOR LOCATIONS) --> WE COULD DELETE THIS
        return render_template("products.j2", data=data)


# route for delete functionality, deleting a product from Products,
# we want to pass the 'id' value of that product on button click (see HTML) via the route
@app.route("/delete_product/<int:productId>")
def delete_product(productId):
    # mySQL query to delete the product with our passed id
    query = "DELETE FROM Products WHERE productId = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query, (productId,))
    mysql.connection.commit()

    # redirect back to products page
    return redirect("/products")

# route for edit functionality, updating the attributes of a product in Products
# similar to our delete route, we want to the pass the 'id' value of that product on button click (see HTML) via the route
@app.route("/edit_products/<int:productId>", methods=["POST", "GET"])
def edit_products(productId):
    if request.method == "GET":
        # mySQL query to grab the info of the product with our passed id
        query = "SELECT * FROM Products WHERE productId = %s;" % (productId)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_products page passing our query data edit_products template
        return render_template("edit_products.j2", data=data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Product' button
        if request.form.get("Edit_Product"):
            # grab user form inputs
            productName = request.form["productName"]
            reference = request.form["reference"]
            brand = request.form["brand"]
            description = request.form["description"]

            # This table does not accept null inputs
            query = "UPDATE Products SET Products.productName = %s, Products.reference = %s, Products.brand = %s, Products.description = %s  WHERE Products.productId = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query, (productName, reference, brand, description, productId))
            mysql.connection.commit()
            
            # redirect back to locations page after we execute the update query
            return redirect("/products")


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
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            phone = request.form["phone"]
            email = request.form["email"]

            # This table does no accept null inputs
            query = "INSERT INTO Mechanics (firstName, lastName, phone, email) VALUES (%s, %s, %s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (firstName, lastName, phone, email))
            mysql.connection.commit()

            # redirect back to mechanics page
            return redirect("/mechanics")
    

    # Grab Mechanics data so we send it to our template to display [IS THIS NECESSARY TO LEAVE IT????
    # ]
    if request.method == "GET":
        # mySQL query to grab all the machines in Machines
        query = "SELECT Mechanics.mechanicId, Mechanics.firstName AS 'First Name', Mechanics.lastName AS 'Last Name', Mechanics.phone AS 'Phone Number', Mechanics.email AS 'Email Address' FROM Mechanics;"
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
    query = "DELETE FROM Mechanics WHERE mechanicId = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query, (mechanicId,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/mechanics")

# route for edit functionality, updating the attributes of a mechanic in Mechanics
# similar to our delete route, we want to the pass the 'id' value of that mechanic on button click (see HTML) via the route
@app.route("/edit_mechanics/<int:mechanicId>", methods=["POST", "GET"])
def edit_mechanics(mechanicId):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Mechanics WHERE mechanicId = %s;" % (mechanicId)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_mechanics page passing our query data edit_mechanics template
        return render_template("edit_mechanics.j2", data=data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Location' button
        if request.form.get("Edit_Mechanic"):
            # grab user form inputs
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            phone = request.form["phone"]
            email = request.form["email"]

            # This table does not accept null inputs
            query = "UPDATE Mechanics SET Mechanics.firstName = %s, Mechanics.lastName = %s, Mechanics.phone = %s, Mechanics.email = %s WHERE Mechanics.mechanicId = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query, (firstName, lastName, phone, email, mechanicId))
            mysql.connection.commit()
            
            # redirect back to locations page after we execute the update query
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
        query = ("SELECT WorkOrders.workOrderId, " 
        "Machines.model AS 'Machine Model', Machines.serial AS 'Machine Serial', Locations.locationName AS 'Location Name', WorkOrders.date AS 'Date', WorkOrders.description AS 'Description'"
        "FROM WorkOrders " 
        "LEFT JOIN Machines ON WorkOrders.machineId = Machines.machineId " 
        "LEFT JOIN Locations ON WorkOrders.locationId = Locations.locationId")
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        machine_dropdown_query = "SELECT machineId, serial FROM Machines;"
        cur = mysql.connection.cursor()
        cur.execute(machine_dropdown_query)
        machine_dropdown_data = cur.fetchall()

        location_dropdown_query = "SELECT locationId, locationName FROM Locations;"
        cur = mysql.connection.cursor()
        cur.execute(location_dropdown_query)
        location_dropdown_data = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("workorders.j2", data=data, machine_dropdown_data=machine_dropdown_data, location_dropdown_data=location_dropdown_data)


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
WORK ORDER DETAILS ROUTES
############################################################################################################################ '''

# route for work order details page
@app.route("/workorderdetails/<int:workOrderId>", methods=["POST", "GET"])
def workorder_details(workOrderId):

    if request.method == "POST":
        
        if request.form.get("Update_Work_Order"):
            # grab user form inputs
            machineId = request.form["serial"]
            locationId = request.form["locationId"]
            date = request.form["date"]
            description = request.form["description"]

            # account for null locationId
            if locationId == "0":
                # mySQL query to insert a new work order into WorkOrders with our form inputs
                # query = "INSERT INTO WorkOrders (machineId, date, description) VALUES ((SELECT machineId FROM Machines WHERE serial = %s), %s, %s)"  
                query = "UPDATE WorkOrders SET machineId = %s, date = %s, description = %s WHERE workOrderId = %s;"               
                cur = mysql.connection.cursor()
                cur.execute(query, (machineId, date, description, workOrderId))
                mysql.connection.commit()

            # no null inputs
            else:
                # query = "INSERT INTO WorkOrders (machineId, locationId, date, description) VALUES ((SELECT machineId FROM Machines WHERE serial = %s), %s, %s, %s)"
                query = "UPDATE WorkOrders SET machineId = %s, locationId = %s, date = %s, description = %s WHERE workOrderId = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, (machineId, locationId, date, description, workOrderId))
                mysql.connection.commit()

            # redirect to work order details page
            current_url = request.referrer or url_for('index')
            return redirect(current_url)

        if request.form.get("Add_Product"):

            productId = request.form["reference"]
            add_product_query = "INSERT INTO WorkOrderProducts (workOrderId, productId) VALUES (%s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(add_product_query, (workOrderId, productId,))
            mysql.connection.commit()

            # redirect to work order details page
            current_url = request.referrer or url_for('index')
            return redirect(current_url)

        if request.form.get("Add_Mechanic"):
            
            mechanicId = request.form["email"]
            add_mechanic_query = "INSERT INTO WorkOrderMechanics (workOrderId, mechanicId) VALUES (%s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(add_mechanic_query, (workOrderId, mechanicId))
            mysql.connection.commit()

            # redirect back to work order mechanic page
            current_url = request.referrer or url_for('index')
            return redirect(current_url)


    # Grab workOrderProducts data so we send it to our template to display
    if request.method == "GET":

        # work orders queries
        workorder_query = ("SELECT WorkOrders.workOrderId," 
        "Machines.model AS 'Machine Model', Machines.serial AS 'Machine Serial', Locations.locationName AS 'Location Name', WorkOrders.date AS 'Date', WorkOrders.description AS 'Description'"
        "FROM WorkOrders " 
        "LEFT JOIN Machines ON WorkOrders.machineId = Machines.machineId " 
        "LEFT JOIN Locations ON WorkOrders.locationId = Locations.locationId "
        "WHERE WorkOrders.workOrderId = %s;")
        cur = mysql.connection.cursor()
        cur.execute(workorder_query, (workOrderId,))
        workorder_data = cur.fetchall()

        # queries for work order update form
        machine_dropdown_query = "SELECT machineId, serial FROM Machines;"
        cur = mysql.connection.cursor()
        cur.execute(machine_dropdown_query)
        machine_dropdown_data = cur.fetchall()

        location_dropdown_query = "SELECT locationId, locationName FROM Locations;"
        cur = mysql.connection.cursor()
        cur.execute(location_dropdown_query)
        location_dropdown_data = cur.fetchall()

        # products queries
        products_query = ("SELECT WorkOrderProducts.workOrderProductId, Products.productId, Products.productName AS 'Product Name', Products.reference AS 'Product Reference' "
        "FROM WorkOrderProducts "
        "JOIN Products ON WorkOrderProducts.productId = Products.productId "
        "WHERE WorkOrderProducts.workOrderId = %s;")
        cur = mysql.connection.cursor()
        cur.execute(products_query, (workOrderId,))
        products_data = cur.fetchall()

        products_dropdown_query = "SELECT productId, reference FROM Products;"
        cur = mysql.connection.cursor()
        cur.execute(products_dropdown_query)
        products_drp_dwn = cur.fetchall()

        # check if there are any records in the workorderproducts intersection table for this work order
        products_message = None

        if not products_data:
            products_message = "There are no products assigned to this work order yet."
        
        # mechanics queries
        # mySQL query to grab all the work order mechanics in the work Order
        mechanics_query = ("SELECT WorkOrderMechanics.workOrderMechanicId, Mechanics.firstName AS 'First Name', Mechanics.lastName AS 'Last Name' FROM WorkOrderMechanics\
                 JOIN Mechanics ON WorkOrderMechanics.mechanicId = Mechanics.mechanicId\
                 WHERE WorkOrderMechanics.workOrderId = %s;")
        cur = mysql.connection.cursor()
        cur.execute(mechanics_query, (workOrderId,))
        mechanics_data = cur.fetchall()

        mechanics_dropdown_query = ("SELECT Mechanics.* "
        "FROM Mechanics "
        "LEFT JOIN WorkOrderMechanics ON Mechanics.mechanicId = WorkOrderMechanics.mechanicId "
        "AND WorkOrderMechanics.workOrderId = %s "
        "WHERE WorkOrderMechanics.workOrderId IS NULL;")
        cur = mysql.connection.cursor()
        cur.execute(mechanics_dropdown_query, (workOrderId,))
        mechanics_drp_dwn = cur.fetchall()

        # check if there are any records in the workordermechanics intersection table for this work order
        mechanics_message = None
        if not mechanics_data:
            mechanics_message = "There are no mechanics assigned to this work order yet."

        # render work order products page passing our query data to the template
        # workOrderId is passed to the template so it is defined in the action for the form
        return render_template("workorder_details.j2", workorder_data=workorder_data, workOrderId=workOrderId,
        machine_dropdown_data=machine_dropdown_data, location_dropdown_data=location_dropdown_data,
        products_data=products_data, products_message=products_message, products_drp_dwn=products_drp_dwn,
        mechanics_data=mechanics_data, mechanics_message=mechanics_message, mechanics_drp_dwn=mechanics_drp_dwn
        )


@app.route("/workorderdetails/delete_workorder/<int:workOrderId>")
def delete_workorder_details(workOrderId):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM WorkOrders WHERE workOrderId = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (workOrderId,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/workorders")


# route for delete functionality, deleting a product from a work order,
# we want to pass the 'workOrderProductId' value of that product on button click (see HTML) via the route
@app.route("/productdetails/delete_product/<int:workOrderProductId>")
def delete_product_from_work_order(workOrderProductId):
    # mySQL query to delete the product with our passed id
    query = "DELETE FROM WorkOrderProducts WHERE workOrderProductId = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (workOrderProductId,))
    mysql.connection.commit()

    # redirect to current page
    current_url = request.referrer or url_for('index')
    return redirect(current_url)


# route for delete functionality, deleting a mechanic from a work order,
# we want to pass the 'workOrderMechanicId' value of that mechanic on button click (see HTML) via the route
@app.route("/mechanicdetails/delete_mechanics/<int:workOrderMechanicId>") 
def delete_workorderMechanics(workOrderMechanicId ):
    # mySQL query to delete the mechanic with our passed id
    query = "DELETE FROM WorkOrderMechanics WHERE workOrderMechanicId = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query, (workOrderMechanicId,))
    mysql.connection.commit()

    # redirect to current page
    current_url = request.referrer or url_for('index')
    return redirect(current_url)


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


# Listener
# change the port number if deploying on the flip servers
if __name__ == "__main__":
    app.run(port=11238, debug=True)

