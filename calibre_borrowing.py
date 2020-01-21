from tkinter import *
from tkinter import ttk
from tk_table import Table
from tk_keyboard_listener import KeyboardListener

from time import time
from calibre_transaction_manager import TransactionManager
from calibre_interaction import get_books, change_borrower, get_book_by_isbn

from calibre_config import BORROWER_SEPPARATOR, COLUMNS, COLUMN_NAMES, FULLSCREEN


window = Tk()
if FULLSCREEN:
    window.attributes("-fullscreen", True)
window.title("SCS Library")

tab_list = Table(window)
tab_list.set_columns(COLUMNS)
tab_list.set_names(COLUMN_NAMES)
tab_list.refresh(get_books())
tab_list.pack(expand=YES, fill=BOTH)


def do_borrow(name, isbn):
    book_id, book = get_book_by_isbn(isbn)
    if book_id is not None:
        print(f"{name} borrowed {book.get('title', '')}")
        borrowers = set([b for b in book.get('#borrowed', "").split(BORROWER_SEPPARATOR) if b != "" ])
        borrowers.add(name)
        change_borrower(book_id, BORROWER_SEPPARATOR.join(borrowers))
        tab_list.refresh(get_books())


def do_return(name, isbn):
    book_id, book = get_book_by_isbn(isbn)
    print(f"{name} returned {book.get('title', '')}")
    if book_id is not None:
        borrowers = set([b for b in book.get('#borrowed', "").split(BORROWER_SEPPARATOR) if b != "" ])
        if name in borrowers:
            borrowers.remove(name)
        change_borrower(book_id, BORROWER_SEPPARATOR.join(borrowers))
        tab_list.refresh(get_books())


def visualize_command():
    print("command set")

def visualize_name():
    print("name set")

def visualize_isbn():
    print("isbn set")

def reset_visualization():
    print("transaction reset")


transaction_manager = TransactionManager(do_borrow, do_return, visualize_command, visualize_name, visualize_isbn, reset_visualization)
keyboard = KeyboardListener(window, transaction_manager.on_enter_pressed)

window.mainloop()
