from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    csp = (
        "default-src 'self'; "
        "script-src 'self' https://exemplo.com; "
        "style-src 'self' 'unsafe-inline'; "
        "img-src 'self' data: https://images.exemplo.com; "
        "font-src 'self' https://fonts.exemplo.com; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "frame-ancestors 'none';"
    )
    response.headers["Content-Security-Policy"] = csp
    return response

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head><title>Exemplo CSP em FastAPI</title></head>
        <body><h1>Página protegida por CSP</h1></body>
    </html>
    """