
from django.conf.urls import url
from .views import home,article_detail,admin,newarticle,delete_article

urlpatterns = [
    url(r'^$',home,name="home"),
    url(r'^article/(?P<id>[\d]+)$',article_detail,name="Article detail"),
    url(r'^delete_article/(?P<id>[\d]+)$',delete_article,name="delete_article"),

    url(r'^admin/$',admin,name="admin"),
    url(r'^article/add_new$',newarticle,name="new article"),
]
