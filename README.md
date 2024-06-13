# LLM Docker Microservices

## Introducción

LLM Docker Microservices es una aplicación basada en microservicios diseñada para proporcionar una arquitectura modular y escalable. La aplicación consta de tres microservicios principales:

1. **Servicio de Autenticación (auth-service)**: Maneja el registro, inicio de sesión y validación de tokens JWT para los usuarios.
2. **Servicio de Chat (chat-service)**: Permite a los usuarios crear chats y enviar mensajes, con integración a OpenAI para generar respuestas automáticas.
3. **Servicio Frontend (frontend-service)**: Una aplicación React que sirve como la interfaz de usuario para interactuar con los servicios de autenticación y chat.

Cada uno de estos servicios está contenido en su propio directorio y se despliega como un contenedor Docker independiente, permitiendo una fácil gestión y escalabilidad.



## Guía de Despliegue

### Prerrequisitos

- Docker
- Docker Compose

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/tuusuario/llm-docker-microservices.git
cd llm-docker-microservices
```

### Paso 2: Crear el Archivo .env
Crea un archivo .env en la raíz del proyecto con las siguientes variables de entorno:

```
POSTGRES_USER=tu_usuario_postgres
POSTGRES_PASSWORD=tu_contraseña_postgres
SECRET_KEY=tu_clave_secreta
ACCESS_TOKEN_EXPIRE_MINUTES=30
OPENAI_API_KEY=tu_clave_api_openai
```


### Paso 3: Desplegar la Arquitectura con Docker Compose
Ejecuta el siguiente comando para iniciar todos los servicios:

```
docker-compose up --build
```

Esto hará lo siguiente:

1. Levantará dos bases de datos PostgreSQL, una para el servicio de autenticación y otra para el servicio de chat.
2. Construirá y desplegará los contenedores para auth-service, chat-service y frontend-service.
3. Configurará las bases de datos usando los scripts SQL proporcionados en sql-scripts.

## Servicios y Puertos

- auth-service: Disponible en http://localhost:8000
- chat-service: Disponible en http://localhost:8001
- frontend-service: Disponible en http://localhost:3000

## Comandos Adicionales
### Detener los servicios:
```
docker-compose down
```

### Ver logs de los servicios:
```
docker-compose logs -f
```

## Contribuciones
Las contribuciones son bienvenidas. Por favor, sigue el flujo de trabajo de Git estándar (fork, branch, commit, pull request).

## Licencia
Este proyecto está licenciado bajo los términos de la MIT License.