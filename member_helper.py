from random import randint
from globals import CONNECTION_STRING
from sqlalchemy import create_engine
from helper import outstanding_fines

def id_generator():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = alphabet[randint(0,25)] + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + alphabet[randint(0,25)]
    return output
def add_new_member(id, name, faculty, pn, email):
    with engine.connect() as conn:
        ins_query = f"INSERT INTO Members VALUES ('{id}', '{name}', '{faculty}', '{pn}', '{email}')"
        try:
            conn.execute(ins_query)
            return 1
        except:
            return -1
           
 
def retrieve_member(id):
    with engine.connect() as conn:
        query = f"SELECT * FROM Members WHERE MemberID='{id}'"
        res = conn.execute(query).fetchone()
        return res

def outstanding_books(id):
    with engine.connect() as conn:
        query = f"SELECT * FROM borrowby WHERE MemberID='{id}' AND ReturnDate IS NULL"
        res = conn.execute(query).fetchall()
        return len(res)

def has_reserve(id):
    with engine.connect() as conn:
        query = f"SELECT * FROM reserverecords WHERE MemberID='{id}'"
        res = conn.execute(query).fetchall()
        return len(res)



def delete_member(id):
    with engine.connect() as conn:
        if outstanding_fines(id) == None and outstanding_books(id) == 0 and has_reserve(id) == 0:
            delete_query = f"DELETE FROM Members WHERE MemberID = '{id}'"
            try:
                conn.execute(delete_query)
                return 1
            except:
                return -1
        else:
            return -1
 
def update_member(id, name, faculty, pn, email):
    with engine.connect() as conn:
        update_query = f"UPDATE Members \
         SET Name = \"{name}\", Faculty = \"{faculty}\", PhoneNumber = \"{pn}\", Email = \"{email}\" \
         WHERE (MemberID=\"{id}\")"
        try:
            conn.execute(update_query)
            return 1
        except:
            return -1
 


connection_string = CONNECTION_STRING
 
engine = create_engine(connection_string, echo=True)
