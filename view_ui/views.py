from django.shortcuts import render

def ui(request):
    return render(request, 'view_ui/view.html')
