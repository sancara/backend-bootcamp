CREATE TABLE users(

    id PRIMARY KEY,
    name VARCHAR(20),
    last_name VARCHAR(20),
    email VARCHAR(50),
    country VARCHAR(10),
    cp VARCHAR(10),
    created_at DATETIME
        
);

DESC