from flask import Flask, render_template
from extensions import db, login_manager
from flask_login import login_required
from models.user import User
from routes.auth import auth_bp
from routes.user import users_bp

app = Flask(__name__)
app.config.from_object("config.Config")

db.init_app(app)
login_manager.init_app(app)

users = [
    {
        "id": 1,
        "nome": "João da Silva",
        "email": "joao.silva@email.com",
        "perfil": "Coordenador",
        "status": "Ativo"
    },
    {
        "id": 2,
        "nome": "Maria Oliveira",
        "email": "maria.oliveira@email.com",
        "perfil": "Desenvolvedor",
        "status": "Ativo"
    },
    {
        "id": 3,
        "nome": "Carlos Santos",
        "email": "carlos.santos@email.com",
        "perfil": "Gerente de Projetos",
        "status": "Inativo"
    },
    {
        "id": 4,
        "nome": "Ana Souza",
        "email": "ana.souza@email.com",
        "perfil": "Analista de Dados",
        "status": "Ativo"
    },
    {
        "id": 5,
        "nome": "Fernando Lima",
        "email": "fernando.lima@email.com",
        "perfil": "Designer UX/UI",
        "status": "Ativo"
    },
    {
        "id": 6,
        "nome": "Patrícia Costa",
        "email": "patricia.costa@email.com",
        "perfil": "QA",
        "status": "Inativo"
    },
    {
        "id": 7,
        "nome": "Lucas Pereira",
        "email": "lucas.pereira@email.com",
        "perfil": "DevOps",
        "status": "Ativo"
    }
]


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("index.html")

with app.app_context():
    db.create_all()
    if not User.query.filter_by(email="admin@seloedu.com").first():
        user = User(nome="Admin", email="admin@seloedu.com", role="master")
        user.set_password("123456")
        db.session.add(user)
        db.session.commit()
        print("Usuário admin criado com sucesso!")

app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)

if __name__ == "__main__":
    app.run(debug=True)