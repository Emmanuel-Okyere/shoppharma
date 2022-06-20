from django.shortcuts import render


def handler404(request, *args, **argv):
    response = render(request, 'shop/404.html')
    print(response)
    response.status_code = 404
    return response