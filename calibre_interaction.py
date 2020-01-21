from requests.auth import HTTPDigestAuth
from requests import get as _get
from requests import post as _post
from calibre_credentails import *
from pprint import pprint

 
def get(url, *a, **kw):
    return _get(url, *a, auth=HTTPDigestAuth(USERNAME, PASSWORD), **kw)

def post(url, payload, *a, **kw):
    return _post(url, *a, json=payload, auth=HTTPDigestAuth(USERNAME, PASSWORD), **kw)

def get_books():
    data = {}
    resp = get(BASE_URL + "/interface-data/books-init")
    data.update(resp.json()["metadata"])
    while resp.status_code == 200:
        payload = {"offset":len(data),"query":"","sort":"timestamp","sort_order":"desc","vl":""}
        resp = post(BASE_URL + "/interface-data/more-books?library_id="+LIBRARY_NAME, payload)
        metadata = resp.json()["metadata"]
        data.update(metadata)
        if len(metadata) == 0:
            break
    data = {k:v for k,v in sorted(data.items(), key=lambda x:int(x[0]))}
    return data
    
def list_books():
    meta = get_books()
    cols = [5, 75, 35, 15]
    print(f'{"id".center(cols[0])}|{"title".center(cols[1])}|{"author".center(cols[2])}|{"borrowed by".center(cols[3])}')
    print(f'{"-"*cols[0]}+{"-"*cols[1]}+{"-"*cols[2]}+{"-"*cols[3]}')
    for book_id in meta:
        book = meta[book_id]
        print(f'{str(book_id).center(cols[0])}|{book.get("title", "")[:cols[1]].center(cols[1])}|{book.get("author_sort", "")[:cols[2]].center(cols[2])}|{book.get("#borrowed", "")[:cols[3]].center(cols[3])}')

def get_book_by_isbn(isbn):
    books = get_books()
    matches = [k for k, v in books.items() if v.get("#isbn", None) == isbn]
    if len(matches) == 0:
        return None
    return matches[0], books[matches[0]]

def change_borrower(book_id, borrower):
    resp = post(BASE_URL + f"/cdb/set-fields/{book_id}/{LIBRARY_NAME}",
                {"changes":{"#borrowed":str(borrower)}})

def download(book_id, format):
    def get_filename(response):
        cd = response.headers.get('content-disposition')
        if not cd:
            return None
        import re
        fname = re.findall('filename="([^"]+)', cd)
        if len(fname) == 0:
            return None
        return fname[0]

    resp = get(BASE_URL + f"/get/{format}/{book_id}/{LIBRARY_NAME}", allow_redirects=True)
    fn = get_filename(resp)
    with open(fn, "wb") as f:
        f.write(resp.content)
    print(fn)

def main():
    from sys import argv
    args = argv[1:]
    if len(args) == 0:
        print("usage: ")
        exit(1)
    
    if "list" == args[0]:
        list_books()
    if "borrow" == args[0]:
        change_borrower(args[1], args[2])
    if "download" == args[0]:
        download(args[1], "AZW3")

if __name__ == "__main__":
    main()
