from wsgiref.simple_server import make_server


def application(environ, start_response): #Interfaz wsgi
    '''
    environ: variables from request
        - method
        - html version
        - headers
        - body
    start_response
    '''
    status = '200 OK'
    headers = []

    start_response(status, headers) # MetaData
    html = "Hola mundo estamos en el WSGI"

    return [ bytes(html, 'UTF-8')] # Respuesta al cliente
    
PORT = 8000

with make_server('localhost', PORT, application) as server:
    print(f">>> El servidor se encuentra a la escucha en el puerto {PORT}")
    server.serve_forever()
