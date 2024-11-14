dicci = {
    "nombre": "Juan",
    "edad": 28,
    "ciudad": "Madrid",
    "profesion": "Ingeniero",
}
print("Este es el diccionario original:", dicci)

print("\nAccediendo y cambiando valores...")
dicci["edad"] = 32  
dicci["ciudad"] = "Barcelona"  

dicci["email"] = "juan@example.com" 
print("\nDiccionario después de modificarse:") 
print(dicci)