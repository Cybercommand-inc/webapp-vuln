<?php
session_start();

// デモンストレーション目的の簡単な認証
$valid_username = "user";
$valid_password = "password";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    if ($username === $valid_username && $password === $valid_password) {
        $_SESSION["loggedin"] = true;
        $session_token = bin2hex(random_bytes(16));
        $_SESSION["token"] = $session_token;
        header("Location: dashboard.php?token=$session_token");
        exit();
    } else {
        echo "無効な認証情報です！";
    }
}
?>
