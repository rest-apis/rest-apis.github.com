#encoding=utf-8
#pip install termcolor requests
#cf: http://pypi.python.org/pypi/termcolor
#cf: http://docs.python-requests.org/
from sys import argv, stdout
from termcolor import colored
import requests
import json, random

HTTP_ROOT = "http://notas.herokuapp.com"

def pretty_print(obj):
    if hasattr(obj, 'items'):
        for key, val in obj.items():
            print colored(key, "green"), val
    else:
        print obj

def index():
    print colored("Obteniendo todas las notas en json", 'green')
    print "curl -H Accept:application/json http://notas.herokuapp.com/notes"
    r = requests.get(HTTP_ROOT+"/notes", headers={'Accept': 'application/json'})
    pretty_print(json.loads(r.content))
def get():
    print colored("Obteniendo la primer nota en varios formatos", 'green')
    for f in ['text/html', 'application/json', 'text/plain', 'text/xml']:
        r = requests.get(HTTP_ROOT+"/notes/1", headers={'Accept': f})
        print colored("Pidiendo en formato %s"%f, attrs=['bold', 'underline'])
        pretty_print(r.headers)
        if r.status_code == 200:
            print colored(r.content, 'green')
        else:
            print colored(r.status_code, 'red')
        print '\n\n'
def post():
    title = "nota %s" % random.randint(0,100)
    text = "Lorem ipsum dolor sic amet"
    #curl
    for color in ['green', 'red']:
        print colored("Creando una nota:", 'green', attrs=['bold'])
        r = requests.post(
                    HTTP_ROOT+"/notes",
                    data = json.dumps({'note': {'title': title, 'content': text}}),
                    headers = {'Content-Type': 'application/json', 'Accept':"application/json"}
                )
        pretty_print(r.headers)
        print colored(r.content, color)

def put():
    print colored("Actualizando una nota", 'green', attrs=['bold'])
    title = "Nuevo título %s" % random.randint(0,100)
    r = requests.put(
                HTTP_ROOT+"/notes/1",
                data = json.dumps({'note': {'title': title}}),
                headers = {'Content-Type': 'application/json', 'Accept':"application/json"}
            )
    pretty_print(r.headers)
    print colored(r.content, 'green')

if __name__ == "__main__":
    action = argv[1] if len(argv) > 1 else "index"
    config = {'verbose': stdout}
    exec action+"()"
