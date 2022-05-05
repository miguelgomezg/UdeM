import random
from enum import Enum
from dataclasses import dataclass
from email.mime import nonmultipart
from select import select
from shutil import register_unpack_format


class Individuo:
    contador: str = 0

    def __init__(self, nb: str) -> None:
        self._nombre: str = nb
        self.feliz: bool = True
        self.__class__.agregar_uno()
        self.id = self.__class__.contador

    @property
    def nombre(self):
        return self._nombre

    def es_feliz(self):
        return self.feliz

    def cambiar_estado_de_animo(self):
        self.feliz = not self.feliz
        return self.feliz

    def hablar(self):
        return f"Hola yo soy {self.nombre}" if self.feliz else "Alejate"

    @classmethod
    def agregar_uno(cls):
        cls.contador += 1

    def __str__(self):
        return f"Individuo [<{self.id}>, <{self.nombre}>]"


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


if __name__ == "__main__":
    alguien = Individuo("Miguel")
    alguien2 = Individuo("Mister")
    alguien.cambiar_estado_de_animo()

    # Individuo.agregar_uno()
    alguien3 = Individuo("Mister3")

    variable: str = "Hola"

    print(alguien.hablar())
    print(alguien2.hablar())
    print(alguien3)
