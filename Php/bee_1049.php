<?php
$nome1 = trim(fgets(STDIN));
$nome2 = trim(fgets(STDIN));
$nome3 = trim(fgets(STDIN));

if ($nome1 == "vertebrado" && $nome2 == "ave" && $nome3 == "carnivoro") {
 echo "aguia". PHP_EOL;   
}
elseif ($nome1 == "vertebrado" && $nome2 == "ave" && $nome3 == "onivoro") {
 echo "pomba". PHP_EOL;   
}
elseif ($nome1 == "vertebrado" && $nome2 == "mamifero" && $nome3 == "onivoro") {
 echo "homem". PHP_EOL;   
}
elseif ($nome1 == "vertebrado" && $nome2 == "mamifero" && $nome3 == "herbivoro") {
 echo "vaca". PHP_EOL;   
}
elseif ($nome1 == "invertebrado" && $nome2 == "inseto" && $nome3 == "hematofago") {
 echo "pulga". PHP_EOL;   
}
elseif ($nome1 == "invertebrado" && $nome2 == "inseto" && $nome3 == "herbivoro") {
 echo "lagarta". PHP_EOL;   
}
elseif ($nome1 == "invertebrado" && $nome2 == "anelideo" && $nome3 == "hematofago") {
 echo "sanguessuga". PHP_EOL;   
}
elseif ($nome1 == "invertebrado" && $nome2 == "anelideo" && $nome3 == "onivoro") {
 echo "minhoca". PHP_EOL;   
}



?>