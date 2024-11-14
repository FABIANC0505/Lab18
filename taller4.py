mi_lista = [42, "Hola", 3.14, True, None, [1, 2, 3], {"clave": "valor"}, (5, 6), False, "Python"]
print("Elemento en el índice 1:", mi_lista[1]) 
mi_lista[2] = 7.56
print("Lista después de modificar el tercer elemento:", mi_lista)

mi_lista.append("El Elemento")  
print("La lista después de agregar un nuevo elemento:", mi_lista)
mi_lista.remove("Hola")  
print("Lista después de eliminar un elemento:", mi_lista)