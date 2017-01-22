from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from models import Article






# Create your views here.
def home(request):
	articles = Article.objects.all()
	return render(request,'index.html',{'articles':articles})


def article_detail(request,id):
	try:
		article = Article.objects.get(id = id)
		return render(request,"article.html",{'article':article})
	except :
		
		return render(request,'error.html',{})


	

def admin(request):
	print("I am admin")
	return HttpResponse("i am admin")

def newarticle(request):
	if request.method == 'POST':
		newArticle = Article.objects.create(
				title = request.POST['title'],
				content = request.POST['content']
			)
		return HttpResponseRedirect('/myblog/article/'+str(newArticle.id))
	else:
		return render(request,'newarticle.html',{})

def delete_article(request,id):
	try:
		article = Article.objects.get(id = id)
		article.delete()
		return HttpResponseRedirect('/')
	except :
		
		return render(request,'error.html',{})
