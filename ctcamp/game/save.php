<?php

if(!isset($_POST["Savedata"]) || !isset($_POST["SavedataName"]))
{
  echo ("NO DATA RECIEVED");
  return;
}

$file = $_POST["SavedataName"];
$Savedata = $_POST["Savedata"];

echo $file;
echo "\n";
echo $Savedata;


$newFile = fopen($file, 'w+');

echo $newFile;

fwrite($newFile, $data);
fclose($newFile);

?>
