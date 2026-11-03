# main.py
from servicios.centro_service import CentroService

service = CentroService()

# Centros

service.crear_centro(
    1,
    "Centro Suba",
    "Suba"
)

service.crear_centro(
    2,
    "Centro Chapinero",
    "Chapinero"
)

service.crear_centro(
    3,
    "Centro Bosa",
    "Bosa"
)

service.crear_centro(
    4,
    "Centro Teusaquillo",
    "Teusaquillo"
)

service.crear_centro(
    5,
    "Centro Soacha",
    "Soacha"
)

# Recorridos

service.registrar_recorrido(
    1,
    2,
    23
)

service.registrar_recorrido(
    1,
    3,
    35
)

service.registrar_recorrido(
    2,
    3,
    29
)

service.registrar_recorrido(
    2,
    4,
    12
)

service.registrar_recorrido(
    3,
    5,
    8
)

service.registrar_recorrido(
    4,
    1,
    24
)

service.registrar_recorrido(
    4,
    5,
    39
)

# Listar centros

print("\n=== CENTROS ORDENADOS ===")

for centro in service.listar_centros():
    print(centro)

# Recorridos de Suba

print("\n=== RECORRIDOS DESDE SUBA ===")

for recorrido in service.listar_recorridos(1):
    print(recorrido)