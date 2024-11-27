import random

# Opciones del juego y reglas
opciones = ["roca", "fuego", "tijera", "esponja", "papel", "aire", "agua"]
reglas = {
    "roca": ["fuego", "tijera", "esponja"],
    "fuego": ["tijera", "papel", "esponja"],
    "tijera": ["aire", "papel", "esponja"],
    "esponja": ["papel", "aire", "agua"],
    "papel": ["aire", "roca", "agua"],
    "aire": ["fuego", "roca", "agua"],
    "agua": ["roca", "fuego", "tijera"]
}

# Marcador
victorias =0
derrotas = 0

def jugar():
    global victorias, derrotas
    maquina = random.choice(opciones)
    usuario =input(f"Selecciona una opción ({', '.join(opciones)}): ").strip().lower()
       
    if usuario not in opciones:
        print("Opción no válida.")
        return
    
    print(f"Máquina eligió: {maquina}")
    
   
    if usuario == maquina:
        print("¡Empate!")

    elif maquina in reglas[usuario]:
        
        print("¡Ganaste!")
        victorias +=1 
     
    else:
       print("¡Perdiste!")
       derrotas +=1
jugar()
   

def ver_marcador():
    print(f"\nVictorias: {victorias} | Derrotas: {derrotas}")

ver_marcador()

# Programa principal
while True:
    opcion=input("\n1. Jugar\n2. Ver marcador\n3. Salir\nElige una opción: ").strip()
    
 
    if opcion == "1":
        jugar()
 

   
    elif opcion == "2":
        ver_marcador()