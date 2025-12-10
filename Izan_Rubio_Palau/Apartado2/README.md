# Práctica Puntuable RA1 – PPS 25_26

## Apartado 2

En este apartado se ha desarrollado un **script en Bash** cuyo objetivo es obtener información esencial del sistema donde se ejecuta.  
La práctica indica que todos los datos deben mostrarse en un único mensaje en la consola, y que el script debe funcionar en un entorno Linux.  
Para cumplir estos requisitos, se ha ejecutado y probado dentro de WSL (Windows Subsystem for Linux).

## Descripción del script

El script `info_equipo.sh` recopila cuatro datos importantes del sistema:

- **Dirección MAC** del equipo.
- **Sistema operativo** en el que se está ejecutando el script.
- **Nombre del equipo (hostname).**
- **Usuario actual** que ha lanzado el script.

Toda esta información se muestra de forma organizada en un único bloque en la consola.

## Utilidad del script

Este tipo de script es útil en diferentes ámbitos de administración y ciberseguridad:

- Identificar de qué máquina proviene una ejecución concreta.
- Obtener información básica del sistema para auditorías.
- Documentar o registrar características del entorno en tareas de despliegue.
- Automatizar procesos que necesiten conocer datos del sistema antes de ejecutarse.

## Requisitos

Para ejecutar este script se requiere:

- Un entorno **GNU/Linux** o **WSL (Windows Subsystem for Linux).**
- Intérprete **Bash**, disponible por defecto en cualquier distribución Linux.
- Permisos para ejecutar scripts.

## Contenido del apartado

El archivo que he incluido para este apartado es:

- `info_equipo.sh`  

## Cómo ejecutar el script

1. Abrir una terminal de Linux o WSL
2. Navegar al directorio donde se encuentra el script:
   ```bash
   cd ruta/al/archivo/apartado2
   ```
3. Asignar permisos de ejecución:
   ```bash
   chmod +x info_equipo.sh
   ```
4. Ejecutar el script:
   ```bash
   ./info_equipo.sh
   ```

## Ejemplo de ejecución en terminal
Aquí se muestra un ejemplo real del script ejecutado desde WSL:
```bash
Información del sistema:
-------------------------------------------
Usuario: izan
Equipo (Hostname): DESKTOP-XXXX
Dirección MAC: 00:15:5d:ab:23:91
Sistema Operativo: Linux DESKTOP-XXXX 5.15.133.1-microsoft-standard-WSL2 x86_64 GNU/Linux
-------------------------------------------
```
Este resultado confirma que el script recoge correctamente todos los datos solicitados y los muestra en un único mensaje.

## Conclusión

Este apartado demuestra el uso de **Bash** para recopilar información básica del sistema de forma automatizada.  
El script funciona correctamente en WSL y cumple con los requisitos del ejercicio, mostrando de forma clara y estructurada todos los valores solicitados.

## Autor

**Izan Rubio Palau**

Estudiante del módulo PPS 25_26