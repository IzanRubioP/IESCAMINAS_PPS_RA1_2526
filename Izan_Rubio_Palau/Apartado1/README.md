# Práctica Puntuable RA1 – PPS 25_26

## Apartado 1

Se ha desarrollado una aplicación sencilla en **Python** relacionada con la **ciberseguridad**, concretamente con la verificación de integridad mediante **hashes criptográficos**.  
El proyecto incluye además **cuatro tests unitarios** que validan el correcto funcionamiento de la lógica principal.

## Descripción de la aplicación

La aplicación permite calcular el **hash SHA-256** de un archivo y, opcionalmente, compararlo con un hash previo facilitado por el usuario.  
Su objetivo es determinar si un archivo ha sido modificado entre dos momentos diferentes.

El uso de funciones hash criptográficas es un mecanismo habitual en ciberseguridad, ya que permite:

- Identificar cualquier alteración en un archivo, incluso mínima.  
- Garantizar la integridad de descargas.  
- Comprobar que un archivo o aplicación no ha sido manipulado.  
- Comparar versiones de archivos sin necesidad de inspeccionar su contenido.

## Utilidad de la aplicación

Esta herramienta resulta especialmente útil en tareas de seguridad de la información:

- **Detección de modificaciones no autorizadas:**  
  Permite comprobar si un archivo ha sido alterado por accesos indebidos o malware.

- **Verificación de integridad tras descargas:**  
  Muchas organizaciones publican el hash de sus archivos para que los usuarios validen su autenticidad.

- **Comprobación de integridad de aplicaciones:**  
  Ayuda a verificar que un programa sigue siendo idéntico a su versión original.

- **Comparación de versiones:**  
  Permite saber si dos archivos son exactamente iguales sin compararlos manualmente.

## Requisitos

El proyecto utiliza únicamente librerías estándar de **Python**, por lo que no requiere dependencias adicionales para la ejecución de la aplicación.

Requisitos mínimos:

- Python 3.8 o superior  
- Uso de una terminal (CMD, PowerShell o terminal de Visual Studio Code)

## Cómo ejecutar la aplicación

La aplicación principal se encuentra en el archivo `integrity_tool.py`.  
Para ejecutar el verificador de integridad desde la terminal, utiliza:

```bash
python integrity_tool.py
```

El programa solicitará:

La ruta del archivo a verificar.

Un hash previo (opcional) para comparar con el hash calculado.

Si no se proporciona un hash previo, el programa mostrará el hash calculado para que pueda guardarse y usarse en futuras comprobaciones.
Si se introduce un hash previo, el programa indicará si el archivo ha sido modificado o se mantiene íntegro.

## Ejemplo de ejecución en terminal

Aquí voy a mostrar, a modo de ejemplo, cómo he verificado un archivo, en mi caso, he creado un archivo llamado **prueba.txt** donde el contenido era "Hola", luego de obtener el hash, le he añadido una "a", pasando a ser "Holaa", y al comprobar el hash nuevo con el antiguo el programa me ha avisado que el archivo ha cambiado.

Aquí un ejemplo más gráfico:

**Con el mensaje "Hola" dentro de prueba.txt:**
```bash
PS F:\Ciberseguridad\Puesta en produccion segura\RA1_Actividad_Puntuable\IESCAMINAS_PPS_RA1_2526> python integrity_tool
=== Verificador de Integridad ===
Ruta del archivo: C:\Users\Nasta\Pictures\prueba.txt
Hash calculado: e633f4fc79badea1dc5db970cf397c8248bac47cc3acf9915ba60b5d76b0e88f
Introduce el hash previo (o deja vacío si no tienes):
Guarda este hash para futuras comprobaciones.
```
**Con el mensaje "Holaa" dentro de prueba.txt:**
```bash
PS F:\Ciberseguridad\Puesta en produccion segura\RA1_Actividad_Puntuable\IESCAMINAS_PPS_RA1_2526> python integrity_tool
=== Verificador de Integridad ===
Ruta del archivo: C:\Users\Nasta\Pictures\prueba.txt
Hash calculado: 5f02704b97c1ea7871de46be3ee8a5fa40530898ad0be2f88c34d3d86d03be28
Introduce el hash previo (o deja vacío si no tienes): e633f4fc79badea1dc5db970cf397c8248bac47cc3acf9915ba60b5d76b0e88f
El archivo ha cambiado.
```
En este ejemplo, el hash calculado no coincide con el hash previo introducido, por lo que la aplicación detecta correctamente que el archivo ha sido modificado.

## Tests unitarios

El archivo `test_integrity_tool.py` contiene 4 tests unitarios que validan el comportamiento de la función `calcular_hash`.

Los tests comprueban:

1. Cálculo correcto del hash de un archivo existente.

1. Manejo de archivos inexistentes.

1. Hash de archivos vacíos.

1. Detección de diferencias entre archivos con contenido distinto.

### Instalación de pytest

Es necesario para realizar los tests, en caso de no estar instalado, lo añadiremos mediante:

```bash
pip install pytest
```

### Ejecución de los test unitarios

Para ejecutar los tests en modo detallado, utilizaremos:

```bash
pytest test_integrity_tool.py --verbose
```
Si todo funciona correctamente, los cuatro tests aparecerán en estado PASSED.

## Conclusión

La verificación de integridad de archivos es un control de seguridad fundamental.
Este script demuestra cómo implementar un sistema de detección de modificaciones no autorizadas mediante **hashes criptográficos** de forma sencilla y efectiva.
La inclusión de tests unitarios garantiza que la funcionalidad permanezca correcta ante futuros cambios en el código.

## Autor

**Izan Rubio Palau**

Estudiante del módulo PPS 25_26