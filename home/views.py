"""
Tjene rowt
"""

from django.shortcuts import render

# Create your views here.


def index(request):
    """
    A view to display the home/index page
    """

    return render(request, 'home/index.html')
