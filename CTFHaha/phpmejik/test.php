<?php
    if(isset($_GET['hehe']) && isset($_GET['haha'])) {
        if (($_GET['haha'] !== $_GET['hehe']) && (md5($_GET['hehe']) == md5($_GET['haha']))) {
            $fd = fopen("/var/flag.txt", "r");
            $flag = fread($fd, 100);
            fclose($fd);

            echo $flag;
        } else {
            echo "try again pls :(";
        }
    } else {
        highlight_file(__file__);
    }
?>
