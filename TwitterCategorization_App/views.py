from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm
from .Classes.searchTweets_Test import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.

def Home(request):
	#posts = Post.objects.filter(whenPublished__lte=timezone.now()).order_by('-whenPublished')
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			twitterusername = form.cleaned_data['twitterusername']

			#make instance of a class used inside the file : searchTweets_Test
			searchTweets_Test_cls = TweetClassifier()

			#Download the train data set
			searchTweets_Test_cls.get_train_data()

			#run the NaivesBayes test
			Output = searchTweets_Test_cls.classify_account(twitterusername)

		return render(request, 'home.html', {
			'twitterusername': twitterusername,
			'Output':Output,
			'form': form
		})
	else:
		form = NameForm()
	return render(request, 'home.html', {'form': form})

