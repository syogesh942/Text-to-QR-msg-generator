from django.shortcuts import render
# from home.views import homepage

# Create your views here.

def homepage(request):
    # if request.method == "GET":
    #     print(request.GET)
    # else:
    #     print(request.GET)

    if 'textQR' in request.POST:
        QR = request.POST.get('textQR')
        QR = QR.split(' ')
        QR = '%20'.join(QR)
        url = 'https://chart.googleapis.com/chart?chs=300x300&cht=qr&chl={}&choe=UTF-8'.format(QR)
    else:
        # Handle the case where 'textQR' is not present
        QR = 'please enter a string'
        QR = QR.split(' ')
        QR = '%20'.join(QR)
        url = 'https://chart.googleapis.com/chart?chs=300x300&cht=qr&chl={}&choe=UTF-8'.format(QR)

    return render(request, 'home.html', {'url': url})