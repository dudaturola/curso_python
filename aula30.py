"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas codições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 #velocidade atual do carro
local_carro = 90 #local em que o carro está na estrada

RADAR_1 = 60 #velocidade máxima do radar
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 #A distancia onde o radar pega

if velocidade > RADAR_1:
    print('Você está acima do limite permitido')

if local_carro >= (LOCAL_1 + RADAR_RANGE) and (LOCAL_1 - RADAR_RANGE):
    print('Carro multado em radar 1')