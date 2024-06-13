# Chat Service

## Definición

El Chat Service es un microservicio encargado de gestionar las sesiones de chat y los mensajes. Permite crear nuevas sesiones de chat, enviar mensajes y recuperar el historial de chats y mensajes. Este servicio interactúa con OpenAI para generar respuestas automáticas a los mensajes de los usuarios.

## Endpoints

### Crear una Nueva Sesión de Chat

**Endpoint:** `/create-chat`  
**Método:** `POST`  
**Descripción:** Crea una nueva sesión de chat para el usuario autenticado.

**Solicitud HTTP:**

```bash
curl -X POST "http://localhost:8001/create-chat" -H "Authorization: Bearer your_jwt_token"
```

**Respuesta Exitosa (200):**

```
{
    "id": 1,
    "user_id": 1,
    "created_at": "2023-06-01T00:00:00.000Z",
    "messages": []
}
```


### Enviar un Mensaje

**Endpoint:** `/create-message`  
**Método:** `POST`  
**Descripción:** Envía un mensaje en una sesión de chat específica. Si el mensaje es del usuario, el sistema generará una respuesta automática.

**Solicitud HTTP:**

```bash
curl -X POST "http://localhost:8001/create-message" -H "Authorization: Bearer your_jwt_token" -H "Content-Type: application/json" -d '{
    "chat_id": 1,
    "role": "user",
    "content": "This is a test message"
}'
```

**Respuesta Exitosa (200):**

```
{
    "id": 1,
    "chat_id": 1,
    "role": "user",
    "content": "This is a test message",
    "timestamp": "2023-06-01T00:00:00.000Z"
}
```

### Obtener Historial de Chats

**Endpoint:** `/chats`  
**Método:** `GET`  
**Descripción:** Recupera todas las sesiones de chat del usuario autenticado.

**Solicitud HTTP:**

```bash
curl -X GET "http://localhost:8001/chats" -H "Authorization: Bearer your_jwt_token"

```

**Respuesta Exitosa (200):**

```
[
    {
        "id": 1,
        "user_id": 1,
        "created_at": "2023-06-01T00:00:00.000Z",
        "messages": []
    }
]
```

### Obtener Mensajes de un Chat Específico

**Endpoint:** `/messages/{chat_id}`  
**Método:** `GET`  
**Descripción:** Recupera todos los mensajes de una sesión de chat específica.

**Solicitud HTTP:**

```bash
curl -X GET "http://localhost:8001/messages/1" -H "Authorization: Bearer your_jwt_token"
```

**Respuesta Exitosa (200):**

```
[
    {
        "id": 1,
        "chat_id": 1,
        "role": "user",
        "content": "This is a test message",
        "timestamp": "2023-06-01T00:00:00.000Z"
    }
]
```