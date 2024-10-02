from flask import Flask, request, render_template
from lxml import etree

app = Flask(__name__)

# Sample XML data
xml_data = '''<users>
    <user>
        <username>john</username>
        <password>john123</password>
    </user>
    <user>
        <username>alice</username>
        <password>alice123</password>
    </user>
    <user>
        <username>bob</username>
        <password>bob123</password>
    </user>
</users>'''

# Parse the XML data
tree = etree.XML(xml_data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/xpath_injection', methods=['GET'])
def xpath_injection():
    # GETリクエストからユーザー名を取得する
    username = request.args.get('username', '')
    
    # 脆弱なXPathクエリ
    query = f"//user[username/text()='{username}']/password/text()"
    
    # XPathクエリを実行する
    result = tree.xpath(query)
    
    if result:
        return f"パスワード: {result[0]}"
    else:
        return "そのユーザー名のユーザーは見つかりませんでした。"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

