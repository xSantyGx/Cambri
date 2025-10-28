# pedidos_data.py
pedidos = [
    {
        "id": 1001,
        "cliente": "Maria Inc.",
        "estado": "Pendiente",
        "contacto": "maria@inc.com",
        "fecha": "2025-10-20",
        "costo": 250000,
        "descripcion": "Pedido de insumos textiles"
    },
    # Más pedidos iniciales opcionales
]

def next_id():
    if pedidos:
        return max(p["id"] for p in pedidos) + 1
    return 1001
