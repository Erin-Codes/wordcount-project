from django.http import HttpResponse #This is used to be able to return a String in the code as html on the web page/app.
from django.shortcuts import render #This will be used to be able to return an html template.
import operator
import re

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    # Retrieves the value for 'fulltext' from the form in home.html

    no_punctuation = re.sub(r'[^\w\s]', '', fulltext)
    # Using regular expressions to remove all punctuation from the text.

    count = len(fulltext.split())
    # Assigning the amount of words in fulltext to the variable count.

    word_dict = {}
    for word in no_punctuation.split():
        if word.lower() in word_dict:
            word_dict[word.lower()] += 1
        else:
            word_dict[word.lower()] = 1
    # Adds 1 to the value of the word(key) if the word already exists in the dict,
    # and puts the value equal to one if the value doesn't exist in the dict.

    sorts = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    #Line 19 sorts word_dict


    return render(request, 'count.html', {'fulltext':fulltext, 'word_count':count, 'sorted_words': sorts})
    # returns count.html and a python dictionary to be accessed by count.html
