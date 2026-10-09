from datetime import datetime
pacotes1=1500000
pacotes2=2000000
agora=datetime.now()
print("="*40)
print(f"{'RELATORIO DE REDE':^40}")
print("="*40)

print("servidor:servidor01")
print(f"{'IP':<15}{'STATUS':<10}{'LATÊNCIA':<10}")
print(f"{'192.168.0.1':<15}{'ONLINE':<10}{'10.25 ms'}")
print(f"Pacotes processados:{pacotes1:,}\n")
print("servidor:servidor02")
print(f"{'IP':<15}{'STATUS':<10}{'LATÊNCIA':<10}")
print(f"{'192.168.0.10':<15}{'OFFLINE':<10}{'15.78 ms'}")
print(f"Pacotes processados:{pacotes2:,}\n")
print("servidor:servidor03")
print(f"{'IP':<15}{'STATUS':<10}{'LATÊNCIA':<10}")
print(f"{'192.168.0.20':<15}{'ONLINE':<10}{'-'}")
print(f"Pacotes processados:{'-'}\n")

print(f"Data de verificação: {agora.strftime('%d/%m/%y')}")
print(f"Horario: {agora.strftime('%H:%M:%S')}")


