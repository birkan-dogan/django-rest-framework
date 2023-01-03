from django.urls import path

from .views import ArticleListCreateAPIView, ArticleDetailAPIView

# urlpatterns for class-based views
urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view(), name="list-of-articles"),
    path("articles/<int:pk>",ArticleDetailAPIView.as_view(), name = "article-detail")
]


# urlpatterns for function-based views
"""
from news.api.views import article_list_create_api_view, article_detail_api_view

urlpatterns = [
    path("articles/", article_list_create_api_view, name="list-of-articles"),
    path("articles/<int:pk>",article_detail_api_view, name = "article-detail")
]

"""