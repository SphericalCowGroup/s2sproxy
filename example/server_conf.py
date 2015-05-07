# -*- coding: utf-8 -*-

# Server hostname
HOST = 'localhost'
# Port for the server
PORT = 8090
# True if HTTPS should be used, false for plain HTTP
HTTPS = True
# If HTTPS is true you have to assign the server cert, key and certificate chain.
SERVER_CERT = 'pki/mycert.pem'
SERVER_KEY = 'pki/mykey.pem'
# CERT_CHAIN="certs/chain.pem"
CERT_CHAIN = None

if HTTPS:
    BASEURL = 'https://%s' % HOST
else:
    BASEURL = 'http://%s' % HOST

STATIC_DIR = '/static'
# Filename for log
LOG_FILE = 'server.log'

# Beaker session configuration.
# This session can be configured to use database, file, or memory.
SESSION_OPTS = {
    'session.type': 'memory',
    'session.cookie_expires': True,  # Expire when the session is closed.
    #'session.data_dir': './data',
    'session.auto': True,
    #'session.timeout' : 900 #Never expires only when the session is closed.
}