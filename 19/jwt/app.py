import jwt
import datetime
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# HMAC署名用の弱い秘密鍵
SECRET_KEY = 'secret'

# index.htmlをホームページとして提供
@app.route('/')
def index():
    return render_template('index.html')

# JWT署名が検証されない脆弱なルート
@app.route('/no-signature-verification', methods=['GET'])
def no_signature_verification():
    token = request.args.get('token', '')
    try:
        # 署名を検証せずにトークンをデコード
        decoded = jwt.decode(token, options={"verify_signature": False})
        return jsonify({"message": "Token decoded without signature verification", "data": decoded})
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"})
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"})

# 'none'アルゴリズムに脆弱なルート
@app.route('/none-algorithm', methods=['GET'])
def none_algorithm():
    token = request.args.get('token', '')
    try:
        # 'none'アルゴリズムを許可（脆弱性）
        decoded = jwt.decode(token, key=None, algorithms=["none"], options={"verify_signature": False})
        return jsonify({"message": "Token decoded using 'none' algorithm", "data": decoded})
    except jwt.InvalidTokenError as e:
        return jsonify({"error": "Invalid token", "details": str(e)})

# 弱いHMAC秘密鍵を許可する脆弱なルート
@app.route('/weak-hmac-secret', methods=['GET'])
def weak_hmac_secret():
    token = request.args.get('token', '')
    try:
        # 弱いHMAC秘密鍵を使用してトークンをデコード
        decoded = jwt.decode(token, key=SECRET_KEY, algorithms=["HS256"])
        return jsonify({"message": "Token decoded using weak HMAC secret", "data": decoded})
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"})

# 任意の'jku'ヘッダーをサポートする脆弱なルート
@app.route('/arbitrary-jku', methods=['GET'])
def arbitrary_jku():
    token = request.args.get('token', '')
    try:
        # トークンから'jku'ヘッダーを抽出
        headers = jwt.get_unverified_header(token)
        if 'jku' in headers:
            return jsonify({"message": "Arbitrary 'jku' header found", "jku": headers['jku']})
        return jsonify({"message": "No 'jku' header found"})
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"})

# 任意の'x5u'ヘッダーをサポートする脆弱なルート
@app.route('/arbitrary-x5u', methods=['GET'])
def arbitrary_x5u():
    token = request.args.get('token', '')
    try:
        # トークンから'x5u'ヘッダーを抽出
        headers = jwt.get_unverified_header(token)
        if 'x5u' in headers:
            return jsonify({"message": "Arbitrary 'x5u' header found", "x5u": headers['x5u']})
        return jsonify({"message": "No 'x5u' header found"})
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
