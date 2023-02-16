-- Group 39
-- Team Members: Juan Pablo Duque Ochoa, Marco Scandroglio
-- Project Name: Hello Earth!
-- Project Step 2 Draft: Normalized Schema + DDL with Sample Data 

SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

-- Table Machines

CREATE OR REPLACE TABLE Machines (
    machineId int NOT NULL UNIQUE AUTO_INCREMENT,
    year year NOT NULL,
    make varchar(45) NOT NULL,
    model varchar(45) NOT NULL,
    serial varchar(255) NOT NULL,
    class varchar(45) NOT NULL,
    PRIMARY KEY (machineId)
);

-- Table Mechanics

CREATE OR REPLACE TABLE Mechanics (
    mechanicId int NOT NULL UNIQUE AUTO_INCREMENT,
    firstName varchar(255) NOT NULL,
    lastName varchar(255) NOT NULL,
    phone varchar(25) NOT NULL,
    email varchar(255) NOT NULL,
    PRIMARY KEY (mechanicId),
    CONSTRAINT full_name UNIQUE (firstName, lastName)
);

-- Table Products

CREATE OR REPLACE TABLE Products (
    productId int NOT NULL UNIQUE AUTO_INCREMENT,
    productName varchar(45) NOT NULL,
    reference varchar(45) NOT NULL,
    brand varchar(45) NOT NULL,
    description TEXT,
    PRIMARY KEY (productId)
);

-- Table Locations

CREATE OR REPLACE TABLE Locations (
    locationId int NOT NULL UNIQUE AUTO_INCREMENT,
    locationName varchar(45) NOT NULL,
    address varchar(255) NOT NULL,
    zipcode varchar(45) NOT NULL,
    state varchar(45) NOT NULL,
    isClientLocation TINYINT NOT NULL,
    PRIMARY KEY (locationId)
);

-- Table WorkOrders

CREATE OR REPLACE TABLE WorkOrders (
    workOrderId int NOT NULL UNIQUE AUTO_INCREMENT,
    machineId int NOT NULL,
    locationId int,
    date DATE NOT NULL,
    description TEXT,
    PRIMARY KEY (workOrderId),
    FOREIGN KEY (machineId) REFERENCES Machines(machineId) ON DELETE CASCADE,
    FOREIGN KEY (locationId) REFERENCES Locations(locationId) ON DELETE SET NULL
);

-- Intersection table between Mechanics and WorkOrders (WorkOrderMechanics)

CREATE OR REPLACE TABLE WorkOrderMechanics (
    workOrderMechanicId int NOT NULL AUTO_INCREMENT,
    workOrderId int NOT NULL,
    mechanicId int,
    PRIMARY KEY (workOrderMechanicId),
    FOREIGN KEY (mechanicId) REFERENCES Mechanics(mechanicId) ON DELETE SET NULL,
    FOREIGN KEY (workOrderId) REFERENCES WorkOrders(workOrderId) ON DELETE CASCADE
);

-- Intersection table between Products and WorkOrders (WorkOrderProducts)

CREATE OR REPLACE TABLE WorkOrderProducts (
    workOrderProductId int NOT NULL AUTO_INCREMENT,
    workOrderId int NOT NULL,
    productId int,
    PRIMARY KEY (workOrderProductId),
    FOREIGN KEY (productId) REFERENCES Products(productId) ON DELETE SET NULL,
    FOREIGN KEY (workOrderId) REFERENCES WorkOrders(workOrderId) ON DELETE CASCADE
);

-- Insert sample data on Machines

INSERT INTO Machines (year, make, model, serial, class)
VALUES (2010, "Liebherr", "R 317 Litronic", "1042-48528", "Tracked Excavator"),
(2017, "KOMATSU", "HD325-8", "50027", "Off-Highway Truck"),
(2020, "CATERPILLAR", "963K", "D8T49943", "Tracked Loader"),
(2001, "CATERPILLAR", "D6M", "3WN02456", "Bulldozer"),
(2001, "CATERPILLAR", "320C", "AKH01920", "Tracked Excavator"),
(2008, "CATERPILLAR", "320DL", "KGF02672", "Tracked Excavator"),
(2008, "INGERSOLL-RAND", "SD70", "168762", "Compactor"),
(1980, "CATERPILLAR", "D6D", "4X05964", "Bulldozer"),
(1982, "CATERPILLAR", "D6D", "75W02070", "Bulldozer");

-- Insert sample data on Mechanics

INSERT INTO Mechanics (firstName, lastName, phone, email)
VALUES ("Bryan", "Cook", "+16945702087", "bryan.cook@gmail.com"),
("Maverick", "Ruiz", "+1-432-416-1915", "maverick.ruiz@gmail.com"),
("Clark", "Bennet", "(742) 757-1004 4662", "clark.bennet@gmail.com"),
("John", "Williams", "(962) 857-1021 4889", "johnhappy@hotmail.com"),
("Adam", "Edison", "(956)320-1080 4335", "edisonjr@outlook.com"),
("Robert", "Schalke", "645-867-5309 5309", "robschal@yahoo.com");

-- Insert sample data on Products

INSERT INTO Products (productName, reference, brand, description)
VALUES ('Lubricant X', 'REF001', 'Brand A', 'High-quality lubricant for earth moving machinery'),
('Grease Y', 'REF002', 'Brand B', 'Special grease for heavy-duty earth moving equipment'),
('Spare Part Z', 'REF003', 'Brand C', 'Genuine spare part for earth moving machinery maintenance'),
('Hydraulic filter', 'P164381', 'Donaldson', 'Hydraulic filter for compactors'),
('Fuel filter', 'P551315', 'Donaldson', 'Fuel filter for excavators and bulldozers'),
('Air filter', 'P532501', 'Donaldson', 'Air filter for excavators'),
('Hydraulic oil', 'HYDO10', 'Caterpillar', 'Hydraulic oil 6000+ hours extended life'),
('Motor oil', '15W40', 'Gulf', 'Motor multigrade oil');

-- Insert sample data on Locations

INSERT INTO Locations (locationName, address, zipcode, state, isClientLocation)
VALUES ('HelloEarth Depot 1', '123 Main Street', '12345', 'State A', 0),
('HelloEarth Depot 2', '456 Market Ave', '67890', 'State B', 0),
('HelloEarth Depot 3', '789 Ocean Blvd', '24680', 'State C', 0),
('Client Site 1', '725 Oakland Blvd', '24559', 'State C', 1),
('Client Site 2', '865 Park Ave', '25683', 'State E', 1),
('Client Site 3', '325 Sunrise Blvd', '24735', 'State F', 1),
('Client Site 4', '286 Market St', '24750', 'State T', 1);

-- Insert sample data on WorkOrders

INSERT INTO WorkOrders (machineId, locationId, date, description)
VALUES ((SELECT machineId FROM Machines WHERE make='Liebherr' AND model='R 317 Litronic'),
        (SELECT locationId FROM Locations WHERE locationName='Client Site 1'),
        '2023-02-07', 'Machine needs a general check-up'),
((SELECT machineId FROM Machines WHERE make='CATERPILLAR' AND model='963K'),
        (SELECT locationId FROM Locations WHERE locationName='HelloEarth Depot 1'),
        '2023-02-07', 'Machine needs an oil change'),
((SELECT machineId FROM Machines WHERE make='Liebherr' AND model='R 317 Litronic'),
        (SELECT locationId FROM Locations WHERE locationName='HelloEarth Depot 2'),
        '2023-02-08', 'Machine needs a new alternator'),
((SELECT machineId FROM Machines WHERE make='KOMATSU' AND model='HD325-8'),
        (SELECT locationId FROM Locations WHERE locationName='Client Site 1'),
        '2023-02-08', 'Machine needs a new starter'),
((SELECT machineId FROM Machines WHERE serial='3WN02456'),
        (SELECT locationId FROM Locations WHERE locationName='Client Site 2'),
        '2023-02-02', 'Perform 250-hour routine maintenance'),
((SELECT machineId FROM Machines WHERE serial='AKH01920'),
        (SELECT locationId FROM Locations WHERE locationName='Client Site 3'),
        '2023-01-20', 'Perform 1000-hour routine maintenance'),
((SELECT machineId FROM Machines WHERE serial='4X05964'),
        (SELECT locationId FROM Locations WHERE locationName='HelloEarth Depot 3'),
        '2023-01-15', 'Fix undercarriage issues'),
((SELECT machineId FROM Machines WHERE serial='KGF02672'),
        (SELECT locationId FROM Locations WHERE locationName='HelloEarth Depot 3'),
        '2023-01-03', 'Adjust boom'),
((SELECT machineId FROM Machines WHERE serial='168762'),
        NULL,
        '2022-12-15', 'Replace drum mounting pads');

-- Insert sample data on intersection table WorkOrderMechanics

INSERT INTO WorkOrderMechanics (workOrderId, mechanicId)
VALUES ((SELECT workOrderId FROM WorkOrders WHERE description='Machine needs a general check-up'),
        (SELECT mechanicId FROM Mechanics WHERE lastName='Cook')),
((SELECT workOrderId FROM WorkOrders WHERE description='Machine needs an oil change'),
        (SELECT mechanicId FROM Mechanics WHERE lastName='Bennet')),
((SELECT workOrderId FROM WorkOrders WHERE description='Machine needs a new alternator'),
        (SELECT mechanicId FROM Mechanics WHERE lastName='Cook')),
((SELECT workOrderId FROM WorkOrders WHERE description='Machine needs a new alternator'),
        (SELECT mechanicId FROM Mechanics WHERE lastName='Bennet')),
((SELECT workOrderId FROM WorkOrders WHERE description='Machine needs a new starter'),
        (SELECT mechanicId FROM Mechanics WHERE lastName='Ruiz')),
((SELECT workOrderId FROM WorkOrders WHERE description='Replace drum mounting pads'),
        (SELECT mechanicId FROM Mechanics WHERE lastName='Bennet')),
((SELECT workOrderId FROM WorkOrders WHERE description='Fix undercarriage issues'),
        (SELECT mechanicId FROM Mechanics WHERE lastName='Schalke')),
((SELECT workOrderId FROM WorkOrders WHERE description='Adjust boom'),
        (SELECT mechanicId FROM Mechanics WHERE lastName='Schalke')),
((SELECT workOrderId FROM WorkOrders WHERE description='Adjust boom'), NULL);       

-- Insert sample data on intersection table WorkOrderProducts

INSERT INTO WorkOrderProducts (workOrderId, productId)
VALUES ((SELECT workOrderId FROM WorkOrders WHERE description='Machine needs a general check-up'),
        (SELECT productId FROM Products WHERE reference='REF001')),
((SELECT workOrderId FROM WorkOrders WHERE description='Machine needs a general check-up'),
        (SELECT productId FROM Products WHERE reference='REF002')),
((SELECT workOrderId FROM WorkOrders WHERE description='Machine needs an oil change'),
        (SELECT productId FROM Products WHERE reference='REF001')),
((SELECT workOrderId FROM WorkOrders WHERE description='Machine needs a new alternator'),
        (SELECT productId FROM Products WHERE reference='REF003')),
((SELECT workOrderId FROM WorkOrders WHERE description='Machine needs a new starter'),
        (SELECT productId FROM Products WHERE reference='REF003')),
((SELECT workOrderId FROM WorkOrders WHERE description='Replace drum mounting pads'),
        (SELECT productId FROM Products WHERE reference='REF003')),
((SELECT workOrderId FROM WorkOrders WHERE description='Fix undercarriage issues'),
        (SELECT productId FROM Products WHERE reference='HYDO10')),
((SELECT workOrderId FROM WorkOrders WHERE description='Adjust boom'),
        (SELECT productId FROM Products WHERE reference='P164381')),
((SELECT workOrderId FROM WorkOrders WHERE description='Adjust boom'), NULL);

SET FOREIGN_KEY_CHECKS=1;
COMMIT;
