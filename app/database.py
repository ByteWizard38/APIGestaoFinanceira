from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

# Credenciais do mongoDB ATLAS
uri = "mongodb+srv://heitorocosta:rdjA1M8I3vggWEaL@cluster0.58oyysf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Conectando com a API do banco de dados
client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))

db = client.GerenciamentoFinanceiro

async def ping():
    try:
        await db.command('ping')
        print("Connected to MongoDB!")
    except Exception as e:
        print(e)
