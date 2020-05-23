from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(response):
    return render(response, 'home.html')
def count(response):
    Fulltext = response.GET['FullText']
    wordlist = Fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1

        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True)

    return render(response, 'count.html', {'initialtext': Fulltext, 'fcount': len(wordlist),'sortedwords': sortedwords})

def about(response):
        return render(response, 'About.html')
