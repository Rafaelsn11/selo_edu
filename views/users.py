from flask import flash, render_template, redirect, request, url_for, session
from flask_login import current_user, login_required
from models.user import User
from extensions import db

# @users_bp.route("/")
@login_required
def index():
    usuarios = User.query.all()
    return render_template("users.html", usuarios=usuarios)

# @users_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        role = request.form.get("role", "aluno")
        senha = request.form.get("password")

        if current_user.role == "coordenador" and role == "coordenador":
            flash("Coordenador não pode criar outro coordenador.", "warning")

            return render_template("users/form.html", form_data={"nome": nome, "email": email, "role": "aluno"})
        if not senha:
            flash("A senha é obrigatória!", "danger")
            return render_template("users/form.html", form_data={"nome": nome, "email": email, "role": role})

        user = User(nome=nome, email=email, role=role)
        user.set_password("123456")
        db.session.add(user)
        db.session.commit()
        flash("Usuário criado com sucesso!", "sucess")
        return redirect(url_for("users.index"))
    
    return render_template("users/form.html")
