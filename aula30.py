"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas codições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 #velocidade atual do carro
local_carro = 99 #local em que o carro está na estrada

RADAR_1 = 60 #velocidade máxima do radar
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 #A distancia onde o radar pega

vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_1) and\
    local_carro <= (LOCAL_1 + RADAR_1)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_passou_radar_1

if vel_carro_passou_radar_1:
    print('Você está acima do limite permitido')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('Carro multado em radar 1')