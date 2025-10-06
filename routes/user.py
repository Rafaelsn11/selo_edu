from flask import Blueprint
from views import users as users_views

users_bp = Blueprint('users', __name__, url_prefix="/users")

users_bp.add_url_rule("/", view_func=users_views.index)
users_bp.add_url_rule("/create", view_func=users_views.create, methods=["GET", "POST"])


# @users_bp.route("/")
# @login_required
# def index():
#     usuarios = User.query.all()
#     return render_template("users/index.html", usuarios=usuarios)

# @users_bp.route("/create", methods=["GET", "POST"])
# @login_required
# def create():
#     if request.method == "POST":
#         nome = request.form.get("nome")
#         email = request.form.get("email")
#         role = request.form.get("role", "aluno")
#         user = User(nome=nome, email=email, role=role)
#         user.set_password("123456")
#         db.session.add(user)
#         db.session.commit()
#         flash("Usuário criado com sucesso!", "sucess")
#         return redirect(url_for("users.index"))
    
#     return render_template("users/form.html")
