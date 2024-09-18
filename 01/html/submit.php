<?php
// プレーンテキストのパスワード送信に脆弱
$username = $_POST['username'];
$password = $_POST['password'];

// Secure または HttpOnly フラグなしでクッキーを設定
setcookie('session', 'randomsessionvalue', time() + 3600);  // Secure または HttpOnly フラグなし

// Referer ヘッダーに基づいて応答 (検証なし)
if (isset($_SERVER['HTTP_REFERER'])) {
    echo "Referer は " . htmlspecialchars($_SERVER['HTTP_REFERER']);
}

// パスワードの取り扱い (これは単なる例です。パスワードをこのように保存するべきではありません)
file_put_contents('passwords.txt', "ユーザー名: $username, パスワード: $password\n", FILE_APPEND);
echo "パスワードが保存されました。クッキーが有効な場合、Secure または HttpOnly フラグなしで設定されています。";
?>
