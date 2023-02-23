-- Group 39
-- Team Members: Juan Pablo Duque Ochoa, Marco Scandroglio
-- Project Name: Hello Earth!
-- Project Step 3 Draft Version: Design HTML Interface + DML SQL (Group / On Ed Discussion ) 

-- Database Manipulation queries organized by page
-- the colon : character is being used to denote the variables that 
-- will have data from the backend programming language throughout


-------------------------------------------------------
-- Machines Page
-------------------------------------------------------

-- Display Machines table on Machines page
SELECT machineId AS Machine Id, year AS Year, make AS Make, model AS Model, serial AS Serial, class AS Class
FROM Machines;

-- Add machine to Machines table
INSERT INTO Machines (year, make, model, serial, class) 
VALUES (:yearInput, :makeInput, :modelInput, :serialInput, :classInput);

-- Update Machine in Machines Table
UPDATE Machines SET year = :yearInput, make = :makeInput, model = :modelInput, serial = :serialInput, class = :classInput WHERE id= :machine_ID_from_the_update_form;

-- Delete Machine in Machines Table
DELETE FROM Machines WHERE machineId = :machineId_from_the_update_form;


-------------------------------------------------------
-- Locations Page
-------------------------------------------------------

-- Display Locations table on Locations page
SELECT locationId AS Location Id,  locationName AS Location Name, address AS Adress, zipcode AS Zip Code, state AS State, isClientLocation AS Client Location?
FROM Locations;

-- add location to Locations table
INSERT INTO Locations (locationName, address, zipcode, state, isClientLocation)
VALUES (:locationNameInput, :addressInput, :zipcodeInput, :stateInput, :isClientLocationInput);


-------------------------------------------------------
-- Mechanics Page
-------------------------------------------------------

-- Display Mechanics table on Mechanics page
SELECT mechanicId AS Mechanic Id, firstName AS First Name, lastName AS Last Name, phone AS Phone, email AS Email
FROM Mechanics;

-- add mechanic to Mechanics table
INSERT INTO Mechanics (firstName, lastName, phone, email)
VALUES (:firstNameInput, :lastNameInput, :phoneInput, :emailInput);


-------------------------------------------------------
-- Products Page
-------------------------------------------------------

-- Display Products table on Products page
SELECT productId AS Product Id, productName AS Product Name, reference AS Reference, brand AS Brand, description AS Description
FROM Products;

-- add product to Products table
INSERT INTO Products (productName, reference, brand, description)
VALUES (:productNameInput, :referenceInput, :brandInput, :descriptionInput);


-------------------------------------------------------
-- WorkOrders Page
-------------------------------------------------------

-- Display a join of WorkOrders, Machines, and Locations WorkOrders page
-- shows a more complete description of each work order
SELECT WorkOrders.workOrderId AS Order Id, 
       Machines.model AS Machine Model, 
       Machines.serial AS Machine Serial, 
       Locations.locationName AS Location Name, 
       WorkOrders.date AS Date, 
       WorkOrders.description AS Description
FROM WorkOrders 
INNER JOIN Machines ON WorkOrders.machineId = Machines.machineId 
INNER JOIN Locations ON WorkOrders.locationId = Locations.locationId;

-- create new work order
INSERT INTO WorkOrders (machineId, locationName, date, description)
VALUES (
  (SELECT machineId FROM Machines WHERE serial = :machineSerialInput),
  :locationNameInput,
  :dateInput,
  :descriptionInput
);

-- update existing work order
UPDATE WorkOrders 
SET machineId = (SELECT machineId FROM Machines WHERE serial = :machineSerialInput), 
locationName = :locationNameInput, 
date = :dateInput, 
description= :descriptionInput 
WHERE workOrderId = :workOrderId_from_the_update_form;

-- Delete work order in WorkOrder Table
DELETE FROM WorkOrders WHERE workOrderId = :workOrderId_from_the_update_form;

-- populate machineSerial dropdown
SELECT machineId from Machines;

-- populate locationName dropdown
SELECT locationId from Locations;


-------------------------------------------------------
-- Work Order Details Page
-------------------------------------------------------

-- display products associated with work order
-- the current UI displays examples with workOrderId == 1, 2, 8
SELECT Products.productName AS Product Name, Products.productReference AS Product Reference
    FROM WorkOrderProducts
    JOIN Products ON WorkOrderProducts.productId = Products.productId
    WHERE WorkOrderProducts.workOrderId = :workOrderId_from_input;

-- display mechanics associated with work order
-- the current UI displays examples with workOrderId == 1, 2, 8
SELECT Mechanics.firstName AS Mechanic First Name, Mechanics.lastName AS Mechanic Last Name
    FROM WorkOrderMechanics
    JOIN Mechanics ON WorkOrderMechanics.mechanicId = Mechanics.mechanicId
    WHERE WorkOrderMechanics.workOrderId = :workOrderId_from_input;

-- add product to work order (M-to-M relationship addition)
INSERT INTO WorkOrderProducts (workOrderId, productId) VALUES (:workOrderId_from_input, :productId_from_input);

-- delete product from work order (M-to-M relationship deletion)
DELETE FROM WorkOrderProducts WHERE workOrderId = :workOrderId_from_the_update_form AND (SELECT productId FROM Products WHERE reference = :referenceInput);

-- add mechanic to work order (M-to-M relationship addition)
INSERT INTO WorkOrderMechanics (workOrderId, mechanicId)
VALUES ((SELECT workOrderId FROM WorkOrders WHERE workOrderId = :workOrderId_from_the_update_form),
        (SELECT mechanicId FROM Mechanics WHERE email=:emailInput));

-- delete mechanic from work order (M-to-M relationship deletion)
DELETE FROM WorkOrderMechanics WHERE workOrderId = :workOrderId_from_the_update_form AND (SELECT mechanicId FROM Mechanics WHERE email=:emailInput);

-- update WorkOrderProducts (M-to-M relationship update)
UPDATE WorkOrderProducts SET productId = :productId_from_input WHERE workOrderId = :workOrderId_from_the_update_form AND productId = :productId_from_the_update_form;

-- populate productReference dropdown with ids
SELECT productId from Products;

-- populate mechanicEmail dropdown with ids
SELECT mechanicId from Mechanics;


-------------------------------------------------------
-- Work Order Products Detial Page
-------------------------------------------------------

-- display products associated with work order
-- the current UI displays examples with workOrderId == 1, 2, 8
SELECT Products.productName AS Product Name, Products.productReference AS Product Reference
    FROM WorkOrderProducts
    JOIN Products ON WorkOrderProducts.productId = Products.productId
    WHERE WorkOrderProducts.workOrderId = :workOrderId_from_input;

-- delete product from work order (M-to-M relationship deletion)
DELETE FROM WorkOrderProducts WHERE workOrderId = :workOrderId_from_the_update_form AND (SELECT productId FROM Products WHERE reference = :referenceInput);

-- add product to work order (M-to-M relationship addition)
INSERT INTO WorkOrderProducts (workOrderId, productId) VALUES (:workOrderId_from_input, :productId_from_input);

-- update WorkOrderProducts (M-to-M relationship update)
UPDATE WorkOrderProducts SET productId = :productId_from_input WHERE workOrderId = :workOrderId_from_the_update_form AND productId = :productId_from_the_update_form;

-------------------------------------------------------
-- Work Order Mechanics Detial Page
-------------------------------------------------------

-- display mechanics associated with work order
-- the current UI displays examples with mechanicId == 1, 2, 8
SELECT Mechanics.firstName AS Mechanic First Name, Mechanics.lastName AS Mechanic Last Name
    FROM WorkOrderMechanics
    JOIN Mechanics ON WorkOrderMechanics.mechanicId = Mechanics.mechanicId
    WHERE WorkOrderMechanics.workOrderId = :workOrderId_from_input;
   
-- delete mechanic from work order (M-to-M relationship deletion)
DELETE FROM WorkOrderMechanics WHERE workOrderId = :workOrderId_from_the_update_form AND (SELECT mechanicId FROM Mechanics WHERE email=:emailInput);

-- add mechanic to work order (M-to-M relationship addition)
INSERT INTO WorkOrderMechanics (workOrderId, mechanicId) VALUES (:workOrderId_from_input, :mechanicId_from_input);
