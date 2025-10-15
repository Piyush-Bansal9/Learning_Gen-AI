CREATE TABLE orders(
    id INT PRIMARY KEY,
    dateOforder DATE,
    custId int,
    FOREIGN KEY(custId) references customer(id)
)


ALTER TABLE orders
CHANGE COLUMN id idx INT PRIMARY KEY


ALTER TABLE orders
RENAME TO ord




