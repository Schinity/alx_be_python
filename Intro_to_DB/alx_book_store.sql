CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(author_id),
    price DOUBLE NOT NULL,
    publication_date DATE NOT NULL
);

CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL,
    address TEXT NOT NULL
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE Order_Details (
    orderdetails_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity DOUBLE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);