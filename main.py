from analyzer import analisar_logs

resultado = analisar_logs("logs.txt")

print("\nRELATÓRIO")
print("Total linhas:", resultado["total_linhas"])
print("Total erros:", resultado["erros"])
print("IPs únicos:", resultado["ips_unicos"])
print("Top IP:", resultado["top_ip"])
print("Downloads:", resultado["downloads"])




from analyzer import analisar_logs

resultado = analisar_logs("logs.txt")

print(resultado)


