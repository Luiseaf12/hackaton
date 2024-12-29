# API Flask con PostgreSQL

## Configuración del Entorno

1. Crear un entorno virtual:
```bash
python -m venv venv
```

2. Activar el entorno virtual:
- Windows:
```bash
venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
- Copiar `.env.example` a `.env`
- Modificar las variables según tu configuración

5. Iniciar la base de datos:
```bash
flask db init
flask db migrate
flask db upgrade
```

6. Ejecutar la aplicación:
```bash
python run.py
```

## Estructura del Proyecto

```
back/
├── app/
│   ├── __init__.py
│   ├── modelos/
│   └── rutas/
├── migrations/
├── .env.example
├── config.py
├── requirements.txt
└── run.py
```

## Endpoints API

- GET /api/estado - Verifica el estado de la API