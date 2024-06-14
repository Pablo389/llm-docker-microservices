
# Testing Guide
## Introduction

Este documento explica cómo configurar y ejecutar pruebas para los microservicios `auth-service` y `chat-service`. Utilizamos `pytest` como marco de pruebas.

## Pasos para Configurar y Ejecutar las Pruebas

### 1. Moverse a la Carpeta del Microservicio
Primero, navega a la carpeta del microservicio que deseas probar. Por ejemplo:
```bash
cd auth-service
```

### 2. Crear y Configurar Variables de Entorno
Cada microservicio requiere variables de entorno específicas. Puedes encontrar un archivo de ejemplo (.envexample) en la raíz de cada carpeta del microservicio. Copia este archivo y renómbralo a .env:
```bash
cp .envexample .env
```

### 3. Crear y Activar un Entorno Virtual
Crea un entorno virtual en la carpeta del microservicio:
```bash
python -m venv venv
```

### Activa el entorno virtual:
En Windows:
```bash
venv\Scripts\activate
```

En macOS y Linux:
```bash
source venv/bin/activate
```
### 4. Instalar los Requisitos
Con el entorno virtual activado, instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```
### 5. Ejecutar Pytest
Finalmente, ejecuta las pruebas utilizando pytest:

```bash
pytest
```