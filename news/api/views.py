from rest_framework import status
from rest_framework.response import Response

from ..models import Article, Writer
from .serializers import ArticleSerializer, WriterSerializer

# function-based views
"""
from rest_framework.decorators import api_view
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

@api_view(["GET", "PUT", "DELETE"])
def article_detail_api_view(request, pk):

    # error handling
    try:
        article_instance = Article.objects.get(pk = pk)  # taking specific instance while considering primary key

    except Article.DoesNotExist:
        return Response(
            {
                "errors":{
                    "code":404,
                    "message": f"There is no id:{pk} article"
                }
            },
            status = status.HTTP_404_NOT_FOUND
        )

    if(request.method == "GET"):
        serializer = ArticleSerializer(article_instance)
        return Response(serializer.data)

    elif(request.method == "PUT"):
        serializer = ArticleSerializer(article_instance, data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)

        return Response(status = status.HTTP_400_BAD_REQUEST)

    elif(request.method == "DELETE"):
        article_instance.delete()

        return Response(
            {"message": f"The id:{pk} article is deleted"},
            status = status.HTTP_204_NO_CONTENT
        )

"""

#class based views

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class WriterListCreateAPIView(APIView):

    def get(self, request):

        writers = Writer.objects.all()
        serializer = WriterSerializer(writers, many = True)
        return Response(serializer.data)


    def post(self, request):

        serializer = WriterSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ArticleListCreateAPIView(APIView):

    def get(self, request):

        articles = Article.objects.filter(is_active = True)
        serializer = ArticleSerializer(articles, many = True)
        return Response(serializer.data)


    def post(self, request):

        serializer = ArticleSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ArticleDetailAPIView(APIView):

    def get_object(self, pk):
        article_instance = get_object_or_404(Article, pk = pk)
        return article_instance

    def get(self, request, pk):

        article = self.get_object(pk = pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):

        article = self.get_object(pk = pk)
        serializer = ArticleSerializer(article, data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):

        article = self.get_object(pk = pk)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)






