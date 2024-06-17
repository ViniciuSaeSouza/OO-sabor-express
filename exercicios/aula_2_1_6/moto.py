from veiculo import Veiculo
class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo) -> None:
        super().__init__(marca, modelo)
        self.tipo = tipo
    
    def __str__(self) -> str:
        status = "Ligado✅" if self._ligado else "Desligado❌"
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Tipo: {self.tipo} | Status: {status}'