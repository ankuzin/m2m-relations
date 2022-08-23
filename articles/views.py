from django.shortcuts import render

from articles.models import Article, Tags, ArticleTags


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all()
    for article in articles:
        a_tags = article.scopes.all()
    main_tags = Tags.objects.filter(articletags__is_main=True)
    for main_tag in main_tags:
        pass
    context = {'object_list': articles}

    return render(request, template, context)


# context должен выглядеть условно так?
# res = {'articles': [{'title': article.name, 'image': article.image,
#                      'scopes': [{'is_main': True/False, 'tag': {'name': tag.name}}, {}, {}]}, {}, {}]}
