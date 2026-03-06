import csv

def borrow_book(name,book):
    with open("borrow.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name,book])

def return_book(name,book):
    rows = []
    with open("borrow.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row != [name,book]:
                rows.append(row)

    with open("borrow.csv","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)