from django.shortcuts import render, redirect

def first(request):
    return render(request, 'first.html')
    
def second(request):
    if request.method == "POST":
        score = request.POST.get('score')
        redirect('second')
    return render(request, 'second.html', {'score': score})

def third(request):
    if request.method == "POST":
        score = request.POST.get('score')
        redirect('third')
    return render(request, 'third.html', {'score': score})
    
def firth(request):
    if request.method == "POST":
        score = request.POST.get('score')
        redirect('firth')
    return render(request, 'firth.html', {'score': score})
    
def fifth(request):
    if request.method == "POST":
        score = request.POST.get('score')
        redirect('fifth')
    return render(request, 'fifth.html', {'score': score})
    
def sixth(request):
    if request.method == "POST":
        score = request.POST.get('score')
        redirect('sixth')
    return render(request, 'sixth.html', {'score': score})
    
def seventh(request):
    if request.method == "POST":
        score = request.POST.get('score')
        redirect('seventh')
    return render(request, 'seventh.html', {'score': score})
    
def eighth(request):
    if request.method == "POST":
        score = request.POST.get('score')
        redirect('eighth')
    return render(request, 'eighth.html', {'score': score})
    
def ninth(request):
    if request.method == "POST":
        score = request.POST.get('score')
        redirect('ninth')
    return render(request, 'ninth.html', {'score': score})
    
def tenth(request):
    if request.method == "POST":
        score = request.POST.get('score')
        redirect('tenth')
    return render(request, 'tenth.html', {'score': score})
    
def finish(request):
    if request.method=="POST": 
        score = request.POST.get('score')
        redirect('finish')
        return render(request, 'finish.html', {'score': score})