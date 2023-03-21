-- Group 39
-- Team Members: Juan Pablo Duque Ochoa, Marco Scandroglio
-- Project Name: Hello Earth!
-- Project Step 6 (Portfolio Assignment - Group) 

-- Database Manipulation queries organized by page
-- the colon : character is being used to denote the variables that 
-- will have data from the backend programming language throughout


-------------------------------------------------------
-- Machines Page
-------------------------------------------------------

-- Display Machines table on Machines page
SELECT Machines.machineId, Machines.year AS 'Year', Machines.make AS 'Make', Machines.model AS 'Model', Machines.serial AS 'Serial', Machines.class AS 'Class' 
FROM Machines;

-- Display information from single machine
SELECT * FROM Machines WHERE machineId = :machine_ID_from_route;

-- Add machine to Machines table
INSERT INTO Machines (year, make, model, serial, class) 
VALUES (:yearInput, :makeInput, :modelInput, :serialInput, :classInput);

-- Update Machine in Machines Table
UPDATE Machines SET Machines.year = :yearInput, Machines.make = :makeInput, Machines.model = :modelInput, Machines.serial = :serialInput, Machines.class = :classInput  
WHERE Machines.machineId = :machine_ID_from_route;

-- Delete Machine in Machines Table
DELETE FROM Machines WHERE machineId = :machineId_from_the_delete_form;


-------------------------------------------------------
-- Locations Page
-------------------------------------------------------

-- Display Locations table on Locations page
SELECT Locations.locationId, Locations.locationName AS 'Location Name', Locations.address AS 'Address', Locations.zipcode AS 'Zipcode', Locations.state AS 'State', Locations.isClientLocation AS 'Client Location' 
FROM Locations;

-- Display information from single location
SELECT * FROM Locations WHERE locationId = :location_ID_from_route;

-- add location to Locations table
INSERT INTO Locations (locationName, address, zipcode, state, isClientLocation)
VALUES (:locationNameInput, :addressInput, :zipcodeInput, :stateInput, :isClientLocationInput);

-- Update location in Locations table
UPDATE Locations SET Locations.locationName = :locationNameInput, Locations.address = :addressInput, Locations.zipcode = :zipcodeInput, Locations.state = :stateInput, Locations.isClientLocation = :isClientLocationInput 
WHERE Locations.locationId = :location_ID_from_route;

-- Delete Location in Locations table
DELETE FROM Locations WHERE locationId = :location_ID_from_route;


-------------------------------------------------------
-- Mechanics Page
-------------------------------------------------------

-- Display Mechanics table on Mechanics page
SELECT Mechanics.mechanicId, Mechanics.firstName AS 'First Name', Mechanics.lastName AS 'Last Name', Mechanics.phone AS 'Phone Number', Mechanics.email AS 'Email Address' 
FROM Mechanics;

-- Display information from single mechanic
SELECT * FROM Mechanics WHERE mechanicId = :mechanic_ID_from_route;

-- add mechanic to Mechanics table
INSERT INTO Mechanics (firstName, lastName, phone, email)
VALUES (:firstNameInput, :lastNameInput, :phoneInput, :emailInput);

-- Update mechanic in Mechanics table
UPDATE Mechanics SET Mechanics.firstName = :firstNameInput, Mechanics.lastName = :lastNameInput, Mechanics.phone = :phoneInput, Mechanics.email = :emailInput 
WHERE Mechanics.mechanicId = :mechanic_ID_from_route;

-- Delete mechanic from Mechanics table
DELETE FROM Mechanics WHERE mechanicId = :mechanic_ID_from_route;


-------------------------------------------------------
-- Products Page
-------------------------------------------------------

-- Display Products table on Products page
SELECT productId, productName AS 'Product Name', reference AS 'Reference', brand AS 'Brand', description AS 'Description' 
FROM Products;

-- Display information for single product
SELECT * FROM Products WHERE productId = :product_ID_from_route;

-- add product to Products table
INSERT INTO Products (productName, reference, brand, description)
VALUES (:productNameInput, :referenceInput, :brandInput, :descriptionInput);

-- Update product in Products table
UPDATE Products SET Products.productName = :productNameInput, Products.reference = :referenceInput, Products.brand = :brandInput, Products.description = :descriptionInput 
WHERE Products.productId = :product_ID_from_route;

-- Delete product from Products table
DELETE FROM Products WHERE productId = :product_ID_from_route;


-------------------------------------------------------
-- WorkOrders Page
-------------------------------------------------------

-- Display a join of WorkOrders, Machines, and Locations WorkOrders page
-- shows a more complete description of each work order
SELECT WorkOrders.workOrderId, 
       Machines.model AS "Machine Model", 
       Machines.serial AS "Machine Serial", 
       Locations.locationName AS "Location Name", 
       WorkOrders.date AS "Date", 
       WorkOrders.description AS "Description"
FROM WorkOrders 
LEFT JOIN Machines ON WorkOrders.machineId = Machines.machineId 
LEFT JOIN Locations ON WorkOrders.locationId = Locations.locationId;

-- Create new work order with NULL location input
INSERT INTO WorkOrders (machineId, date, description)
VALUES (
  (SELECT machineId FROM Machines WHERE serial = :machineSerialInput_from_the_create_form),
  :dateInput,
  :descriptionInput
);

-- create new work order with no NULL inputs
INSERT INTO WorkOrders (machineId, locationId, date, description)
VALUES (
  (SELECT machineId FROM Machines WHERE serial = :machineSerialInput_from_the_create_form),
  :locationId_from_the_create_form,
  :dateInput,
  :descriptionInput
);

-- update existing work order
UPDATE WorkOrders 
    SET machineId = (SELECT machineId FROM Machines WHERE serial = :machineSerialInput), 
    locationName = :locationNameInput, 
    date = :dateInput, 
    description= :descriptionInput 
    WHERE workOrderId = :workOrderId_from_route;

-- Delete work order in WorkOrder Table
DELETE FROM WorkOrders WHERE workOrderId = :workOrderId_from_route;

-- populate Machine Serial dropdown
SELECT machineId, serial from Machines;

-- populate locationName dropdown
SELECT locationId, locationName from Locations;


-------------------------------------------------------
-- Work Order Details Page
-------------------------------------------------------

-- Display the selected work order
SELECT WorkOrders.workOrderId, 
    Machines.model AS 'Machine Model', 
    Machines.serial AS 'Machine Serial', 
    Locations.locationName AS 'Location Name', 
    WorkOrders.date AS 'Date', 
    WorkOrders.description AS 'Description'
FROM WorkOrders 
LEFT JOIN Machines ON WorkOrders.machineId = Machines.machineId 
LEFT JOIN Locations ON WorkOrders.locationId = Locations.locationId
WHERE WorkOrders.workOrderId = :workOrderId_from_route;

-- display products associated with work order (JOIN utilizing intersection table)
SELECT WorkOrderProducts.workOrderProductId, 
    Products.productId, 
    Products.productName AS 'Product Name', 
    Products.reference AS 'Product Reference'
FROM WorkOrderProducts
JOIN Products ON WorkOrderProducts.productId = Products.productId
WHERE WorkOrderProducts.workOrderId = :workOrderId_from_route;

-- display mechanics associated with work order (JOIN utilizing intersection table)
SELECT WorkOrderMechanics.workOrderMechanicId, 
    Mechanics.firstName AS 'First Name', 
    Mechanics.lastName AS 'Last Name' 
FROM WorkOrderMechanics
JOIN Mechanics ON WorkOrderMechanics.mechanicId = Mechanics.mechanicId\
WHERE WorkOrderMechanics.workOrderId = :workOrderId_from_route;

-- add product to work order (M-to-M relationship addition)
INSERT INTO WorkOrderProducts (workOrderId, productId) VALUES (:workOrderId_from_route, :productId_from_input);

-- delete product from work order (M-to-M relationship deletion)
DELETE FROM WorkOrderProducts WHERE workOrderId = :workOrderProductId_from_route;

-- add mechanic to work order (M-to-M relationship addition)
INSERT INTO WorkOrderMechanics (workOrderId, mechanicId) VALUES (:workOrderId_from_route, :mechanicId_from_input);;

-- delete mechanic from work order (M-to-M relationship deletion)
DELETE FROM WorkOrderMechanics WHERE workOrderMechanicId = :workOrderMechanicId_from_route;

-- populate Product Reference dropdown with ids
SELECT productId, reference from Products;

-- populate Mechanic Email dropdown with ids not already associated with work order (prevents duplicates)
SELECT Mechanics.* 
FROM Mechanics
LEFT JOIN WorkOrderMechanics ON Mechanics.mechanicId = WorkOrderMechanics.mechanicId
AND WorkOrderMechanics.workOrderId = :workOrderId_from_route
WHERE WorkOrderMechanics.workOrderId IS NULL;
