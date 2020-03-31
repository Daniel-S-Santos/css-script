from selenium import webdriver
from flask import Flask
import re
import json

app = Flask(__name__)

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver")


driver.get("https://lojaseletromais.vteximg.com.br/arquivos/main.css")
content = driver.page_source

corNome = re.findall('(?<=skuespec_)(.*)(?={)',content)
arquivoNome = re.findall('(?<=/arquivos/)(.*)(?=")',content)


CssNome = []
arquivo = []
arquivos = []
ress = []

for item in corNome:
    z = re.sub('\s','',item)    
    CssNome.append(z)
CssNome.pop(0)
for item in arquivoNome:
    arquivo.append(item)


for index, i in enumerate(CssNome):    
    arquivos.append({"Nome":i,"Arquivo":arquivo[index]})


res = json.dumps(arquivos)

@app.route("/arquivo/css")
def reqArquivos():    
    return res


if __name__ == "__main__":
    app.run(host="10.1.2.84",port=3788,debug=True)
