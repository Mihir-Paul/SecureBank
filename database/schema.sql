CREATE TABLE admins(
    admin_id INT PRIMARY KEY,
    username VARCHAR(30) NOT NULL UNIQUE,
    password_hash VARCHAR(100) NOT NULL,
    full_name VARCHAR(100) ,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE customers(
    customer_id INT PRIMARY key,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) UNIQUE,
    email VARCHAR(100) UNIQUE NOT NULL,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE accounts(
    account_number BIGINT PRIMARY KEY,
    customer_id INT NOT NULL,
    account_type ENUM('savings','current') NOT NULL,
    balance DECIMAL(12,2) DEFAULT 0.00,
    pin_hash VARCHAR(255) NOT NULL,
    status ENUM('Active','Blocked') DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE transactions(
    transaction_id INT PRIMARY KEY,
    account_number BIGINT NOT NULL,
    transaction_type ENUM('Deposit','Withdraw','Transfer') NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    description VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_number) REFERENCES accounts(account_number)
);