def Calcular_Descuento(monto_total, porcentaje_descuento = 10):
   descuento=(monto_total * porcentaje_descuento) / 100
   return descuento

def main ():

    # Llamadas a la función calcular_descuento
    montocompra1 = 88
    descuento1 = Calcular_Descuento(montocompra1)
    montofinal1 =  montocompra1-descuento1
    print(f"\n Monto total de compra: ${montocompra1}")
    print(f"\n Aplicar el siguiente descuento: ${descuento1}")
    print(f"\n Monto final a pagarse de la compra realizada: ${montofinal1}")

    print("\n ---------------------------->")

    montocompra2=58
    porcentajedescuento2=15
    Descuento2 = Calcular_Descuento(montocompra2, porcentajedescuento2)
    montofinal2=montocompra2-Descuento2

    print(f"\n Monto total de compra: ${montocompra2}")
    print(f"\n Porcentaje de descuento: ${porcentajedescuento2}%")
    print(f"\n Descuento aplicado: ${Descuento2}%")
    print(f"\n Monto final al pagar: ${montofinal2}")


if __name__ == "__main__": main()