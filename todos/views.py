from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# usei apenas para testar sem a segurança do csrf token
from django.views.decorators.http import require_http_methods

from .todo import todos


def index(request):
    return render(request, 'index.html', {'todos': []})


# @csrf_exempt
@require_http_methods(['POST'])
def search(request):
    res_todos = []
    search = request.POST['search']
    if len(search) == 0:
        return render(request, 'todo.html', {'todos': []})
    for i in todos:
        if search in i['title']:
            res_todos.append(i)

    return render(request, 'todo.html', {'todos': res_todos})
