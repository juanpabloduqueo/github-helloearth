-- Group 39
-- Team Members: Juan Pablo Duque Ochoa, Marco Scandroglio
-- Project Name: Hello Earth!
-- Project Step 3 Draft Version: Design HTML Interface + DML SQL (Group / On Ed Discussion ) 

-- Database Manipulation queries organized by page

-------------------------------------------------------
-- Machines Page
-------------------------------------------------------

-- Display Machines table on Machines page
SELECT * FROM Machines;

-- Add machine to Machines table
INSERT INTO Machines (year, make, model, serial, class) 
VALUES (:yearInput, :makeInput, :modelInput, :serialInput, :classInput);

-- Update Machine in Machines Table
UPDATE Machines SET year = :yearInput, make = :makeInput, model = :modelInput, serial = :serialInput, class = :classInput WHERE id= :machine_ID_from_the_update_form;


-------------------------------------------------------
-- Locations Page
-------------------------------------------------------

-- Display Locations table on Locations page
SELECT * FROM Locations;

-- add location to Locations table
INSERT INTO Locations (locationName, address, zipcode, state, isClientLocation)
VALUES (:locationNameInput, :addressInput, :zipcodeInput, :stateInput, :isClientLocationInput);


-------------------------------------------------------
-- Mechanics Page
-------------------------------------------------------

-- Display Mechanics table on Mechanics page
SELECT * FROM Mechanics;

-- add mechanic to Mechanics table
INSERT INTO Mechanics (firstName, lastName, phone, email)
VALUES (:firstNameInput, :lastNameInput, :phoneInput, :emailInput);


-------------------------------------------------------
-- Products Page
-------------------------------------------------------

-- Display Products table on Products page
SELECT * FROM Products;

-- add product to Products table
INSERT INTO Products (productName, reference, brand, description)
VALUES (:productNameInput, :referenceInput, :brandInput, :descriptionInput);


-------------------------------------------------------
-- WorkOrders Page
-------------------------------------------------------

-- Display a join of WorkOrders, Machines, and Locations WorkOrders page
-- shows a more complete description of each work order
SELECT WorkOrders.workOrderId, 
       Machines.model AS machineModel, 
       Machines.serial AS machineSerial, 
       Locations.locationName, 
       WorkOrders.date, 
       WorkOrders.description
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

-- populate machineSerial dropdown
SELECT machineId from Machines;

-- populate locationName dropdown
SELECT locationId from Locations;

-- populate productReference dropdown
SELECT productId from Products;

-- populate mechanicEmail dropdown
SELECT mechanicId from Mechanics;

-- sample insert into WorkOrders
INSERT INTO WorkOrders (machineId, locationId, date, description)
VALUES (
  (SELECT machineId FROM Machines WHERE serial = "50027"),
  (SELECT locationId FROM Locations WHERE locationName = "Client Site 2"),
  "2023-02-24",
  "Machine needs an oil change"
);

-- add product to work order (M-to-M relationship addition)
INSERT INTO WorkOrderProducts (workOrderId, productId) VALUES (workOrderId_from_input, :productId_from_input);

-- sample addition of product
INSERT INTO WorkOrderProducts (workOrderId, productId)
VALUES ((SELECT workOrderId FROM WorkOrders WHERE workOrderId = 10),
        (SELECT productId FROM Products WHERE reference = "15W40"));

-- delete product from work order
DELETE FROM WorkOrderProducts WHERE workOrderId = :workOrderId_from_the_update_form AND (SELECT productId FROM Products WHERE reference = :referenceInput);

-- sample delete product from work order
DELETE FROM WorkOrderProducts WHERE workOrderId = 10 AND (SELECT productId FROM Products WHERE reference = "15W40");

-- add mechanic to work order (M-to-M relationship addition)
INSERT INTO WorkOrderMechanics (workOrderId, mechanicId)
VALUES ((SELECT workOrderId FROM WorkOrders WHERE workOrderId = :workOrderId_from_the_update_form),
        (SELECT mechanicId FROM Mechanics WHERE email=:emailInput));

-- sample add mechanic to work order
INSERT INTO WorkOrderMechanics (workOrderId, mechanicId)
VALUES (11, (SELECT mechanicId FROM Mechanics WHERE email="edisonjr@outlook.com"));

-- delete mechanic from work order (M-to-M relationship deletion)
DELETE FROM WorkOrderMechanics WHERE workOrderId = :workOrderId_from_the_update_form AND (SELECT mechanicId FROM Mechanics WHERE email=:emailInput);


-- sample delete mechanic from work order
DELETE FROM WorkOrderMechanics WHERE workOrderId = 11 AND (SELECT mechanicId FROM Mechanics WHERE email="edisonjr@outlook.com");
