# Sistema Web de Gestao de Eventos Academicos
# Desenvolvimento Web II (DW2)

from flask import Flask
from controllers.evento_controller import evento_bp
from database import db

app = Flask(__name__)

# Configuração do banco SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///eventos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa o SQLAlchemy com o Flask
db.init_app(app)

# Registra as rotas dos eventos
app.register_blueprint(evento_bp)


if __name__ == "__main__":
    app.run(debug=True)