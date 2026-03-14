from django.shortcuts import render, redirect
from django.http import Http404
from .models import Article


def archive(request):
    return render(
        request,
        'archive.html',
        {"posts": Article.objects.all()}
    )


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)

        return render(
            request,
            'article.html',
            {"post": post}
        )

    except Article.DoesNotExist:
        raise Http404


def create_post(request):

    if not request.user.is_anonymous:

        if request.method == "POST":

            form = {
                "title": request.POST.get("title"),
                "text": request.POST.get("text")
            }

            # проверка заполнения полей
            if form["title"] and form["text"]:

                # проверка уникальности названия
                if Article.objects.filter(title=form["title"]).exists():

                    form["errors"] = "Статья с таким названием уже существует"

                    return render(request, 'create_post.html', {'form': form})

                # создание статьи
                article = Article.objects.create(
                    title=form["title"],
                    text=form["text"],
                    author=request.user
                )

                return redirect('get_article', article_id=article.id)

            else:

                form["errors"] = "Не все поля заполнены"

                return render(request, 'create_post.html', {'form': form})

        else:
            return render(request, 'create_post.html', {})

    else:
        raise Http404
