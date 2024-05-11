<?php
$contador = 0;
for($i = 0; $i < 6; $i++){
$valores = intval(fgets(STDIN));
if($valores >= 0){
    $contador += 1;
}
}

echo "$contador valores positivos". PHP_EOL;

?>