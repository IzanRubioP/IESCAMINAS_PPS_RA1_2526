#!/bin/bash

# Autor: Izan Rubio Palau
# Script para mostrar información del sistema para la actividad del apartado 2

# Descripción:
# Este script sirve para mostrar en un mensaje único la información del sistema.
# El script está hecho en bash y solo se podrá ejecutar en entornos Linux.

# MAC del equipo
MAC=$(ip link show | awk '/ether/ {print $2; exit}')

# Sistema Operativo
SO=$(uname -a)

# Nombre del host
HOSTNAME=$(hostname)

# Usuario
USUARIO=$(whoami)

# Mostrar mensaje único con toda la información
echo "Información del sistema:"
echo "-------------------------------------------"
echo "Usuario: $USUARIO"
echo "Equipo (Hostname): $HOSTNAME"
echo "Dirección MAC: $MAC"
echo "Sistema Operativo: $SO"
echo "-------------------------------------------"
