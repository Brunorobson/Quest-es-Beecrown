<?php
$alfabeto = [
    'A' => 0, 'B' => 1, 'C' => 2, 'D' => 3, 'E' => 4, 'F' => 5, 'G' => 6,
    'H' => 7, 'I' => 8, 'J' => 9, 'K' => 10, 'L' => 11, 'M' => 12, 'N' => 13,
    'O' => 14, 'P' => 15, 'Q' => 16, 'R' => 17, 'S' => 18, 'T' => 19, 'U' => 20,
    'V' => 21, 'W' => 22, 'X' => 23, 'Y' => 24, 'Z' => 25
];

$qtd = intval(fgets(STDIN));

while ($qtd > 0) {
    $l = intval(fgets(STDIN));
    $hash = 0;

    for ($i = 0; $i < $l; $i++) {
        $linha = trim(fgets(STDIN));
        $len = strlen($linha);

        for ($j = 0; $j < $len; $j++) {
            $char = $linha[$j];
            $posicaoAlfabeto = $alfabeto[$char];
            $valor = $posicaoAlfabeto + $i + $j;
            $hash += $valor;
        }
    }

    echo $hash . "\n";
    $qtd--;
}
?>
