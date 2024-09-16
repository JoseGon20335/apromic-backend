# Apromic Backend

Este es un proyecto de backend para manejar boletines usando Flask y Firebase. Incluye funcionalidades para cargar, descargar y borrar boletines, almacenando los archivos en Firebase Storage y las referencias en Firestore.

## Dependencias

Las principales dependencias de este proyecto son:

- Python 3.8+
- Flask
- Firebase Admin SDK
- Werkzeug (para la gestión de archivos seguros)

## Instalación de Librerías Necesarias

1. **Clona este repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/apromic-backend.git
   cd apromic-backend
   ```

2. **Crea y activa un entorno virtual (opcional pero recomendado):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. **Instala las dependencias necesarias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configura tus credenciales de Firebase:**

   - Descarga el archivo JSON de credenciales de tu proyecto Firebase y colócalo en la raíz del proyecto.
   - Asegúrate de que el archivo `firebase_key.json` esté correctamente nombrado o ajusta el código para que coincida con el nombre del archivo de credenciales.

## Cómo Correr el Programa

1. **Inicializa la aplicación Flask:**

   Ejecuta el siguiente comando para iniciar la aplicación:

   ```bash
   flask run
   ```

   Por defecto, la aplicación estará disponible en `http://127.0.0.1:5000`.

2. **Probar Endpoints:**

   Puedes probar los endpoints usando herramientas como `curl`, `Postman`, o directamente desde el navegador para los métodos `GET`.

## Herramientas Usadas

- **Flask:** Un microframework de Python para desarrollar aplicaciones web.
- **Firebase Admin SDK:** Biblioteca para interactuar con Firebase desde Python.
- **Firebase Storage:** Servicio de Firebase para almacenar archivos.
- **Firestore:** Base de datos NoSQL de Firebase para almacenar referencias y datos estructurados.
- **Werkzeug:** Herramienta WSGI para Flask, utilizada para la gestión segura de archivos.

## Colaboradores

- **Tu Nombre:** Desarrollador principal.
- *(Añadir más colaboradores si los hay).*

## Notas

- Recuerda ajustar las reglas de seguridad de Firebase Storage y Firestore para tu entorno de producción.
- Este proyecto es una implementación básica para la gestión de boletines y puede ser ampliado según las necesidades específicas.
