<?php
$n = fgets(STDIN);
$pi = 3.14159;
$area = $pi * ($n * $n);

echo "A=" . number_format($area, 4);
?>