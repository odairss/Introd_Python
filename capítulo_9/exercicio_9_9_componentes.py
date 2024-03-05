def adicionar_arquivos_em_lista(names):
    files = list()
    for name in names:
        files.append(open(name, 'r'))
    return files

def imprimir_arquivos(files):
    for file in files:
        print(f"Conteúdo do arquivo {file.name}")
        for line in file.readlines():
            print(line)

def fechar_arquivos(files):
    for file in files:
        file.close()
