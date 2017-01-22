
from django.conf.urls import url
from .views import home,article_detail,admin

urlpatterns = [
    url(r'^$',home,name="home"),
    url(r'^article/$',article_detail,name="Article detail"),
    url(r'^admin/$',admin,name="admin"),
]
