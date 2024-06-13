# Auth Service

## Definición

El Auth Service es un microservicio dedicado a la gestión de usuarios y autenticación. Proporciona funcionalidades para registrar nuevos usuarios, iniciar sesión y validar tokens JWT. Este servicio es fundamental para asegurar que solo los usuarios autenticados puedan acceder a otros servicios dentro de la arquitectura de microservicios.

## Endpoints

### Registro de Usuarios

**Endpoint:** `/register`  
**Método:** `POST`  
**Descripción:** Registra un nuevo usuario.

**Solicitud HTTP:**

```bash
curl -X POST "http://localhost:8000/register" -H "Content-Type: application/json" -d '{
    "email": "testuser@example.com",
    "password": "password123"
}'
```

**Respuesta Exitosa (200):**

```
{
    "msg": "User registered successfully"
}
```

**Error (400):**


```
{
    "detail": "Email already registered"
}
```

### Inicio de Sesión

**Endpoint:** `/login`  
**Método:** `POST`  
**Descripción:** Inicia sesión con las credenciales del usuario y obtiene un token de acceso.

**Solicitud HTTP:**

```bash
curl -X POST "http://localhost:8000/login" -H "Content-Type: application/json" -d '{
    "email": "testuser@example.com",
    "password": "password123"
}'
```

**Respuesta Exitosa (200):**

```
{
    "access_token": "your_jwt_token",
    "token_type": "bearer"
}
```

**Error (400):**


```
{
    "detail": "Invalid credentials"
}
```

### Validación de Token

**Endpoint:** `/validate-token`  
**Método:** `GET`  
**Descripción:** Valida un token JWT.

**Solicitud HTTP:**

```bash
curl -X GET "http://localhost:8000/validate-token" -H "Authorization: Bearer your_jwt_token"
```

**Respuesta Exitosa (200):**

```
{
    "sub": "testuser@example.com",
    "user_id": 1
}
```

**Error (400):**


```
{
    "detail": "Token inválido"
}
```