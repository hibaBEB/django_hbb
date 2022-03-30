from django.shortcuts import render
from .models import Post, Products

posts = [
{
	'author' : 'Noah',
	'title' : 'Post test',
	'content' : 'test',
	'date_posted' : 'March 18, 2022'
},
{
	'author' : 'hbb',
	'title' : 'Post test',
	'content' : 'test',
	'date_posted' : 'March 18, 2022'
}
]
def home(request):
		context = {
			'posts' : Post.objects.all()
		}
		return render(request, 'blog/home.html',context)

def products(request):
		context = {
			'products' : Products.objects.all()
		}
		return render(request, 'blog/products.html', context)
