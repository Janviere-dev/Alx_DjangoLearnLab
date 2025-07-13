reate Operation

This file documents the creation of a `Book` instance using Django's ORM through the shell.

## 📌 Command Used
```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
output:
<Book: 1984 by George Orwell (1949)>

