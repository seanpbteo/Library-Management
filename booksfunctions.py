from sqlalchemy import create_engine
from helper import *
from globals import CONNECTION_STRING

engine = create_engine(CONNECTION_STRING, echo=True)

def book_acquisition(accession_id, title, authors, isbn, publisher, year):
    for field in (accession_id, title, isbn, publisher, year):
        if field == "":
            raise Exception("Empty field")

    if authors == []:
        raise Exception("Empty field")

    if book_in_library(accession_id):
        raise Exception("Duplicate Accession ID")

    add_authors(authors)
    author_ids = get_author_ids(authors)

    with engine.connect() as conn:
        # based on function parameters, insert new book into Books table
        book_query = f"INSERT INTO Books (AccessionID, Title, ISBN, Publisher, PublishYear) \
            VALUES (\"{accession_id}\", \"{title}\", \"{isbn}\", \"{publisher}\", {year});"
        conn.execute(book_query)

        # for each author, get the author id and insert relationship into AuthorBook table
        for author_id in author_ids:
            authorbook_query = f"INSERT IGNORE INTO AuthorBook(AccessionID, AuthorID) VALUES(\"{accession_id}\", {author_id});"
            conn.execute(authorbook_query)

def book_withdrawal(accession_id):
    for field in (accession_id):
        if field == "":
            raise Exception("Empty field")

    if not book_in_library(accession_id):
        raise Exception("Book does not exist")

    if book_on_loan(accession_id):
        raise Exception("Book is currently on loan")

    if book_is_reserved(accession_id):
        raise Exception("Book is currently reserved")

    query = f"DELETE FROM Books WHERE AccessionID=\"{accession_id}\""

    with engine.connect() as conn:
        conn.execute(query)

def book_search(title, isbn, publisher, year, authors):
    
    """
    1. build search query to get the accession_id of the relevant books
    2. execute search query to get the accession_ids
    3. build results query to display the information for each accession_id
    4. execute results query and return dict of results
    """

    fields_str = []
    fields = ("Books.Title", "Books.ISBN", "Books.Publisher", "Books.PublishYear", "Authors.Name")
    values = (title, isbn, publisher, year, authors)

    for field, value, in zip(fields, values):
        if value == "" or value == 0:
            continue

        fields_str.append(f"{field} LIKE '{value}%%'" if field != "Book.PublishYear" \
                          else f"CAST({field} AS VARCHAR(4)) LIKE '{value}%%'")

    if fields_str == []:
        raise Exception("No search terms entered")

    fields_str = " AND ".join(fields_str)
    
    search_query = f"SELECT Books.AccessionID \
        FROM AuthorBook LEFT JOIN Books ON AuthorBook.AccessionID = Books.AccessionID \
        LEFT JOIN Authors ON AuthorBook.AuthorID = Authors.AuthorID \
        WHERE {fields_str}"

    with engine.connect() as conn:
        search_res = conn.execute(search_query).fetchall()

    search_res = [row[0] for row in search_res]
    search_str = []

    for accession_id in search_res:
        search_str.append(f"AuthorBook.AccessionID='{accession_id}'")

    if search_str == []:
        raise Exception("No such book")

    search_str = " OR ".join(search_str)

    results_query = f"SELECT Books.AccessionID, Books.Title, Books.ISBN, Books.Publisher, Books.PublishYear, \
        GROUP_CONCAT(Authors.Name) AS Authors \
        FROM AuthorBook LEFT JOIN Books ON AuthorBook.AccessionID = Books.AccessionID \
        LEFT JOIN Authors ON AuthorBook.AuthorID = Authors.AuthorID \
        WHERE {search_str} \
        GROUP BY AuthorBook.AccessionID"

    with engine.connect() as conn:
        res = conn.execute(results_query).mappings().all()

    return res
