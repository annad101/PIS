from django.shortcuts import render, redirect
from django.http import Http404
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


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
    
def register(request):

    if request.method == "POST":

        form = {
            "username": request.POST.get("username"),
            "email": request.POST.get("email"),
            "password": request.POST.get("password")
        }

        if form["username"] and form["email"] and form["password"]:

            if User.objects.filter(username=form["username"]).exists():

                form["errors"] = "Пользователь с таким именем уже существует"
                return render(request, "register.html", {"form": form})

            else:

                User.objects.create_user(
                    username=form["username"],
                    email=form["email"],
                    password=form["password"]
                )

                return redirect("archive")

        else:

            form["errors"] = "Все поля должны быть заполнены"
            return render(request, "register.html", {"form": form})

    else:

        return render(request, "register.html")
    
def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:

            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)
                return redirect("archive")

            else:

                return render(request, "login.html", {
                    "error": "Нет аккаунта с таким логином и паролем"
                })

        else:

            return render(request, "login.html", {
                "error": "Заполните все поля"
            })

    else:

        return render(request, "login.html")