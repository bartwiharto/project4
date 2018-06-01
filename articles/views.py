from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Articles
from django.contrib.auth.decorators import login_required
from .import forms

@login_required(login_url="/accounts/login/")

def article_list(request):
    articles = Articles.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Articles.objects.get(slug=slug)

    return render(request, 'articles/article_detail.html', {'article': article})


def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticles(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()

            return redirect('articles:list')
    else:
        form = forms.CreateArticles()
    return render(request, 'articles/article_create.html', {'form': form})
