from django.shortcuts import render


posts = [
    {
        'author':'ZachP',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 18, 2022'
    },
    {
        'author':'SomeoneElse',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 19, 2022'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
