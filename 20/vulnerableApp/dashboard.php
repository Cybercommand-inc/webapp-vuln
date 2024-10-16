<?php
session_start();

//if (!isset($_GET["token"]) || $_SESSION["token"] !== $_GET["token"]) {
if (!isset($_GET["token"])) {
    echo "アクセスが拒否されました！";
    exit();
}
?>
<!DOCTYPE html>
<html lang="jp">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ダッシュボード</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>ダッシュボードへようこそ！</h1>
    <p>ログインに成功しました。</p>
</body>
</html>
