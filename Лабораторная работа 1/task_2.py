# TODO Найдите количество книг, которое можно разместить на дискете
disk = 1.44 * 1024 * 1024  # размер диска в байтах
sheet_per_book = 100
lines_per_page = 50
letters_per_line = 25
symbol = 4

book_size = symbol * letters_per_line * lines_per_page * sheet_per_book
books_per_disk = disk // book_size

print("Количество книг, помещающихся на дискету:", int(books_per_disk))