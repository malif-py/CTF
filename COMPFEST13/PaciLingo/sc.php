<?php
if (!isset($_COOKIE['lang'])) {
    setcookie('lang', 'langpack/id-ID', 0, '/');
    header("Location: /");
}
if (isset($_POST['chglang'])) {
    setcookie('lang', $_POST['chglang'], 0, '/');
    header("Location: /");
}

$langpack = $_COOKIE['lang'].".php";
include $langpack;
