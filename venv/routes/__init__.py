from flask import Blueprint

# Importar y registrar los blueprints
def init_app(app):
    from venv.routes.usuario import usuario_bp
    from venv.routes.perfil import perfil_bp

    app.register_blueprint(usuario_bp, url_prefix='/usuarios')
    app.register_blueprint(perfil_bp, url_prefix='/perfiles')
