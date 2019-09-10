<<<<<<< HEAD

=======
>>>>>>> 8ef656553446a01c279f0b34583b1507b163af7b
from django.shortcuts import render
from .models import Cat

# View functions

def home(request):
<<<<<<< HEAD
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
=======
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')
>>>>>>> 8ef656553446a01c279f0b34583b1507b163af7b

def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats })

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', { 'cat': cat })