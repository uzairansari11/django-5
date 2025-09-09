from django.db import models

# Create your models here.
"""
In Django, what’s the difference between:

created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

created_at (auto_now_add=True) → Django sets this field only once, when the row is first created.

updated_at (auto_now=True) → Django updates this field every time you call .save(), so it always reflects the latest modification.


⚡ Extra Tip:
If you update using .update() on a queryset, auto_now=True won’t trigger — because .update() bypasses save(). So for timestamps, prefer using .save() when you need it auto-updated.
------------------------------------------------------------------------------------------


class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

If I have an author object, how can I get all of their books?
And if I have a book object, how can I get its author?

author.books.all()

book.author

----------------------------------------------------------------------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    published_date = models.DateField()

written_at_least_two_book=Author.objects.annotate(book_count=Count('books__id')).filter(book_count__gte=2)




"""
"""
class Product (models.Model):
  name=models.CharField(max_length=200)
  description=models.TextField(max_length=5000)
  price=models.DecimalField(max)
"""




class Author (models.Model):
  name=models.CharField(max_length=120,db_index=True)
  email=models.EmailField(unique=True)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

  class Meta:
    ordering=['name']
    indexes=[models.Index(fields=['name'])]

  def __str__(self):
    return self.name


# class Category (models.Model):
#   title=models.CharField(max_length=120,unique=True)

#   def __str__(self):
#     return self.title
  
# class Book(models.Model):
#   title = models.CharField(max_length=120)
#   price=models.DecimalField(max_digits=9,decimal_places=2,default=0)
#   author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name="books")
#   categories  = models.ManyToManyField(Category, related_name="books", blank=True)
#   publish=models.DateField(null=True,blank=True)
#   stock= models.PositiveIntegerField(default=0)
#   sold= models.PositiveIntegerField(default=0)

#   class Meta:
#         constraints = [
#             models.CheckConstraint(check=models.Q(stock__gte=0), name="stock_non_negative"),
#         ]
  

