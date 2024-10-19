# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines = 50
symbols = 25
size_symbols_byte = 4
disk_capacity_mb = 1.44

disk_capacity_byte = disk_capacity_mb * 1024 * 1024
size_of_one_book_byte = pages * lines * symbols * size_symbols_byte
number_of_books = disk_capacity_byte/size_of_one_book_byte

print("Количество книг, помещающихся на дискету:", round(number_of_books))
