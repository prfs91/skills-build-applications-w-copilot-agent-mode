from pymongo import MongoClient

try:
    # Conectar ao MongoDB
    client = MongoClient("mongodb://127.0.0.1:27018", serverSelectionTimeoutMS=5000, connectTimeoutMS=5000)
    # Testar a conexão
    client.server_info()
    print("Conexão com o MongoDB bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
