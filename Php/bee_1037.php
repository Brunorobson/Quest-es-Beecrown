<?php
$cedula = doubleval(fgets(STDIN));

if($cedula < 0 || $cedula > 100){
    echo "Fora de intervalo". PHP_EOL;
}
elseif($cedula >= 0 && $cedula <=25){
    echo "Intervalo [0,25]". PHP_EOL;
}
elseif($cedula > 25 && $cedula <=50){
    echo "Intervalo (25,50]". PHP_EOL;
}
elseif($cedula > 50 && $cedula <=75){
    echo "Intervalo (50,75]". PHP_EOL;
}
elseif($cedula > 75 && $cedula <=100){
    echo "Intervalo (75,100]". PHP_EOL;
}