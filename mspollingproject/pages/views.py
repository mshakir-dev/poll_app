from django.shortcuts import render
# HomePage --> It will redirect to the Home Page
def index(request):
  return render(request, 'pages/index.html')