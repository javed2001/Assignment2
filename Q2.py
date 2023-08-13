books = {
    'book1': {
        'title': 'Percy Jackson and the Lightning Thief',
        'author': 'Rick Riordan',
        'year': 2005
    },
    'book2': {
        'title': 'The Sea of Monsters',
        'author': 'Rick Riordan',
        'year': 2006
    },
    'book3': {
        'title': 'The Titan\'s Curse',
        'author': 'Rick Riordan',
        'year': 2007
    },
    'book4': {
        'title': 'The Battle of the Labyrinth',
        'author': 'Rick Riordan',
        'year': 2008
    },
    'book5': {
        'title': 'The Last Olympian',
        'author': 'Rick Riordan',
        'year': 2009
    }
}

# b) Print the titles of all the books
for key, book in books.items():
    print("Title:", book['title'])

# c) Determine the book with the earliest publication year
earliest_book = min(books.values(), key=lambda x: x['year'])
print("Book with earliest publication year:", earliest_book['title'])
print("Author:", earliest_book['author'])
