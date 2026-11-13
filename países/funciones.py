dominio=input("Indicá el dominio que querés conocer: ")
def obtener_pais():
    paises={"ar":"Argentina","br":"Brasil","uy":"Uruguay","cl":"Chile","es":"España","mx":"México","ec":"Ecuador","py":"Paraguay","fr":"Francia"}
    print(paises[dominio])
obtener_pais()