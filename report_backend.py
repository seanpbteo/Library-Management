from sqlalchemy import create_engine
from globals import CONNECTION_STRING
# please change create_engine path
engine = create_engine(CONNECTION_STRING)


def retrieve_authors(books):
    dict = {}
    a = list(books)
    for b in a:
        book = tuple(b)
        book_isbn = book[2]
        author = book[5]
        if book_isbn not in dict:
            dict[book_isbn] = []
        dict[book_isbn].append(author)
    output = []
    for b in a:
        book = tuple(b)
        book_isbn = book[2]
        aut = str(dict[book_isbn])[1:-1]
        book = book[:5] + (aut,)
        output.append(book)
    # remove duplicates
    return [t for t in (set(tuple(i) for i in output))]


def show_books_on_reservation():
    with engine.connect() as conn:
        JointQuery = """
        SELECT reserveRecords.AccessionID, Books.Title, Members.MemberID, Members.name
        FROM reserveRecords
        INNER JOIN Books ON
        reserveRecords.AccessionID = Books.AccessionID
        INNER JOIN Members ON
        Members.MemberID = reserveRecords.MemberID"""
        books = conn.execute(JointQuery)
        return books


def members_with_fines():
    with engine.connect() as conn:
        JointQuery = """
        SELECT Members.MemberID, Members.Name, Members.Faculty, Members.PhoneNumber, Members.Email
        FROM Members
        INNER JOIN Borrowby ON
        Members.MemberID = Borrowby.MemberID
        WHERE Borrowby.FineAmount > 0 AND Borrowby.PaidDate IS NULL"""
        members = conn.execute(JointQuery)
    return members


def show_books_on_loan():
    with engine.connect() as conn:
        JointQuery = """SELECT Books.AccessionID, Books.Title, Books.ISBN, Books.Publisher, Books.PublishYear, Authors.name
        FROM AuthorBook
        INNER JOIN Authors ON
        Authors.AuthorID = AuthorBook.AuthorID
        INNER JOIN Books ON
        AuthorBook.AccessionID = Books.AccessionID
        INNER JOIN Borrowby ON
        Borrowby.AccessionID = Books.AccessionID
        WHERE (Borrowby.ReturnDate IS NULL)"""

        books = conn.execute(JointQuery)

    output = retrieve_authors(books)
    return output


def books_on_loan_by_member(memberid):
    with engine.connect() as conn:

        JointQuery = f"""SELECT Books.AccessionID, Books.Title, Books.ISBN, Books.Publisher, Books.PublishYear, Authors.name
        FROM AuthorBook
        INNER JOIN Authors ON
        Authors.AuthorID = AuthorBook.AuthorID
        INNER JOIN Books ON
        AuthorBook.AccessionID = Books.AccessionID
        INNER JOIN Borrowby ON
        Borrowby.AccessionID = Books.AccessionID
        WHERE (Borrowby.ReturnDate IS NULL AND Borrowby.MemberID = '{memberid}')"""

        books = conn.execute(JointQuery)

    output = retrieve_authors(books)
    return output
