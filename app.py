import streamlit as st
from books import add_book, view_books
from borrow import borrow_book, return_book

st.title("Online Library Management System")

menu = ["Home","Add Book","View Books","Borrow Book","Return Book"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
    st.subheader("Welcome to Library System")

elif choice == "Add Book":
    title = st.text_input("Enter Book Title")
    author = st.text_input("Enter Author Name")

    if st.button("Add Book"):
        add_book(title,author)
        st.success("Book Added Successfully")

elif choice == "View Books":
    books = view_books()
    for book in books:
        st.write(book)

elif choice == "Borrow Book":
    name = st.text_input("Student Name")
    book = st.text_input("Book Name")

    if st.button("Borrow"):
        borrow_book(name,book)
        st.success("Book Borrowed Successfully")

elif choice == "Return Book":
    name = st.text_input("Student Name")
    book = st.text_input("Book Name")

    if st.button("Return"):
        return_book(name,book)
        st.success("Book Returned Successfully")