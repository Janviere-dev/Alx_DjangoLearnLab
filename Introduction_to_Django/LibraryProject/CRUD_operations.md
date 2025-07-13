 
---

### 🗃️ `CRUD_operations.md`

```markdown
# Django Shell CRUD Operations on Book Model

This file documents each CRUD interaction performed via the Django shell.

## ✅ Create
```python
from bookshelf.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
# Output: <Book: 1984 by George Orwell (1949)>

