from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Article
from .serializers import ArticleSerializer

@api_view(["GET","POST"])  # we determine which request will be considered
def article_list_create_api_view(request):

    if(request.method == "GET"):
        articles = Article.objects.filter(is_active = True)
        serializer = ArticleSerializer(articles, many = True)

        return Response(serializer.data)

    elif(request.method == "POST"):
        serializer = ArticleSerializer(data = request.data)  # convert ediyoruz, sonra valid mi diye kontrol ediyoruz
        if(serializer.is_valid()): # valid ise kaydediyoruz

            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(status = status.HTTP_400_BAD_REQUEST)  # valid değilse status = 400 dönüyoruz

