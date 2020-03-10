from django.db import models


class Client(models.Model):
    take = 'taken'

    available = 'available'

    take_choice = [(take, 'Taken'), (available, 'Return')]

    name = models.CharField(max_length=250)

    phone_number = models.CharField(max_length=250)

    address = models.CharField(max_length=250)

    book_title = models.ForeignKey('book_store', on_delete=models.CASCADE,)

    date_taken = models.DateTimeField(auto_now_add=True, blank=True)

    status = models.CharField(max_length=250, choices=take_choice)
    def __str__(self):
        return self.status, self.book_title
   
		
class Book_store(models.Model):
    book_title = models.CharField(max_length=250)

    author = models.CharField(max_length=250)

    isbn = models.CharField(max_length=250, null=True)

    publishing_house = models.CharField(max_length=250, null=True)
   
    def __str__(self):
        return self.book_title

