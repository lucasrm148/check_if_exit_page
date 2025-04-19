
import requests

def check_if_url_exist(url):
        try:
            response = requests.get(url, stream=True,allow_redirects=False)  # stream=True evita carregar o conteúdo inteiro
            if response.status_code == 200 or response.status_code == 302:
                print("O endereço é um arquivo.")
                return True
            else:
                print("O endereço pode não ser um arquivo.")
                return False
        except requests.RequestException as e:
            print("Erro ao acessar o endereço:", e)
            return False

def file_name_process(file):
    file = file.replace(" ", "%20")
    tags = file
    file = file.replace(".pdf", "")
    section = file.split("_")
    
    #tags =tags.replace(".pdf", "")
    if len(section) in [6, 7]:
        cnpj = section[0]
        cpf = section[1]
        nome = section[2].replace(".", "")
        competencia = section[3]
        registro = section[4]
        senha = section[5]
        matriculacontrato = section[6][:-1] if len(section) == 7 else None

        matricula = registro if cnpj != "05294848000194" else matriculacontrato
        new_url = f"/Arquivo/{cnpj}/{competencia}/{cpf}-{nome}/{matricula}/{tags}"
        return new_url
        

        