from flask import Flask, render_template

app = Flask(__name__)

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


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/users")
def users_page():
    return render_template("users.html", users=users)

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('Auth/login.html')