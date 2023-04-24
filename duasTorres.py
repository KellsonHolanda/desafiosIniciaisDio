entrada = input('Digite a distância, o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman: ').split(', ')
distancia = float(entrada[0])
diametro1 = float(entrada[1])
diametro2 = float(entrada[2])
ICM = distancia/(diametro1+diametro2)

print(f"O  ICM da comunicação é: {ICM:.2f}")
