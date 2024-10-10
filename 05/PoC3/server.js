const express = require('express');
const app = express();
const bodyParser = require('body-parser');

// リクエストボディを解析するミドルウェア
app.use(bodyParser.urlencoded({ extended: true }));

// 仮のユーザーデータベース
let users = {
  1: { name: 'ジョン・ドウ', email: 'john@example.com' }
};

// 静的ファイルを提供する（フロントエンド）
app.use(express.static('public'));

// アカウント削除用のルート
app.post('/delete-account', (req, res) => {
  const userId = req.body.userId;
  
  if (users[userId]) {
    delete users[userId];
    res.send('アカウントが正常に削除されました');
  } else {
    res.send('ユーザーが見つかりません');
  }
});

// サーバーを起動する
app.listen(3000, () => {
  console.log('サーバーが http://localhost:3000 で実行中');
});
