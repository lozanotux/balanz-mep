"""
Este script en Python 3 le ayuda a calcular la cantidad total de pesos
argentinos a utilizar para comprar dólares MEP.

Autor: Juan Lozano <lozanotux@gmail.com>
Version: 1.0
Fecha: 11-NOV-2024
"""
# -----------------------------
# Seccion de Imports
# -----------------------------
import requests

# -----------------------------
# Logica
# -----------------------------
def get_tipo_cambio_mep():
    """
    Esta funcion devuelve el tipo de cambio del dolar MEP para la compra.

    Returns:
        float: El valor del precio de compra del dolar MEP.
    """
    base_api_url = "https://dolarapi.com/v1"
    operation_uri = "/dolares/bolsa"

    try:
        response = requests.get(base_api_url + operation_uri)
        return float(response.json()['compra'])
    except Exception:
        print("Error al obtener precio de compra de dolar MEP :(")
        exit(1)


# Formatear la salida manualmente
def formatear_pesos(monto):
    return f"{monto:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


dolares = int(input("Ingrese la cantidad de dólares que desea comprar: "))
comision = 0.0061  # Comisión del 0.61% en cada movimiento
tc_mep = get_tipo_cambio_mep()

# Calcular el monto en dólares considerando las comisiones
total_dolares = dolares * (1 + 2 * comision)

# Calcular el monto en pesos argentinos
total_pesos = total_dolares * tc_mep
pesos = formatear_pesos(total_pesos)

# Imprimir el resultado
print(
    f'\n[INFO] Para comprar {dolares} dólares, necesitas '
    f'aproximadamente $ {pesos} pesos argentinos.\n'
)