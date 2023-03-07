from wsgiref.simple_server import make_server


def application(environ, start_response): # WSGI interface
    '''
    environ: variables from request
        - method
        - html version
        - headers
        - body
    start_response
    '''
    status = '200 OK' # must go with "OK" at least 4 chars
    headers = []

    start_response(status, headers) # MetaData
    html = "Hola mundo estamos en el WSGI"

    return [ bytes(html, 'UTF-8')] # Client response
    
PORT = 8000

with make_server('localhost', PORT, application) as server:
    print(f">>> El servidor se encuentra a la escucha en el puerto {PORT}")
    server.serve_forever()

"""server = make_server('localhost', PORT, application)
print(f">>> El servidor se encuentra a la escucha en el puerto {PORT}")
server.serve_forever()"""