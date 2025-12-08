import unittest
import os
from integrity_tool import calcular_hash

class TestCalcularHash(unittest.TestCase):

    def setUp(self):
        # Crear archivos temporales para las pruebas
        with open("archivo_vacio.txt", "w") as f:
            pass
        with open("archivo1.txt", "w") as f:
            f.write("Contenido de prueba 1")
        with open("archivo2.txt", "w") as f:
            f.write("Contenido de prueba 2")

    def tearDown(self):
        # Eliminar archivos creados después de las pruebas
        for nombre in ["archivo_vacio.txt", "archivo1.txt", "archivo2.txt"]:
            if os.path.exists(nombre):
                os.remove(nombre)

    def test_hash_archivo_existente(self):
        """Comprobar que se calcula correctamente el hash de un archivo existente."""
        hash1 = calcular_hash("archivo1.txt")
        self.assertIsInstance(hash1, str)
        self.assertEqual(len(hash1), 64)  # SHA-256 genera 64 caracteres hexadecimales

    def test_archivo_inexistente(self):
        """Comprobar que se devuelve None si el archivo no existe."""
        self.assertIsNone(calcular_hash("archivo_inexistente.txt"))

    def test_hash_archivo_vacio(self):
        """Comprobar que el hash de un archivo vacío es correcto y de longitud 64."""
        hash_vacio = calcular_hash("archivo_vacio.txt")
        self.assertIsInstance(hash_vacio, str)
        self.assertEqual(len(hash_vacio), 64)

    def test_hash_diferente_entre_archivos(self):
        """Comprobar que archivos con distinto contenido generan hashes diferentes."""
        hash1 = calcular_hash("archivo1.txt")
        hash2 = calcular_hash("archivo2.txt")
        self.assertNotEqual(hash1, hash2)

if __name__ == "__main__":
    unittest.main()
