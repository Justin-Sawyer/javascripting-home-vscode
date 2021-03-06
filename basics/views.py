from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from datetime import datetime

from .models import Article, Category
from .forms import ArticleForm


# This view is not really needed, but is being kept for if users type
# /basics into the url bar
def all_basics(request):
    """ A view to return the basics all articles page """
    articles = Article.objects.all()

    context = {
        'articles': articles,
        'title': 'JavaScripting : The Basics.',
        'section': 'Basics',
        'pagename': 'Reference',
        'this_page': True
    }
    return render(request, 'basics/articles.html', context)


def article(request, article_id):
    """ A view to show the individual article """
    next_article = None
    prev_article = None

    articles = Article.objects.all()
    article = get_object_or_404(Article, pk=article_id)
    # data_a = Article.objects.values("date_added")
    # print(data_a)
    # Used to display "this" article button in different color
    filteredArticle = Article.objects.get(pk=article_id)
    # Next page / previous page buttons
    if filteredArticle != Article.objects.last():
        next_article = Article.get_next_by_date_added(filteredArticle)
        next_article = next_article.id
    if filteredArticle != Article.objects.first():
        prev_article = Article.get_previous_by_date_added(filteredArticle)
        prev_article = prev_article.id
    
    context = {
        'article': article,
        'articles': articles,
        'title': 'JavaScripting : The Basics.',
        'section': 'Basics',
        'pagename': article.name,
        'filteredArticle': filteredArticle,
        'prev_article': prev_article,
        'next_article': next_article,
    }
    return render(request, 'basics/article.html', context)


@login_required
def add_article(request):
    """ Add an article """
    articles = Article.objects.all()

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added article!')
            return redirect(reverse('basics'))
        else:
            messages.error(request, 'Failed to add article. Please ensure the form is valid.')
    else:
        form = ArticleForm
    template = 'basics/add_article.html'
    context = {
        'form': form,
        'articles': articles,
        'title': 'JavaScripting : The Basics.',
        'section': 'Basics',
        'pagename': 'Add an Article',
    }

    return render(request, template, context)


@login_required
def edit_article(request, article_id):
    """ Edit an article """
    articles = Article.objects.all()

    article = get_object_or_404(Article, pk=article_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated article!')
            return redirect(reverse('article_detail', args=[article.id]))
        else:
            messages.error(request, 'Failed to update article. Please ensure the form is valid.')
    else:
        form = ArticleForm(instance=article)
        
    messages.info(request, f'You are editing {article.name}')
    template = 'basics/edit_article.html'
    context = {
        'articles': articles,
        'title': 'JavaScripting : The Basics.',
        'section': 'Basics',
        'pagename': f'Editing "{article.name}"',
        'form': form,
        'article': article,
    }
    return render(request, template, context)


@login_required
def delete_article(request, article_id):
    """ Delete a product from the store """
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    messages.success(request, 'Article deleted!')
    return redirect(reverse('basics'))

