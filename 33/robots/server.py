# webapp/server.py
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_public():
    return send_from_directory('public', 'index.html')

@app.route('/restricted/<path:filename>')
def serve_restricted(filename):
    return send_from_directory('restricted', filename)

@app.route('/robots.txt')
def serve_robots():
    return send_from_directory('.', 'robots.txt')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

