from django.db import models



class client(models.Model):
    take= 'taken'
    av='available'
    default='--------' 
    take_choice= [(take, 'Taken'), (av, 'Return')]
    name= models.CharField(max_length=250)
    phone_number= models.CharField(max_length=250)
    address= models.CharField(max_length=250)
    book_title= models.ForeignKey('book_store',on_delete= models.CASCADE,)
    date_taken= models.DateTimeField(auto_now_add=True,blank=True)
    status= models.CharField(max_length=250, choices=take_choice)
 
    def __str__(self):
        return self.status,self.book_title
   

		

class book_store(models.Model):
    book_title= models.CharField(max_length=250)
    author= models.CharField(max_length=250)
    ISBN= models.CharField(max_length=250, null=True)
    publishing_house= models.CharField(max_length=250, null=True)
   

    def __str__(self):
        return self.book_title



    
