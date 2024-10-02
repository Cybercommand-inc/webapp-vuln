<?php

if (isset($_POST["email"]) and isset($_POST["text"])){
  $email = $_POST["email"];
  $text = $_POST["text"];

  $headers = "From: " . $email;

  mail("mailuser1@srt", "Contact Form", $text, $headers, "-f" . $email);
}

header("Location: http://192.168.7.246/");

?>
