from fastapi import FastAPI
from api.routers import users_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(users_router.user_router)

@app.get('/health')
def health_check():
    return {'success': True}
