from flask import Blueprint, flash, render_template, request, redirect, url_for, session
from flask_login import login_required, login_user, logout_user, login_required
from models.user import User

def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")


        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            flash("Login realizado com sucesso!", "sucess")
            return redirect(url_for("dashboard"))
        else:
            flash("Credenciais inválidas.", "danger")
    
    return render_template("auth/login.html")

@login_required
def logout():
    logout_user()
    flash("Sessão encerrada.", "info")
    return redirect(url_for("auth.login"))