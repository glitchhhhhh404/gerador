##!/usr/bin/python
#By PoisonBR

import urllib.request,json

#APIs
pessoa=urllib.request.urlopen("https://randomuser.me/api/1.2/?nat=br"); pessoa=json.loads(pessoa.read())
cpf=urllib.request.urlopen("http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141"); cpf=json.loads(cpf.read())

cpf=cpf['data']['number_formatted']
genero=pessoa["results"][0]["gender"]
if genero == "female":
 genero=genero.replace('female', 'Mulher')
else:
 genero=genero.replace('male', 'Homem')
pnome=pessoa["results"][0]["name"]["first"]
sobrenome=pessoa["results"][0]["name"]["last"]
nome=pnome+" "+sobrenome
nascimento=pessoa["results"][0]["dob"]["date"][0:10]
d=nascimento.split("-")[2]
m=nascimento.split("-")[1]
a=nascimento.split("-")[0]
nascimento=d+"/"+m+"/"+a
idade=pessoa["results"][0]["dob"]["age"]
email=pnome+"."+sobrenome.replace(' ', '.')+"@outlook.com"
email=email.lower().encode('ascii', 'ignore').decode('ascii')
cidade=pessoa["results"][0]["location"]["city"]
estado=pessoa["results"][0]["location"]["state"]
telefone=pessoa["results"][0]["cell"]
print("""
Genero: {}
Nome: {}
Idade: {}
Nascimento: {}
CPF: {}
E-Mail: {}
Telefone: {}
Cidade: {}
Estado: {}
""".format(genero,nome,idade,nascimento,cpf,email,telefone,cidade,estado))
