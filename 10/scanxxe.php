<?php
// テスト目的で外部エンティティの読み込みが許可されていることを確認してください
libxml_disable_entity_loader(false);

if (isset($_GET['xml']) && !empty($_GET['xml'])) {
    $xml = $_GET['xml'];

    // 新しい DOMDocument インスタンスを作成します
    $doc = new DOMDocument();

    //GET パラメータから XML を読み込みます。// LIBXML_NOENT を使用してエンティティを処理し、LIBXML_DTDLOAD を使用して DTD の読み込みを許可します。
    libxml_use_internal_errors(true);
    $result = $doc->loadXML($xml, LIBXML_NOENT | LIBXML_DTDLOAD | LIBXML_NOCDATA);

    if ($result === false) {
        // XML 読み込みエラーを処理します。
        echo '<p>Failed to load XML. Please check your input.</p>';
        $errors = libxml_get_errors();
        echo '<pre>';
        foreach ($errors as $error) {
            echo "Error: {$error->message}\n";
        }
        echo '</pre>';
        libxml_clear_errors();
    } else {
        // XML を処理します
        echo '<pre>';
        print_r($doc->documentElement->nodeValue);
        echo '</pre>';
    }
} else {
    echo '<p>XML入力を提供してください</p>';
}
?>

<form method="get" action="">
    <textarea name="xml" rows="10" cols="30"></textarea>
    <input type="submit" value="Submit XML">
</form>

