from collections import Counter

def analisar_logs(ficheiro):
    with open(ficheiro, "r") as f:
        linhas = f.readlines()

    total_linhas = len(linhas)

    ips = []
    erros = 0
    downloads = 0

    for linha in linhas:
        partes = linha.strip().split(" - ")

        if len(partes) != 2:
            continue

        ip = partes[0]
        acao = partes[1]

        ips.append(ip)

        if acao == "ERROR":
            erros += 1
        elif acao == "DOWNLOAD":
            downloads += 1

    ip_counter = Counter(ips)

    return {
        "total_linhas": total_linhas,
        "erros": erros,
        "ips_unicos": len(set(ips)),
        "top_ip": ip_counter.most_common(1)[0][0],
        "downloads": downloads
    }



    ok