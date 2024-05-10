<?php
$cedula = intval(fgets(STDIN));
$cemreais = 0;
$cinquentareais = 0;
$vintereais = 0;
$deisreais = 0;
$cincoreais = 0;
$doisreais = 0;
$umreal = 0;
$valor = $cedula;
while($cedula > 0){
    if($cedula >= 100){
        $cedula -= 100;
        $cemreais += 1;
    }
    elseif($cedula >= 50){
        $cedula -= 50;
        $cinquentareais += 1;
    }
    elseif($cedula >= 20){
        $cedula -= 20;
        $vintereais += 1;
    }
    elseif($cedula >= 10){
        $cedula -= 10;
        $deisreais += 1;
    }
    elseif($cedula >= 5){
        $cedula -= 5;
        $cincoreais += 1;
    }
    elseif($cedula >= 2){
        $cedula -= 2;
        $doisreais += 1;
    }
    elseif($cedula >= 1){
        $cedula -= 1;
        $umreal += 1;
    }
}
    echo "$valor\n";
    echo "$cemreais nota(s) de R$ 100,00\n";
    echo "$cinquentareais nota(s) de R$ 50,00\n";
    echo "$vintereais nota(s) de R$ 20,00\n";
    echo "$deisreais nota(s) de R$ 10,00\n";
    echo "$cincoreais nota(s) de R$ 5,00\n";
    echo "$doisreais nota(s) de R$ 2,00\n";
    echo "$umreal nota(s) de R$ 1,00\n";
?>