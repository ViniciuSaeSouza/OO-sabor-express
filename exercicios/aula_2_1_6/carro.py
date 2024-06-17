from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas) -> None:
        super().__init__(marca, modelo)
        self.portas = portas
        
    def __str__(self) -> str:
        status = "Ligado✅" if self._ligado else "Desligado❌"
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Tipo: {self.portas} | Status: {self._ligado}'