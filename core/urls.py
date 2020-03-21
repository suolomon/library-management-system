from django.urls import path

from .views import (InStore, BookList,
                    LendBook, BooksTaken,
                    Returner, BookDetails)

urlpatterns = [
   path('booksinstore/', InStore.as_view(), name='instore'),
   path('', BookList.as_view(), name='booklist'),
   path('lendbook/', LendBook.as_view(), name='lendbook'),
   path('bookstaken/', BooksTaken.as_view(), name='bookstaken'),
   path('returner/<int:pk>', Returner.as_view(), name='returner'),
   path('bookdetails/<int:pk>', BookDetails.as_view(), name='bookdetails'),

]
