#SRS
#RF001: Se necesita que la aplicación transfiera montos entre distintas cuentas a traves de alias/cbu, ingresando el monto a transferir
#       que sea mayor a cero y no supere el monto disponible.          
# HU historias usuario 
# HU-1: Como empresa, quiero rechazar transferencias con monto inválido o mayor al saldo, 
#     para que nadie envíe dinero que no posee.
# HU-2: Como empresa, quiero un límite diario de $200.000 por usuario, 
#     para reducir el riesgo de fraude.
# LISTADO DE CRITERIOS DE ACEPTACION:
# - Dado un acumulado de 100000 $ cuando intento transferir 40000 $ la transferencia se APRUEBA

# constantes
MONTO_INVALIDO="Rechazada: Monto inválido."
SALDO_INSUFICIENTE="Rechazada: Saldo insuficiente."
LIMITE_DIARIO=200000
LIMITE_EXCEDIDO="Rechazada: límite diario excedido."
APROBADA="Transferencia exitosa."

def transferir(saldo,monto,monto_acumulado):
    if monto<=0:
        return MONTO_INVALIDO
    if monto>saldo:
        return SALDO_INSUFICIENTE
    if monto_acumulado+monto>LIMITE_DIARIO:
        return LIMITE_EXCEDIDO
    return APROBADA