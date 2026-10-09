from datetime import datetime
agora=datetime.now()
print(f"Data de verificação: {agora.strftime('%d/%m/%y')}")
print(f"Horario: {agora.strftime('%H:%M:%S')}")