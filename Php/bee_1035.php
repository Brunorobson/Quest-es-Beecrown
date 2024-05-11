<?php

$entrada = readline();
$valores = explode(' ', $entrada);

$a = intval($valores[0]);
$b = intval($valores[1]);
$c = intval($valores[2]);
$d = intval($valores[3]);

$soma1 = $c + $d;
$soma2 = $a + $b;

if($b > $c && $d > $a && $soma1 > $soma2 && $c > 0 && $d > 0 && $a % 2 == 0){
    echo "Valores aceitos";
} else {
    echo "Valores nao aceitos";
}
