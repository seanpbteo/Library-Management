from sqlalchemy import create_engine
from helper import *
from globals import CONNECTION_STRING

engine = create_engine(CONNECTION_STRING, echo=True)

def book_borrowing(accession_id, member_id, borrow_date):
    for field in (accession_id, member_id, borrow_date):
        if field == "":
            raise Exception("Empty field")

    if not book_in_library(accession_id):
        raise Exception("Book does not exist")

    if book_on_loan(accession_id):
        raise Exception(f"Book on loan until {book_next_available_date(accession_id)}")

    if book_is_reserved(accession_id) and next_reserver(accession_id) != member_id:
        raise Exception("Book is reserved by someone else")

    if get_num_of_borrowed_books(member_id) >= 2:
        raise Exception("Member loan quota exceeded")

    if outstanding_fines(member_id):
        raise Exception("Member has outstanding fines")

    with engine.connect() as conn:
        borrow_query = f"INSERT INTO BorrowBy(MemberID, AccessionID, BorrowDate) \
                VALUES (\"{member_id}\", \"{accession_id}\", \"{borrow_date}\")"
        conn.execute(borrow_query)

    if next_reserver(accession_id) == member_id:
        delete_query = f"DELETE FROM ReserveRecords \
            WHERE MemberID='{member_id}' AND AccessionID='{accession_id}'"

        with engine.connect() as conn:
            conn.execute(delete_query)

def book_returning(accession_id, return_date):
    for field in (accession_id, return_date):
        if field == "":
            raise Exception("Empty field")

    if not book_on_loan(accession_id):
        raise Exception("Book is already in library")

    with engine.connect() as conn:
        return_query = f"UPDATE BorrowBy SET ReturnDate=\"{return_date}\" WHERE (AccessionID=\"{accession_id}\" AND ReturnDate IS NULL)"
        conn.execute(return_query)

        fines_query = f"SELECT FineAmount FROM BorrowBy WHERE AccessionID=\"{accession_id}\" ORDER BY ReturnDate"
        fines_res = conn.execute(fines_query).fetchall()

    if fines_res[-1][0] > 0:
        raise Exception("Book returned successfully but has fines")
