import argparse
import os
import sys

import cherrypy
from beaker.middleware import SessionMiddleware
from werkzeug.debug import DebuggedApplication

from s2sproxy.server import WsgiApplication


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', action='store_true', dest="debug",
                        help="Enable debug mode.")
    parser.add_argument('-e', dest="entityid",
                        help="Entity id for the underlying IdP. If not "
                             "specified, a discovery server will be used "
                             "instead.")
    parser.add_argument(dest="config",
                        help="Configuration file for the pysaml sp and idp.")
    parser.add_argument(dest="server_config",
                        help="Configuration file with server settings.")
    args = parser.parse_args()

    sys.path.insert(0, os.getcwd())
    server_conf = __import__(args.server_config)

    wsgi_app = WsgiApplication(args).run_server
    if args.debug:
        wsgi_app = DebuggedApplication(wsgi_app)

    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': server_conf.PORT
    })
    if server_conf.HTTPS:
        cherrypy.config.update({
            'server.ssl_module': 'pyopenssl',
            'server.ssl_certificate': server_conf.SERVER_CERT,
            'server.ssl_private_key': server_conf.SERVER_KEY,
            'server.ssl_certificate_chain': server_conf.CERT_CHAIN,
        })

    cherrypy.tree.graft(SessionMiddleware(wsgi_app, server_conf.SESSION_OPTS),
                        '/')
    cherrypy.tree.mount(None, '/static', {
        '/': {
            'tools.staticdir.dir': server_conf.STATIC_DIR,
            'tools.staticdir.on': True,
        },
        '/robots.txt': {
            'tools.staticfile.on': True,
            'tools.staticfile.filename': "/home/site/style.css"
        }
    })

    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    main()