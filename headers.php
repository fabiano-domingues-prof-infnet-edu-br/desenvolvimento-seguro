<?php
header("X-Content-Type-Options: nosniff");
header("X-Frame-Options: DENY");
header("X-XSS-Protection: 1; mode=block");
header("Strict-Transport-Security: max-age=31536000; includeSubDomains");
header("Referrer-Policy: strict-origin-when-cross-origin");
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <title>Cabeçalhos de Segurança em PHP</title>
</head>
<body>
    <h1>Página protegida com múltiplos cabeçalhos HTTP</h1>
</body>
</html>