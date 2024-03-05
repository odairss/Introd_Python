def add_in_list(names):
    arquivos = list()
    for nome in names:
        arquivos.append(open(nome,'r'))
    return arquivos

def write_big_file(files):
    grande_arquivo = open('grande_arquivo.txt', 'w')
    for arquivo in files:
        for linha in arquivo.readlines():
            grande_arquivo.write(linha)
    grande_arquivo.close()
    

def close_files(files):
    for arquivo in files:
        arquivo.close()

def write_files_in_big_file(names_files):
    args = add_in_list(names_files)
    write_big_file(args)
    close_files(args)
