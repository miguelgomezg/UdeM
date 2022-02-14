from datetime import datetime
from Models import (
    Libro,
    Transaccion,
    TipoTransaccion
)


if __name__ == "__main__":
    libro1 = Libro(
        "123456",
        "Prueba",
        2,
        3000,
        5000,
        [
            Transaccion(2, TipoTransaccion.VENTA)
        ]
    )

    print(libro1.isbn)
