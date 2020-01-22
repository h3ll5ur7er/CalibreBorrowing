# Calibre borrowing system
## Motivation
SCS has many books. eBooks and books made from dead trees.
Until now to borrow a book it was necessary to tell/mail/call the A-Team so they can modify a Excel file to maintain an overview where each book is.
As some employees are not as conscientious many books are borrowd but not registered as such.
An easy to use system can save a lot of time and money.
- The A-Team does not have to manage a excel file
- If you are looking for a book, you know where to find it
- You don't have to to buy a new copy of a book that is already there but nobody knows where it is.

## Employee identification card
We are proud to present an employee identification card that can be used for borrowing books at the library and to borrow tools from the lab.

### Content
The content of the user indentification is `SCSUSER <FIRSTNAME> <LASTNAME>`

### Sticker
The professional P-Touch label printer located @ the automotion departement is capable of printing bar/qr codes.

### Card
A card can be ordered from \<whoever is  responsible for that\>

### Digital
You know how to generate a Bar/QR code isn't it?
Id not google it, there are websites and code for your programming language of choice...

### Future
If at some point SCS decides to add a vCard QR Code to the business card, this could be used aswell (some code changes required).

## Calibre
Calibre is a open source library management system.
It has a lot of interresting features:
- Conversion from and to the most common eBook formats
- Synchronisation of eBooks with eReaders (kindle, tolino,...)
- Integrated webservice to read, download, manage the library

### Setup
- Install calibre
- Add custom columns:
    - Preferences>Add your own columns>Add custom>Name:Borrowed, ColumnHeading:borrowed
    - Preferences>Add your own columns>Add custom>QuickCreate:ISBN
- Activate webservice (Preferences>Sharing over the web>Configure port, Configure autostart, Start server)

### Borrowing system
As an addition to the webservice accessable from the internal network under [http://bibliothek.scs-ad.scs.ch](http://bibliothek.scs-ad.scs.ch) a python application was created to:
- run on a raspberry pi
- be attached to a screen showing a list of all availbale books
- work with a barcode scanner to be able to scan books, user identification cards, ...

### Additional requirement
As SCS has multiple instances of some books (where the isbn is not unique obviously) there have to be control codes to tell the system what action to perform.

## Calibre Protocol

### Get all books
To get the first batch of metadata use:
`GET: BASE_URL/interface-data/books-init`

Until the response is empty use the following POST request to fetch another batch of metadata.
`POST: BASE_URL/interface-data/more-books?library_id=LIBRARY_NAME` with payload `{"offset":OFFSET,"query":"","sort":"timestamp","sort_order":"desc","vl":""}`

The books are listed under the metadata key.
The keys inside the metadata is the BOOK_ID used in other requests

### Make changes
To make changes in any column you have to be logged in as a user with write permission.
By design the SCS library does not have LDAP integration. All users inside the internal network have read access to the library. There is one account with write access used by the borrowing system.

```
username: library
password: $om3V3ry$3cur3P@$$w0rd
```

`POST: BASE_URL/cdb/set-fields/BOOK_ID/LIBRARY_NAME` with payload `{"changes":{"COLUMN_NAME":VALUE}}`

To borrow a book the custom column is called `#borrowed` and the value is a list of names separated by a `&` character.

