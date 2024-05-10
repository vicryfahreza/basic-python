book = {}

book["Tom"] = {
    "name": "Tom",
    "address": "Red Street NYC",
    "phone": 89898989
}
book["Larry"] = {
    "name": "Larry",
    "address": "Green Street NYC",
    "phone": 23232434
}

import json

s = json.dumps(book)
with open("c://src-data//book.txt", "w") as f:
    f.write(s)

r = open("c://src-data//book.txt", "r")
readBook = r.read()
print(readBook)