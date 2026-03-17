def function_register(id_product, product_name, unit_price):
    product = (id_product, product_name, unit_price)
    return product

print("="*50)
print("Bienvenido, a la seccion de regitrar productos...")
print("="*50)

if __name__ == "__main__":
    n = int(input("cuantos productos desea registar: "))
    for i in range(n):
        print(f"-----------Producto #{i+1}-----------")
        id_product = int(input(f"ingrese el ID del producto: "))
        product_name = input(f"ingrese el nombre del producto:  ")
        unit_price = float(input(f"ingrese el ID del producto:  "))
        product = function_register(id_product, product_name, unit_price)
        print("="*50)
        print("¡Registros completados!")
        print(f"producto registrado: {product} ")
        print("="*50)

function_register(id_product, product_name, unit_price)