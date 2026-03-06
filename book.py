import csv

def add_book(title,author):
    with open("books.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([title,author])

def view_books():
    books = []
    try:
        with open("books.csv","r") as file:
            reader = csv.reader(file)
            for row in reader:
                books.append(row)
    except:
        pass
    return books