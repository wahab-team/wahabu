from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Request, Response
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.serving import run_simple
import streamlit.cli

def simple(env, resp):
    if Request(env).headers.get('X-Forwarded-Proto') == 'http':
        resp('301 Moved Permanently', [('Location', Request(env).url.replace("http://", "https://"))])
        return []
    return Response('Hello World!')(env, resp)

app = DispatcherMiddleware(simple, {
    '/app': streamlit.cli.server.server
})

if __name__ == '__main__':
    run_simple('localhost', 8080, app, use_reloader=True, use_debugger=True, use_evalex=True)
