from django.shortcuts import render

def error_img_path(codeStatus):
    img = 'img/errors/' + str(codeStatus) + '.png'
    return img

def error_404_view(request, exception=None):
    codeStatus = 404
    return render(request, 'error.html',{'codeStatus':codeStatus, 'img': error_img_path(codeStatus)}, status=404)


def error_500_view(request, exception=None):
    codeStatus = 500
    return render(request, 'error.html', {'codeStatus':codeStatus, 'img': error_img_path(codeStatus)}, status=500)
    
def error_403_view(request, exception=None):
    codeStatus = 403
    return render(request, 'error.html',{'codeStatus':codeStatus, 'img': error_img_path(codeStatus)}, status=403)