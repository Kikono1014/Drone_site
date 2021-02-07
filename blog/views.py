from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News
from django.contrib.auth.forms import UserCreationForm

def show_news(request):
	if request.method == "GET":
		res = News.objects.all()
		context = {'newses': res}
		return render(request, 'content_news.html', context)

def show_one_news(request, news_id):
	res = get_object_or_404(News, pk=news_id)
	context = {'news': res}
	return render(request, 'content_one_news.html', context)


def show_main(request):
	if request.method == "GET":
		return render(request, 'content_main.html')

def show_structure(request):
	if request.method == "GET":
		return render(request, 'content_structure.html')

def show_using(request):
	if request.method == "GET":
		return render(request, 'content_using.html')

def show_moving(request):
	if request.method == "GET":
		return render(request, 'content_moving.html')

# Create your views here.yessssr
