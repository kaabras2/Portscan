#!/bin/python3import sys
#
# Programa desenvolvido para atividade da materia Optimization for Security
# Made by: Mateus FArias FErreira RM84559 and a little help from google <3
# 
# Data do começo do projeto: 28/08/2020
# Versão: 2.012
# Data da ultima atualização: 03/09/2020
#
# Tomara que funcione! 
#

# Importar as bibliotecas utilizadas:

import socket,sys

# Printa uma linha nova quando a função é chamada. Coisa de preguiçoso mesmo. 

def nl():print('\n')


# Definir o IP para scanear e o range de portas:

nl()
ip = input("[+] Defina o IP para scanear: ")
nl()
portas = int(input("[+] Defina a porta de inicio: "))
nl()
portaf = int(input("[+] Defina a porta de término: "))

# Baner para organização

nl()
print("~" * 50)
print("Scaneando o IP ~> {}".format(ip))
print("~" * 50)
nl()

# Try para ter as exceptions
# Inicio do trabalho pesado: Para cada porta dentro do range informado, tentar a conexão:

try:
    for port in range(portas, portaf):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        result = s.connect_ex((ip, port)) 

# Deixando o programa mais verboso (por que eu gosto de saber o que está ocorrendo) Print para informar qual porta está sendo scaneada
  
        print("Verificando porta:" +str(port)) 

# Se conectar, o programa irá abrir o arquivo "services" e deixar como uma variavel que eu apelidei de renan (um amigo meu).
# Na variavel renan, o arquivo vai ser splitado por linhas. 
# Setando as linhas como variavel linha, as linhas vão ser splitadas pelo tab (como eu formatei o arquivo)
# Linha 0 - Serviço que roda na porta = campos (campo serviço)
# Linha 1 - porta especificada no arquivo = campop (campo porta)
# 
# Como eu fiquei com preguiça de terminar de formatar o arquivo, fiz o programa terminar de formatar.
# Assim a Linha 1 (campop) retira o /TCP ou /UDP do arquivo, para comparar porta do arquivo com porta da variavel que foi verificada pelo socket.

        if result == 0:
  
            file=open("services")
            renan=file.read()
            renan=renan.split("\n")
            for linha in renan:
                linha=linha.split("\t")
                campos=linha[0]
                campop=linha[1]
                campop=campop.split("/")[0]
                campop=int(campop)
                
                if campop == port:


# Printa a porta e o serviço caso a porta esteja aberta.
                    
                    print("<~ Porta " +str(port)+ " aberta e rodando o serviço: " +str(campos)+ " ~>")
                    break
            file.close()
            
    s.close

# Se o usuario quiser parar o programa com CTRL+C, da a seguinte mensagem e fecha o programa:

except KeyboardInterrupt:
 print("<~ Finalizando Scan/Programa ~>")  
 sys.exit()  

# Se não tiver conexão com o IP, da a seguinte mensagem e fecha o programa:

except socket.gaierror: # Se não tiver conexão com o IP  
 print("<~ Não foi possivel conectar-se ao IP ~>")  
 sys.exit()


