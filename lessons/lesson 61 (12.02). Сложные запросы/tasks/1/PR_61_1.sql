DROP TABLE Orders;
DROP TABLE Customers;

CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
	LastName TEXT NOT NULL,
	Email TEXT NOT NULL
);

CREATE TABLE Orders (
	OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER,
    OrderDate TEXT CHECK (OrderDate LIKE DATE(OrderDate)),
    TotalAmount REAL,
	FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
INSERT INTO Customers (CustomerID, FirstName, LastName, Email) VALUES
    ('1', 'John', 'Doe', 'johndoe@example.com'),
    ('2', 'Jane', 'Smith', 'janesmith@example.com');

INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES
	(101, 1, "2025-02-01", 100.50),
    (102, 2, "2025-02-02", 200.75);
	
--SELECT
--    Customers.FirstName,
--    Customers.LastName,
--    Orders.OrderID,
--   Orders.TotalAmount
--FROM Customers
--JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

--SELECT
--    Customers.FirstName,
--    Customers.LastName,
--    Orders.OrderID,
--    Orders.TotalAmount
--FROM Customers
--LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

SELECT OrderID, Orders.CustomerID, OrderDate, TotalAmount
FROM Orders;
EXCEPT
SELECT OrderID, Orders.CustomerID, OrderDate, TotalAmount
FROM Orders;
LEFT JOIN Customers ON Orders.CustomerID = Customers.CustomerID WHERE Customers.CustomerID IS NULL;