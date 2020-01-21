# SELECTOR = "REMOTE"
SELECTOR = "LOCAL"

if SELECTOR == "REMOTE":
    USERNAME = "library"
    PASSWORD = "$om3V3ry$3cur3P@$$w0rd"
    BASE_URL = "http://bibliothek.scs-ad.scs.ch:80"
    LIBRARY_NAME = "SCS_Library"

elif SELECTOR == "LOCAL":
    USERNAME = "eknecht"
    PASSWORD = "1234"
    BASE_URL = "http://127.0.0.1:666"
    LIBRARY_NAME = "Calibre_Library"
