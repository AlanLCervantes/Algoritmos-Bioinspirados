import random

class Patogeno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.peligrosidad = random.randint(1, 10)  # Peligrosidad del patógeno

class CelulaInmunitaria:
    def __init__(self, tipo):
        self.tipo = tipo
        self.fuerza = random.randint(5, 15)  # Fuerza de la célula inmunitaria

    def atacar(self, patogeno):
        print(f"{self.tipo} ataca a {patogeno.nombre} (Peligrosidad: {patogeno.peligrosidad})")
        if self.fuerza >= patogeno.peligrosidad:
            print(f"{self.tipo} ha eliminado a {patogeno.nombre}!")
            return True
        else:
            print(f"{patogeno.nombre} ha sobrevivido el ataque!")
            return False

class SistemaInmunologico:
    def __init__(self):
        self.celulas = [CelulaInmunitaria("Linfocito"), CelulaInmunitaria("Macrófago")]

    def detectar_patogeno(self, patogeno):
        print(f"Detectando patógeno: {patogeno.nombre}")
        for celula in self.celulas:
            if celula.atacar(patogeno):
                return
        print(f"{patogeno.nombre} sigue causando problemas...")

def simular():
    # Crear una lista de patógenos
    patogenos = [Patogeno("Virus A"), Patogeno("Bacteria B"), Patogeno("Hongo C")]
    
    sistema_inmunologico = SistemaInmunologico()
    
    for patogeno in patogenos:
        sistema_inmunologico.detectar_patogeno(patogeno)

if __name__ == "__main__":
    simular()
