<?php
$csp_rules = [
    "default-src 'self'",
    "script-src 'self' https://exemplo.com",
    "style-src 'self' 'unsafe-inline'",
    "img-src 'self' data: https://images.exemplo.com",
    "font-src 'self' https://fonts.exemplo.com",
    "object-src 'none'",
    "base-uri 'self'",
    "frame-ancestors 'none'"
];
header("Content-Security-Policy: " . implode("; ", $csp_rules));
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <title>Exemplo CSP em PHP</title>
</head>
<body>
    <h1>Página protegida por CSP</h1>
</body>
</html>