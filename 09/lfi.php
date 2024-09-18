<?php

// インクルードするファイルはユーザー入力パラメーターによって決定される
$filename = $_GET['file'];

// 指定されたファイルをインクルードする」
include($filename);
?>

