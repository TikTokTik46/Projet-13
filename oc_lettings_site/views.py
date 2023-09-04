from django.shortcuts import render

# Main index
def index(request):
    return render(request, 'index.html')
