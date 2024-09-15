from venv import create_app

# Crear una instancia de la aplicación
app = create_app()

if __name__ == '__main__':
    # Ejecutar la aplicación en modo de depuración
    app.run(debug=True)


