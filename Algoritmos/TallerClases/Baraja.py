from dataclasses import dataclass
from enum import Enum
import random
import Individuo


class Pinta(Enum):
    Corazones = 1
    Diamantes = 2
    Treboles = 3
    Espadas = 4


class Valor(Enum):
    A = 1,
    DOS = 2,
    TRES = 3,
    CUATRO = 4,
    CINCO = 5,
    SEIS = 6,
    SIETE = 7,
    OCHO = 8,
    NUEVE = 9,
    DIEZ = 10,
    J = 11,
    K = 12,
    Q = 13


@dataclass
class Carta:
    pinta: Pinta
    valor: Valor

    def __str__(self) -> str:
        print(f"{self.valor.name} de {self.valor.value}")


class Baraja:
    def __init__(self) -> None:
        self.baraja: list[Carta]
        for _ in range(52):
            self.baraja.append(
                Carta(
                    Pinta(random.randint(1, 4)),
                    Valor(random.randint(1, 13))
                )
            )

    def repartir(self) -> Carta:
        carta = random.choice(self.baraja)
        self.baraja.remove(carta)
        return carta

    def __str__(self) -> str:
        print(f"Cartas restantes en la baraja: {len(self.baraja)}")
