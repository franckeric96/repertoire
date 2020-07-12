from django.shortcuts import render
from website.models import  SocialAccount, Presentation, Article, Gallerie


# Create your views here.
def home(request):


    sociaux = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[:1].get()
    article = Article.objects.filter(status=True)[:1].get()
    gallerie = Gallerie.objects.filter(status=True)

    
    datas = {
        'sociaux':sociaux,
        'presentation': presentation,
        'article': article,
        'gallerie':gallerie

    }
    
    return render(request, "pages/index.html", datas)


def about(request):    

    sociaux = SocialAccount.objects.filter(status=True)
    presentation = Presentation.objects.filter(status=True)[:1].get()
    article = Article.objects.filter(status=True)[:1].get()
    gallerie = Gallerie.objects.filter(status=True)

    datas = {

        'sociaux':sociaux,
        'presentation': presentation,
        'article': article,
        'gallerie':gallerie


    }
    
    return render(request, "pages/about.html", datas)

