from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Getting the text
    txt = request.POST.get('text', 'default')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    removePunc = request.POST.get('removePunc', 'off')
    fullLower = request.POST.get('lowercase', 'off')
    fullUpper = request.POST.get('UPPERCASE', 'off')
    if (removePunc == 'on'):
        analyzed = ""
        for char in txt:
            if (char not in punctuations):
                analyzed += char
        param = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        txt = analyzed
    if (fullUpper == 'on'):
        analyzed = ""
        for char in txt:
            analyzed += str(char).upper()
        param = {'purpose': 'Caps', 'analyzed_text': analyzed}
        txt = analyzed

    if (fullLower == 'on'):
        analyzed = ""
        for char in txt:
            analyzed += str(char).lower()

        param = {'purpose': 'NO Caps', 'analyzed_text': analyzed}
        txt = analyzed
    # Analyzing the text
    return render(request, 'analyze.html', param)
