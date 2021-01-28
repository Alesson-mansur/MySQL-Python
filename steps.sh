#!/bin/bash

######################################
###         Ambiente da API        ###
######################################

### Verificar os ambientes (environments) presentes no Anaconda:

$ conda info --envs

### Criar um novo environment:

$ conda create --name py3-API python=3

### Para remover um ambiente:

### $ conda env remove --name py3-API

### Ativar o ambiente:

$ conda activate py3-API

### Instalar o MySQL connector:

$ conda install mysql-connector-python

### Verificar as instalações:

$ conda list


###############################################################
####  Os passos seguintes referem-se às bibliotecas da API ####
###############################################################



###  Instalar o Virtualenv

$ conda install virtualenv

### Criar e navegar até a pasta em que a API vai rodar:

$ mkdir 3.FlaskAPI
$ cd 3.FlaskAPI/

### Criar as dependências para o virtualenv: 

$ virtualenv .venv

### Instalar/Adicionar o Flask:

$ conda install flask

### Criar arquivo para adicionar a(s) dependência(s) 
### do flask caso haja alguma outra dependência

$ touch requirements.txt

$ conda list
### Copiar a versão do flask pelo conda list e 
### colar no arquivo requirements.txt no formato flask==X.X.X




##################################################################################################################




#####################################
###             API               ###
#####################################

### Caso não queira usar o Anaconda:

### Instalar o python3 pelo tutorial do link

### Se o python3 e os pacotes não estiverem disponíveis para uso:

$ sudo apt-get install python3-pip

$ pip3 install virtualenv

### Criar e navegar até a pasta em que a API vai rodar:

$ mkdir simple-flask-api
$ cd simple-flask-api/

### Criar as dependências para o virtualenv: 

$ python3 -m virtualenv .venv

### Ativar o virtualenv para não poluir a instalação global do Python:

$ source .venv/bin/activate

### Instalar/Adicionar o Flask:

$ pip3 install flask

### Criar arquivo para adicionar a(s) dependência(s) do flask para o caso de haver alguma outra dependência

$ touch requirements.txt

$ conda list
### Copiar a versão do flask pelo conda list e colar no arquivo requirements.txt no formato flask==X.X.X
