from django.shortcuts import render

from .models import posts

posts_ = {
    post['id']: post for post in posts
}


def index(request):
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, id):
    if id in posts_:
        return render(request, 'blog/detail.html', {'post': posts_[id]})

    return render(request, 'blog/not_found_error.html')


def category_posts(request, category_slug):
    return render(request, 'blog/category.html', {'category': category_slug})
