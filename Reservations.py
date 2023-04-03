#Book Reservation
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from helper import *
from report_backend import *
from globals import CONNECTION_STRING
 
engine = create_engine(CONNECTION_STRING, echo=True)

def FindBookTitle(AccessionNo):
    with engine.connect() as conn:
        query = f"SELECT Title \
        FROM Books\
        WHERE (Books.AccessionID = \"{AccessionNo}\")"

        result = conn.execute(query).fetchall()

        return result[0][0]

def FindMemberName(MemberID):
    with engine.connect() as conn:
        query = f"SELECT Name \
        FROM Members\
        WHERE (MemberID=\"{MemberID}\")"

        result = conn.execute(query).fetchall()

        return result[0][0]


def ReservationFunction(AccessionNumber, MemberID, ReserveDate):
    MaxReservations = 2
    ReservationValid = True
    with engine.connect() as conn:
        if not book_on_loan(AccessionNumber):
            return -3

        elif outstanding_fines(MemberID):
            return -1
 
        #Select latest record with AccessionNumber
        ReservationsQuery = f"SELECT * \
                FROM ReserveRecords\
                WHERE MemberID= '{MemberID}'"
 
        result = conn.execute(ReservationsQuery).fetchall()
 
        if len(result) >= MaxReservations:
            return -2
 
 
        if ReservationValid:
            #create row in reservations(AccessionNumber, ReserveDate, MemberID)
            reservation_query = f"INSERT INTO ReserveRecords VALUES ('{MemberID}', '{AccessionNumber}', '{ReserveDate}') "
            conn.execute(reservation_query)
            return 1
     
        else:
            return False
            
def book_is_reserved_by(accession_id,MemberID):
    query = f"SELECT MemberID FROM ReserveRecords WHERE AccessionID=\"{accession_id}\" AND MemberID = '{MemberID}'"

    with engine.connect() as conn:
        reserve_records = conn.execute(query).fetchall()

    return len(reserve_records) > 0
 


def cancelReservation(AccessionNumber,MemberID):
    with engine.connect() as conn:
        if book_is_reserved_by(AccessionNumber, MemberID):
        #delete latest entry in reservations with (AccessionNumber,MemberID)
            query = f"DELETE FROM reserveRecords \
            WHERE AccessionID='{AccessionNumber}' AND MemberID='{MemberID}'"
            conn.execute(query)
            return 1

        else: 
            return -1


# def BookSearch(word, attribute):
#     #Left Join authorBook, Author and Book
#     with engine.connect() as conn:
#         #joint table with all columns avail
#         JointQuery = f"SELECT Books.AccessionID, Books.Title, Books.ISBN, Books.Publisher, Books.PublishYear, Authors.Name \
#         FROM AuthorBook \
#         INNER JOIN AuthorsON \
#         Authors.AuthorID = AuthorBook.AuthorID \
#         INNER JOIN Books ON \
#         AuthorBook.AccessionID = Books.AccessionID \
#         WHERE ({attribute} LIKE '%{word} %' OR {attribute} LIKE '{word} %' OR {attribute} LIKE '{word}')"

#         Joint = conn.execute(JointQuery).fetchall()

#     output = retrieve_authors(Joint)
#     for row in output:
#         print(row)
        

    
def FinePaymentFunction(MemberID, PaymentDate, PaymentAmt):
    #select borrowingRecords
    #where MemberId = MemberID
    #check for latest open fine record
    with engine.connect() as conn:
        if outstanding_fines(MemberID):
            if outstanding_fines(MemberID) == int(PaymentAmt):
                UpdateFineQuery = f"UPDATE BorrowBy \
                SET PaidDate = '{PaymentDate}'\
                WHERE MemberID= '{MemberID}' AND PaidDate IS NULL AND FineAmount > 0"
                #fine = 
                conn.execute(UpdateFineQuery)
                return 1

            else:
                return -2

        else:
            return -1

