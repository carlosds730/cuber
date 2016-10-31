from .models import MainText
from base.view import basic_response


# Create your views here.
def home(request):
    main_text = MainText.objects.first()
    return basic_response(request, 'home.html', {'main_text': main_text})
