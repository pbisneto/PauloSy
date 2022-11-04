# abre o arquivo
entrada = input()
nome_entrada_formatada = 'formatada_' + entrada + '.txt'
abrir = open(entrada, "rt")

# abre o arquivo de saida
abrir_saida = open(nome_entrada_formatada, "wt")

for line in abrir:
    # substitui os caracteres
    abrir_saida.write(line.replace("@", " ").replace("-", "_").replace("!", ""))

# fecha os arquivos que tinha sido abertos
abrir.close()
abrir_saida.close()