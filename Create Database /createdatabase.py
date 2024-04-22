CREATE TABLE Books (
    BookID INTEGER PRIMARY KEY,
    Title TEXT,
    Author TEXT,
    YearPublished INTEGER,
    Genre TEXT
);


INSERT INTO Books (Title, Author, YearPublished, Genre)
VALUES 
    ('To Kill', 'Harper Lee', 1960, 'Fiction'),
    ('Do not leave me', 'George Orwell', 1949, 'Romance'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 2024, 'Drama');

SELECT * FROM Books;

SELECT * FROM Books WHERE YearPublished > 2000;

SELECT * FROM Books WHERE Genre = 'Fiction';

UPDATE Books SET YearPublished = 1984 WHERE Title = 'Do not leave me';
