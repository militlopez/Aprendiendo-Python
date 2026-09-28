"""Sugerencias de películas.

Pide el nombre, el género favorito y un rating mínimo, y sugiere
las películas de la lista que cumplan con esos criterios.
"""

# Cada película: [nombre, género, año, rating]
PELICULAS = [
    ["Rápidos y Furiosos", "Acción", 2001, 6.8],
    ["Troya", "Acción", 2004, 7.3],
    ["Terminator 2", "Acción", 1991, 8.6],
    ["¿Y dónde está el piloto?", "Comedia", 1980, 7.7],
    ["Resident Evil: Noche cero", "Terror", 2026, 7.7],
    ["Coco", "Animación", 2017, 8.4],
    ["Toy Story", "Animación", 1995, 8.3],
    ["Shrek", "Animación", 2001, 7.9],
    ["El exorcista", "Terror", 1973, 8.1],
    ["¿Y dónde están las rubias?", "Comedia", 2004, 5.8],
    ["Son como niños", "Comedia", 2010, 6.0],
]

GENEROS = ["Acción", "Comedia", "Terror", "Animación", "Drama"]


def mostrar_encabezado():
    print("=====================================")
    print("      SUGERENCIAS DE PELÍCULAS       ")
    print("=====================================\n")


def mostrar_generos():
    print("-------- GÉNEROS --------")
    for genero in GENEROS:
        print(genero)
    print()


def buscar_peliculas(genero_favorito, rating_minimo):
    """Devuelve los nombres de las películas del género con rating >= mínimo."""
    return [
        nombre
        for nombre, genero, _anio, rating in PELICULAS
        if genero.lower() == genero_favorito.lower() and rating >= rating_minimo
    ]


def mostrar_perfil(usuario):
    print("\n--- Perfil de " + usuario["nombre"] + " ---")
    print("Género favorito: " + usuario["genero_fav"])
    print("Películas sugeridas:")
    for nombre in usuario["sugeridas"]:
        print("  - " + nombre)


def main():
    mostrar_encabezado()

    nombre = input("Buen día, ¿cuál es tu nombre? ")
    print("¿Qué querés ver hoy, " + nombre + "?\n")

    mostrar_generos()
    genero_favorito = input("¿Qué género te gusta? ")
    rating_minimo = float(input("¿Cuál es el rating mínimo? "))

    print("Buscando películas del género " + genero_favorito + "...")
    sugeridas = buscar_peliculas(genero_favorito, rating_minimo)

    if not sugeridas:
        print("No se ha encontrado ninguna película.")
        return

    usuario = {
        "nombre": nombre,
        "genero_fav": genero_favorito,
        "sugeridas": sugeridas,
    }
    mostrar_perfil(usuario)


if __name__ == "__main__":
    main()
