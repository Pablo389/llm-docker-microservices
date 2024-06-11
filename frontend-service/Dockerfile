# Etapa 1: Construcción de la aplicación
FROM node:14 AS build

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos package.json y package-lock.json
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el resto de los archivos de la aplicación
COPY . .

# Construye la aplicación para producción
RUN npm run build

# Etapa 2: Servir la aplicación
FROM nginx:stable-alpine

# Copia los archivos construidos desde la etapa de construcción
COPY --from=build /app/build /usr/share/nginx/html

# Copia la configuración de nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Expon el puerto en el que nginx estará sirviendo
EXPOSE 80

# Comando por defecto para correr nginx
CMD ["nginx", "-g", "daemon off;"]