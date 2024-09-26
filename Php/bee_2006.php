<?php
$t = intval(fgets(STDIN));
$count = 0;

$entrada = readline();
$valores = explode(' ', $entrada);

for ($i = 0; $i < 5; $i++) {
    if (intval($valores[$i]) == $t) {
        $count++;
    }
}

print ($count);