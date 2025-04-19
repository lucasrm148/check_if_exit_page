import os
def create_file(file_path, content):
    with  open(file_path,'w') as arquivo:
        arquivo.write(content)
        arquivo.close()

def add_line(file_path, content):
    with open(file_path, "a") as arquivo:
        arquivo.write(content)


def check_if_file_exis(file_path):
    return os.path.exists(file_path)

def get_all_files_dir(dir_path):
    arquivos = os.listdir(dir_path)
    return arquivos

def padroniza_file_name(file_name):
    file_name = file_name.replace(" ", "%20")
    file_name_list = file_name.split("_")
    return file_name

