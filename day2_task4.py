book = {"title": "Python Programming",
         "author": "John Doe",
         "year": 2021,
         "publisher": "Tech Books Publishing Co.",
         "pages": 350,
         "rating": 4.5
}

for key, value in book.items():
    print(f"{key}: {value}")

print("=" * 20)

book ["rating"] = 4.7
print("Updated rating:", book["rating"])

book ["Genre"] = "Programming"
print("Added Genre:", book["Genre"])

for key, value in book.items():
    print(f"{key}: {value}")

print("=" * 20)

del book["year"]
print("After deleting year")

for key, value in book.items():
    print(f"{key}: {value}")
print("=" * 20)
