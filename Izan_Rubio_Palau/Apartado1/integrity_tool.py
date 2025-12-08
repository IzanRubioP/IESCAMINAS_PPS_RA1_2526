import hashlib
import os

def calcular_hash(ruta):
    """Devuelve el hash SHA-256 de un archivo o None si no existe."""
    if not os.path.isfile(ruta):
        return None

    sha256 = hashlib.sha256()

    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(4096), b""):
            sha256.update(bloque)

    return sha256.hexdigest()


def main():
    print("=== Verificador de Integridad ===")
    archivo = input("Ruta del archivo: ").strip()

    hash_actual = calcular_hash(archivo)

    if hash_actual is None:
        print("El archivo no existe o no es válido.")
        return

    print(f"Hash calculado: {hash_actual}")

    hash_prev = input("Introduce el hash previo (o deja vacío si no tienes): ").strip()

    if hash_prev:
        if hash_prev == hash_actual:
            print("El archivo no ha sido modificado.")
        else:
            print("El archivo ha cambiado.")
    else:
        print("Guarda este hash para futuras comprobaciones.")


if __name__ == "__main__":
    main()
