<?php
$calculo = 0;
$contagem = 0;

while (true) {
    $valor = intval(fgets(STDIN));
    if ($valor < 0) {
        break;
    }
    $calculo = $calculo + $valor;
    $contagem = $contagem + 1;
}

    $media = $calculo / $contagem;
    
    echo "$media";

?>
