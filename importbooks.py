from csv import reader
from booksfunctions import *

with open('LibBooks.csv', newline='') as f:
    reader = reader(f)
    df = [tuple(row) for row in reader]
    books_table = df[1:]

for accession_id, title, author_1, author_2, author_3, isbn, publisher, year in books_table:
    authors = []
    for author in (author_1, author_2, author_3):
        if author == "":
            continue

        authors.append(author)

    book_acquisition(
        accession_id=accession_id,
        title=title,
        authors=authors,
        isbn=isbn,
        publisher=publisher,
        year=year
    )
