from django.shortcuts import render
from .forms import Post

# Create your views here.
def list_posts(request):
    return render(request, "main/list_posts.html", {})

def create_post(request):
    if request.method == 'POST':
        form = Post(request.POST)
        if form.is_valid():
            return render(request, "main/create_post.html", {})
    else:
        form = Post()
    return render(request, "main/create_post.html", {'form':form})