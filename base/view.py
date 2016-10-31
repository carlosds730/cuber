from django.shortcuts import render
from cuber.settings import ALLOW_LOGIN


def basic_response(request, template, content):
    basic_content = {'allow_login': ALLOW_LOGIN}
    basic_content.update(content)
    return render(request, template, basic_content)
