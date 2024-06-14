<?php
$array = [
    'vertebrado' => ['ave' => ['carnivoro' => 'aguia','onivoro' => 'pomba'],
                     'mamifero' => ['onivoro' => 'homem','herbivoro' => 'vaca']],
    'invertebrado' => ['inseto' => ['hematofago' => 'pulga','herbivoro' => 'lagarta'],
        'anelideo' => ['hematofago' => 'sanguessuga','onivoro' => 'minhoca']]
];


$nome2 = trim(fgets(STDIN));
$nome3 = trim(fgets(STDIN));

if (isset($array[$nome1][$nome2][$nome3])) {
    echo $array[$nome1][$nome2][$nome3] . "\n";
}
?>