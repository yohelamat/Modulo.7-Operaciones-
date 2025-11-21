Calculadora Módulo 7 (Programación III)

Este repositorio contiene una aplicación de calculadora básica desarrollada en Python. El objetivo principal es demostrar la modularización del código mediante la separación de la lógica de las operaciones matemáticas en un módulo dedicado.

Objetivo y Contexto

Esta aplicación fue creada como parte de las actividades del Módulo 7 de Programación III.

Estructura del Proyecto

El proyecto está compuesto por dos archivos clave:
Operaciones.py: El módulo que define las funciones esenciales de la calculadora (sumar, restar, multiplicar, dividir). Este archivo es el componente central de la lógica matemática y está diseñado para ser reutilizado.
main.py: El script principal que orquesta la interacción con el usuario. Se encarga de la entrada de datos, importa el módulo Operaciones.py y presenta el resultado.

Funcionalidad

El flujo de uso de la calculadora es el siguiente:
Solicitud de Entrada: El programa pedirá al usuario que ingrese dos valores numéricos (tanto enteros como decimales son aceptados).
Selección de Operación: Se presentarán opciones para elegir entre suma, resta, multiplicación o división.
Cálculo: El script main.py utiliza la función correspondiente del módulo Operaciones.py para obtener el resultado.
Resultado: El resultado final se imprime por pantalla.


Nota Importante:

La aplicación está diseñada para un solo uso. Tan pronto como el usuario realiza la operación y ve el resultado, el programa finaliza. Si se desea realizar otra operación, debe ejecutarse nuevamente.
