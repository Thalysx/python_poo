class Carro:
    def __init__(self, modelo, marca, cor, consumo_medio, odometro, tanque):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.consumo_medio = consumo_medio
        self.odometro = odometro
        self.tanque = tanque
        self.motor_ligado = False

    def ligar(self):
        self.motor_ligado = True
        print(f'O motor do carro {self.modelo} está ligado.')

    def desligar(self):
        self.motor_ligado = False
        print(f'O motor do carro {self.modelo} está desligado.')

    def acelerar(self, velocidade, tempo):
        if not self.motor_ligado:
            print('O motor precisa estar ligado para acelerar.')
            return
        distancia = velocidade * tempo
        self.odometro += distancia
        consumo = distancia / self.consumo_medio
        self.tanque -= consumo
        if self.tanque < 0:
            self.tanque = 0
        print(f'O carro {self.modelo} acelerou por {distancia} km.')

    def __str__(self):
        return (f'Modelo: {self.modelo}\n'
                f'Marca: {self.marca}\n'
                f'Cor: {self.cor}\n'
                f'Odômetro: {self.odometro} km\n'
                f'Tanque: {self.tanque} litros')

def operar_carro(carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opções [1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

if __name__ == "__main__":
    print('Cadastre um carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    kms = float(input('Digite quantos Kms: '))
    consumo_medio = float(input('Digite o consumo médio (km/l): '))
    tanque = float(input('Digite a quantidade de combustível no tanque (litros): '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, consumo_medio, kms, tanque)

    print('Cadastre outro carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    kms = float(input('Digite quantos Kms: '))
    consumo_medio = float(input('Digite o consumo médio (km/l): '))
    tanque = float(input('Digite a quantidade de combustível no tanque (litros): '))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, consumo_medio, kms, tanque)

    '''
    Controlando o carro até ele atingir 600 Km
    '''
    while carro1.odometro < 600 and carro2.odometro < 600:
        try:
            op = 0
            while op not in (1, 2):
                op = int(input("Qual carro? [1,2]? "))

            if op == 1:
                operar_carro(carro1)
            else:
                operar_carro(carro2)

            print('Infos atuais dos carros:')
            print(carro1)
            print(carro2)
        except Exception as e:
            print("Erro!")
            print(e)

    carro1.desligar()
    carro2.desligar()
    print(carro1)
    print(carro2)
