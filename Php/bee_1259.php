<?php
$qtd = intval(fgets(STDIN));
$pares = array();
$impares = array();
while($qtd > 0){
    $numero = intval(fgets(STDIN));
    
    if ($numero % 2 == 0){
        array_push($pares, $numero);
    } else {
        array_push($impares, $numero);
    }
    $qtd -= 1;
}
sort($pares);
foreach($pares as $valor){
    echo $valor . "\n";
}
rsort($impares);
foreach($impares as $valor){
    echo $valor . "\n";
}


?>