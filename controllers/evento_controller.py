# Controller - recebe a requisicao e coordena o fluxo.
# Ele nao conhece SQL: apenas pede ao DAO.

from flask import Blueprint, render_template, request, redirect
from models.evento import Evento
from dao.evento_dao import EventoDAO

evento_bp = Blueprint("evento", __name__)


@evento_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        evento = Evento(
            nome=request.form["nome"],
            data=request.form["data"],
            local=request.form["local"],
            vagas=int(request.form["vagas"])
        )

        EventoDAO.salvar(evento)
        return redirect("/")

    return render_template("index.html", eventos=EventoDAO.listar())