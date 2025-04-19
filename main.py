from re import search
from getFile import *
from FileUpdate import *

url = input("digite a url a ser verificada: ") ##https://forthinformatica.com.br/Arquivo
url_to_search =  input("digite o path de busca: ")
files = get_all_files_dir(url_to_search)

for file in files:
    file = file_name_process(file)
    print(url +  str(file))
    res = check_if_url_exist(url +  str(file))
    if(not res):
        add_line("arquivos_existentes.txt", str(file) + "\n")

