<?php
$entrada = readline();
$valores = explode(' ', $entrada);

$a1 = intval($valores[0]);
$a2 = intval($valores[1]);
$a3 = intval($valores[2]);

$maiorAB = ($a1 + $a2 + abs($a1 - $a2)) / 2;
$maiorABC = ($maiorAB + $a3 + abs($maiorAB - $a3)) / 2;

echo "$maiorABC eh o maior" . PHP_EOL;
?>