create database library;
use library;

create table Authors (
    AuthorID integer NOT NULL AUTO_INCREMENT,
    Name varchar(30) UNIQUE,
    primary key (AuthorID)
);

create table Books (
    AccessionID	varchar(10) not null,
    ISBN varchar(20),
    Title varchar(100),
    Publisher varchar(100),
    PublishYear numeric(4) CHECK (PublishYear > 0),
    Primary key(AccessionID)
    -- Foreign key(ISBN) references AuthorBook(ISBN)
);

create table AuthorBook (
    AuthorID integer,
    AccessionID varchar(10) not null,
    primary key (AccessionID, AuthorID),
    foreign key (AuthorID)
        references Authors(AuthorID)
        ON UPDATE CASCADE ON DELETE CASCADE,
    foreign key (AccessionID)
        references Books(AccessionID)
        ON UPDATE CASCADE ON DELETE CASCADE
);	

CREATE TABLE Members (
    MemberID VARCHAR(10) NOT NULL,
    Name VARCHAR(30) CHECK (LENGTH(Name) > 0),
    Faculty VARCHAR(25) NOT NULL CHECK (LENGTH(Faculty) > 0),
    PhoneNumber NUMERIC(8) CHECK (LENGTH(PhoneNumber) = 8),
    Email VARCHAR(50) CHECK (Email LIKE '%@%'),
    PRIMARY KEY(MemberID)
);

CREATE TABLE ReserveRecords (
    MemberID VARCHAR(5) NOT NULL,
    AccessionID VARCHAR(45) NOT NULL,
    ReserveDate DATE,
    FOREIGN KEY (MemberID)
        REFERENCES Members(MemberID)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (AccessionID)
        REFERENCES Books(AccessionID)
        ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY (MemberID, AccessionID, ReserveDate)
);

CREATE TABLE BorrowBy (
    SessionID integer NOT NULL AUTO_INCREMENT,
    MemberID VARCHAR(45) NOT NULL,
    AccessionID VARCHAR(45) NOT NULL,
    BorrowDate DATE,
    DueDate DATE AS (DATE_ADD(BorrowDate, INTERVAL 14 DAY)),
    ReturnDate DATE,
    FineAmount DECIMAL AS (DATEDIFF(ReturnDate, DueDate)),
    PaidDate DATE,
    FOREIGN KEY (MemberID)
        REFERENCES Members(MemberID)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (accessionID)
        REFERENCES Books(accessionID)
        ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY (SessionID)
);



INSERT INTO Members (MemberID, name, Faculty, PhoneNumber, Email)
VALUES
('A101A', 'Hermione Granger', 'Science', '33336663', 'flying@als.edu'),
('A201B', 'Sherlock Holmes', 'Law', '44327676', 'elementarydrw@als.edu'),
('A301C', 'Tintin', 'Engineering', '14358788', 'luvmilu@als.edu'),
('A401D', 'Prinche Hamlet', 'FASS', '16091609', 'tobeornot@als.edu'),
('A5101E', 'Willy Wonka', 'FASS', '19701970', 'choco1@als.edu'),
('A601F', 'Holly Golightly', 'Business', '55548008', 'diamond@als.edu'),
('A701G', 'Raskolnikov', 'Law', '18661866', 'oneaxe@als.edu'),
('A801H', 'Patrick Bateman', 'Business', '38548544', 'mice@als.edu'),
('A901I', 'Captain Ahab', 'Science', '18511851', 'wwhale@als.edu');
