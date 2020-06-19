from django.shortcuts import render

# Create your views here.
def list_posts(request):
    return render(request, "main/list_posts.html", {})

def create_post(request):
    return render(request, "main/create_post.html", {})