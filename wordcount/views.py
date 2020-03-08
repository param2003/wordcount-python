from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request, 'home.html')
def count(request):
    data = request.GET['fulltextarea']
    word_list = data.split()
    data_length = len(word_list)
    worddictionary = {}
    for i in word_list:
        if i in worddictionary:
            worddictionary[i] += 1
        else:
            worddictionary[i] = 1
    sorted_list = sorted(worddictionary.items() , key = operator.itemgetter(1))
    return render(request , 'count.html' , {'fulltext':data , 'words':data_length , 'word_dict':sorted_list})
def about(request):
    return render(request , 'about.html')

