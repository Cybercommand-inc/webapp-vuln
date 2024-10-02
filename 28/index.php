<!DOCTYPE html>
<html>
  <head>
    <title>cybercommand</title>
    <link rel="stylesheet" href="index.css">
  <body>
    <div class="contact">
      <h2 class="title">コンタクト</h2>
      <form action="send.php" method="post">
        <label for="name">メールアドレス:</label><br/>
        <input type="email" id="email" name="email" placeholder="you@example.org"/><br/>
        <label for="text">テキスト:</label><br/>
        <textarea id="text" name="text" minlength="10" placeholder="tst"></textarea><br/>
        <button class="submit">送る&ensp;→</button>
      </form>
    </div>
  </body>
</html>
