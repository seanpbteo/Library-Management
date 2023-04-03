from sqlalchemy import create_engine
from globals import CONNECTION_STRING

engine = create_engine(CONNECTION_STRING, echo=True)

# To get details for one entry
def get_details(query):
    with engine.connect() as conn:
        res = conn.execute(query).mappings().all()

    print("\n")
    print(res)
    print("\n")

    return res[0]
    
def book_in_library(accession_id):
    query = f"SELECT * FROM Books WHERE AccessionID=\"{accession_id}\"" 

    with engine.connect() as conn:
        res = conn.execute(query).fetchall()

    return len(res) > 0

def book_on_loan(accession_id):
    query = f"SELECT ReturnDate FROM BorrowBy WHERE AccessionID=\"{accession_id}\" ORDER BY BorrowDate"

    with engine.connect() as conn:
        res = conn.execute(query).fetchall()

    return res[-1][0] == None if len(res) > 0 else False

def book_next_available_date(accession_id):
    query = f"SELECT DueDate FROM BorrowBy WHERE AccessionID=\"{accession_id}\" ORDER BY BorrowDate"

    with engine.connect() as conn:
        res = conn.execute(query).fetchall()

    return res[-1][0] if res[-1][0] != None else "further notice"

# list of (str) author names -> add to Author table
def add_authors(authors):
    with engine.connect() as conn:
        for author_name in authors:
            query = f"INSERT IGNORE INTO Authors (Name) VALUES (\"{author_name}\")"
            conn.execute(query)

# list of (str) author names -> list of (int) author IDs
def get_author_ids(authors):
    list_of_author_ids = []
    with engine.connect() as conn:
        for author_name in authors:
            query = f"SELECT AuthorID FROM Authors WHERE Name=\"{author_name}\""
            res = conn.execute(query).fetchall()
            list_of_author_ids.append(res[0][0])

    return list_of_author_ids

def book_is_reserved(accession_id):
    query = f"SELECT MemberID FROM ReserveRecords WHERE AccessionID=\"{accession_id}\""

    with engine.connect() as conn:
        reserve_records = conn.execute(query).fetchall()

    return len(reserve_records) > 0

def next_reserver(accession_id):
    query = f"SELECT MemberID FROM ReserveRecords WHERE AccessionID=\"{accession_id}\" ORDER BY ReserveDate"

    with engine.connect() as conn:
        reserve_records = conn.execute(query).fetchall()

    return reserve_records[0][0] if len(reserve_records) > 0 else ""

def get_num_of_borrowed_books(member_id):
    query = f"SELECT * FROM BorrowBy WHERE (MemberID=\"{member_id}\" AND ReturnDate IS NULL)"
    
    with engine.connect() as conn:
        curr_borrowed = conn.execute(query).fetchall()

    return len(curr_borrowed)

# (str) member_id -> (bool) if fines exist, whether they have a paid date
def outstanding_fines(member_id):
    query = f"SELECT SUM(FineAmount) FROM BorrowBy WHERE (\
        MemberID=\"{member_id}\" AND \
        PaidDate IS NULL \
        AND FineAmount > 0)"

    with engine.connect() as conn:
        total_fines = (conn.execute(query).fetchall())[0][0]

    return total_fines
