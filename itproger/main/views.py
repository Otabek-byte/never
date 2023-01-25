from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        'title': 'General Site!',
        'values': ['some', 'some', 'body'],
        'obj': {
            'Car': 'BMW',
            'Age': '18',
            'Hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
