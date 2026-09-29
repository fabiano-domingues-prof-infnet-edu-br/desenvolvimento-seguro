from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head><title>Cabeçalhos de Segurança em FastAPI</title></head>
        <body><h1>Página protegida com múltiplos cabeçalhos HTTP</h1></body>
    </html>
    """