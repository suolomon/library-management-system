from django.urls import path

from .views import In_store, booklist,lendbook,bookstaken,returner,bookdetails

urlpatterns=[
   path('booksinstore/',In_store.as_view(),name='instore'),
   path('',booklist.as_view(), name='booklist'),
   path('lendbook/',lendbook.as_view(),name='lendbook'),
   path('bookstaken/',bookstaken.as_view(),name='bookstaken'),
   path('returner/<int:pk>', returner.as_view(),name='returner'),
   path('bookdetails/<int:pk>', bookdetails.as_view(),name='bookdetails'),

]