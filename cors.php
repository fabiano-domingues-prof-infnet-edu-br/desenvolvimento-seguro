<?php
$origem_permitida = "https://meu-frontend-confiavel.com";
header("Access-Control-Allow-Origin: " . $origem_permitida);
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With");
header("Access-Control-Allow-Credentials: true"); 
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit();
}
echo "CORS configurado com sucesso!";
?>