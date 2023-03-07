from wsgiref.simple_server import make_server


def application(environ, start_response): #Interfaz wsgi
    '''
    environ: variables from request
    start_response
    '''
    status = '200 OK'
    headers = []

    start_response(status, headers) # MetaData
    html = "Hola mundo estamos en el WSGI"

    return [ bytes(html, 'UTF-8')] # Respuesta al cliente
    

server = make_server('localhost', 8000, application)
server.serve_forever()