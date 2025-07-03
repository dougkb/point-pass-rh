from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Middleware de sécurité
app.add_middleware(HTTPSRedirectMiddleware)  # Redirige vers HTTPS si activé
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # à restreindre en prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "127.0.0.1", "*.ngrok.io"]
)

app.include_router(router)
