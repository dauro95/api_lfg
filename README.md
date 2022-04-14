# Reto Final - API LFG (Looking For Groups)

#### Tabla de contenido

- [1. Descripción](#1-descripción)
- [2. Requisitos Funcionales](#2-requisitos-funcionales)
- [3. Objetivos](#3-objetivos)
- [4. Stack Tecnológico](#4-stack-tecnológico)
- [5. Cómo usar la aplicación](#5-cómo-usar-la-aplicación)
- [6. Evidencias de consecución](#6-Evidencias-consecucion)


## 1. Descripción

[⬆ Volver al índice](#tabla-de-contenido)

Se trata de la cración de un api BackEnd desarrollado en DjangoRest definida en el reto final del bootcamp Python

## 2. Requisitos Funcionales

[⬆ Volver al índice](#tabla-de-contenido)

Los requisitos funcionales de la aplicación son los siguientes:

1. **RF** - Los usuarios se tienen que poder registrar a la aplicación, estableciendo un usuario/contraseña.
1. **RF** - Los usuarios tienen que autenticarse a la aplicación haciendo login.
1. **RF** - Los usuarios tienen que poder crear Parties (grupos) por un determinado videojuego.
1. **RF** - Los usuarios tienen que poder buscar Parties seleccionando un videojuego.
1. **RF** - Los usuarios pueden entrar y salir de una Party.
1. **RF** - Los usuarios tienen que poder enviar mensajes a la Party. Estos mensajes tienen que poder ser editados y borrados por su usuario creador.
1. **RF** - Los mensajes que existan a una Party se tienen que visualizar como un chat común.
1. **RF** - Los usuarios pueden introducir y modificar sus datos de perfil, por ejemplo, su usuario de Steam.
1. **RF** - Los usuarios tienen que poder hacer logout de la aplicación web.

## 3. Objetivos

[⬆ Volver al índice](#tabla-de-contenido)

Realizar una API REST completa, con Django, que cumpla con los requisitos anteriormente planteados.

Que además proporcione y asegure:

- Registro de usuarios.
- Login de usuarios, auth + token.
- CRUD de los diferentes modelos.
- Excelente Readme (IMPORTANTE).

Y como preferidos:

- Buen naming en las variables.
- Aplicación de buenas prácticas.

## 4. Stack Tecnológico

[⬆ Volver al índice](#tabla-de-contenido)

Para el desarrollo de la API utilizaremos PostgreSQL con Django:

- PostgreSQL.
- Python (3.6 o superior).
- VirtualEnv propio.
- Django para la estructura de proyecto.
- Django Rest Framework encargado de la serialización de objetos JSON.
- JWT.

Como Sistema Control de Versiones se utilizará Git, hosteado en Github, haciendo uso de Git-Flow.
o)

## 5. Como usar la aplicacion
[⬆ Volver al índice](#tabla-de-contenido)
### Ejecutar la aplicación
[⬆ Volver al índice](#tabla-de-contenido)

```shell
python -m django apibook/manager.py runserver
```
### Desde la API
[⬆ Volver al índice](#tabla-de-contenido)

Una vez iniciada la aplicación con `... runserver`

`http://localhost:8000/{entidad}`

## 6. Evidencias consecución
[⬆ Volver al índice](#tabla-de-contenido)

![image](https://user-images.githubusercontent.com/77200841/163490359-5a52a5f4-1922-4c2d-8fb1-856ef8619081.png)
![image](https://user-images.githubusercontent.com/77200841/163490374-d3e4410c-2176-40f3-9e9e-634e8ad3d789.png)
![image](https://user-images.githubusercontent.com/77200841/163490397-37b194ae-5988-4d00-a4e4-3c0ff71ca496.png)
![image](https://user-images.githubusercontent.com/77200841/163490406-887d6e4f-391a-4c20-848d-d22cfba7bb8a.png)
![image](https://user-images.githubusercontent.com/77200841/163490421-72597d7b-3357-4b94-b0c9-85ebc9a1cb66.png)
![image](https://user-images.githubusercontent.com/77200841/163490434-378bd4a1-0dee-42ad-84fc-581a3a01798b.png)
![image](https://user-images.githubusercontent.com/77200841/163490444-a2440589-fe92-43a3-a62f-2755650dafce.png)












