import random

class Book:
    def __init__(self, title, author, publisher, publication_date, ISBN):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
        self.ISBN = ISBN

def generate_ISBN(publisher_code=None):
    if publisher_code is None:
        publisher_code = "".join([str(random.randint(0, 9)) for i in range(4)])
    ISBN = "978" + publisher_code + "".join([str(random.randint(0, 9)) for i in range(4)])
    sum = 0
    for i in range(0, 12, 2):
        sum += int(ISBN[i])
    for i in range(1, 12, 2):
        sum += 3 * int(ISBN[i])
    check_digit = 10 - (sum % 10)
    ISBN += str(check_digit if check_digit != 10 else 0)
    return ISBN

print(generate_ISBN("123456"))
