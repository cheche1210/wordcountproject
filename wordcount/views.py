from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def result(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary = {}
  
    

    
    
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    


    return render(request, 'result.html', {
        'fulltext' :  full_text,
        'total':len(word_list),
        'dictionary':sorted(word_dictionary.items(), key=lambda x: x[1], reverse=True),
        'maxTotal':max(word_dictionary.items(), key = lambda x: x[1])[0]
    })

# Create your views here.
