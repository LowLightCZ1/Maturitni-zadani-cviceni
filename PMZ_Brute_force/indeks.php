<?php

function bruteForce(string $targetHash, string $charset, int $maxLength): ?string{
    for($length = 1; $length <= $maxLength; $length++){
        $result = tryAllComb($targetHash, $charset, $length);
        if($result !== null) return $result;
    }
    return null;
}



function tryAllComb(string $hash, string $charset, int $length, string $current = ""): ?string{
    if(strlen($current) == $length){
        return md5($current) == $hash ? $current : null;
    }

    for($i = 0; $i < strlen($charset); $i++){
        $result = tryAllComb($hash, $charset, $length, $current . $charset[$i]);
        if($result !== null) return $result;
    }
    return null;
}

$targetHash = "5c4c3d6b1e6c7c0c5a5f9e3c6f4e3c0d";

$lowercase  = "abcdefghijklmnopqrstuvwxyz";         // 26
$uppercase  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";         // 26
$digits     = "0123456789";                          // 10
$symbols    = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~\"\\"; // 32

// Combine as needed
$charset = $lowercase . $digits;                     // 36 chars
$charset = $lowercase . $uppercase . $digits;        // 62 chars
$charset = $lowercase . $uppercase . $digits . $symbols; // 94 chars

$found = bruteForce($targetHash, $charset, 4);
echo $found ? "Found :$found" : "Not found";




?>