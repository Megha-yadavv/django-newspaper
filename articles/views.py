from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article


@login_required
def articleView(request):
    if request.method == 'POST':
        data = request.POST
        title_value = data.get('title')
        body_value = data.get('body')
       

        Article.objects.create(title = title_value, body = body_value, author = request.user)
        return redirect('/article_list')

    return render(request, 'article.html')


def articleList(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles' : articles})

def articleEdit(request, id):
    article = Article.objects.get(id = id)
    
    if request.method == 'POST':
         data = request.POST
         article.title = data.get('title')
         article.body = data.get('body')
    

         article.save()
         return redirect('/article_list/')

    return render(request, 'article_edit.html', {'article': article})

def articleDelete(request, id):
    article = Article.objects.get(id = id)
    if request.method == 'POST':
         article.delete()
         return redirect('/article_list/')
    

    return render(request, 'article_delete_confirm.html', {'article': article})
