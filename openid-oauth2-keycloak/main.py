import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="chave_super_secreta_da_aula")

os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'

oauth = OAuth()

CONF_URL = 'http://localhost:9090/realms/aula-seguranca/.well-known/openid-configuration'

oauth.register(
    name='keycloak',
    client_id='fastapi-app',
    client_secret='COLE O SEU SECRET AQUI',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid profile email',
        'code_challenge_method': 'S256'
    }
)

@app.get("/login")
async def login(request: Request):
    redirect_uri = 'http://localhost:8080/callback'
    return await oauth.keycloak.authorize_redirect(request, redirect_uri)


@app.get("/callback")
async def callback(request: Request):
    token = await oauth.keycloak.authorize_access_token(request)
    
    user_info = token.get('userinfo')
    if not user_info:
        user_info = await oauth.keycloak.userinfo(token=token)
        
    print("\n" + "="*50)
    print("🚀 [BACK-CHANNEL] SUCESSO! TOKENS RECEBIDOS")
    print("🔑 ACCESS TOKEN:\n", token.get('access_token'))
    print("-" * 50)
    print("📜 ID TOKEN (JWT):\n", token.get('id_token'))
    print("="*50 + "\n")
    
    request.session['user_name'] = user_info.get('name') or user_info.get('preferred_username', 'Usuário')
    request.session['user_email'] = user_info.get('email', 'Sem e-mail')
    
    response = RedirectResponse(url="/")
    
    response.set_cookie(
        key="id_token_seguro", 
        value=token.get('id_token'), 
        httponly=True
    )
    
    return response


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    user_name = request.session.get('user_name')
    
    if not user_name:
        return '<h1>Autenticação com Authlib</h1><a href="/login">Fazer login no Keycloak</a>'
    
    user_email = request.session.get('user_email')
    
    html = f"""
    <div style="font-family: sans-serif; max-width: 800px; margin: auto;">
        <h1>Bem-vindo, {user_name}!</h1>
        <p>E-mail validado pelo Keycloak: {user_email}</p>
        
        <hr style="margin: 30px 0;">
        
        <h2>Onde estão os Tokens?</h2>
        
        <div style="background-color: #fff3cd; padding: 20px; border-left: 5px solid #ffc107; margin-bottom: 20px;">
            <p>Os tokens gerados pelo Keycloak ultrapassaram o limite de 4KB permitido para cookies nos navegadores.</p>
            <p>Para o sistema não quebrar, nós os interceptamos no <i>Back-channel</i>. <b>Abra o terminal do seu servidor Python e veja os tokens lá!</b></p>
        </div>
        
        <br>
        <a href="/logout" style="padding: 10px 15px; background: #dc3545; color: white; text-decoration: none; border-radius: 5px;">Sair do sistema</a>
    </div>
    """
    return html


@app.get("/logout")
async def logout(request: Request):
    id_token = request.cookies.get("id_token_seguro")
    
    request.session.clear()
    
    if id_token:
        logout_url = (
            f"http://localhost:9090/realms/aula-seguranca/protocol/openid-connect/logout"
            f"?post_logout_redirect_uri=http://localhost:8080/"
            f"&id_token_hint={id_token}"
        )
        response = RedirectResponse(url=logout_url)
    else:
        response = RedirectResponse(url="/")
        
    response.delete_cookie("id_token_seguro")
    
    return response
