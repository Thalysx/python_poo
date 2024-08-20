class Carro:
    def __init__(self, modelo: str, marca: str, cor: str,
                       odometro: float, tanque: float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.odometro = odometro
        self.tanque = tanque
        self.motor_on = False

    def ligar(self):
        if not self.motor_on:
            self.motor_on = True
            print(f"{self.modelo} está agora ligado.")
        else:
            raise Exception("Erro: Motor já ligado!")

    def acelerar(self, velocidade: float, tempo: float):
        if self.motor_on:
            distancia = velocidade * tempo
            litros_usados = distancia / self.consumo_medio
            if litros_usados <= self.tanque:
                self.odometro += distancia
                self.tanque -= litros_usados
                print(f"{self.modelo} percorreu {distancia:.2f} km. Combustível restante: {self.tanque:.2f} litros.")
            else:
                print(f"Combustível insuficiente para percorrer {distancia:.2f} km.")
        else:
            print(f"{self.modelo} está desligado. Não pode acelerar.")

    def desligar(self):
        if self.motor_on:
            self.motor_on = False
            print(f"{self.modelo} está agora desligado.")
        else:
            raise Exception("Erro: Motor já desligado!")

    def __str__(self):
        return (f"Modelo: {self.modelo}, Marca: {self.marca}, Cor: {self.cor}, "
                f"Odômetro: {self.odometro:.2f} km, Combustível: {self.tanque:.2f} litros")

