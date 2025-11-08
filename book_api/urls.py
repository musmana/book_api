from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2>Welcome to the Book Management API 📚</h2><p>Visit <a href='/api/books/'>/api/books/</a> to access the API.</p>")

urlpatterns = [
    path('', home),  # 👈 Add this line
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
]
