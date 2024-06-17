class Veiculo:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self._ligado = False
        
    def __str__(self) -> str:
        status = "ligado" if self._ligado else "desligado"
        return f'Marca: {self.marca} \nModelo {self.modelo} \nStatus: {status}'
        