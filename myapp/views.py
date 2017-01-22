from django.shortcuts import render
from django.http import HttpResponse
from models import Article






# Create your views here.
def home(request):
	articles = Article.objects.all()
	return render(request,'index.html',{'articles':articles})


def article_detail(request):
	print("Detail of the article")
	return HttpResponse("Detail of the article")

def admin(request):
	print("I am admin")
	return HttpResponse("i am admin")
