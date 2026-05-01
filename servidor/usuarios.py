from flask import Blueprint, jsonify
from flask.templating import render_template, request
from models import Usuario
from database import db
import secrets
import json
import random

bp_usuarios = Blueprint("usuarios", __name__, template_folder= "templates")

@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
  if request.method=='GET':
    return render_template('usuarios_create.html')

  if request.method == 'POST':
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    token =  "Bearer " + secrets.token_hex(16)
    
    u = Usuario(nome, email, senha, token)
    db.session.add(u)
    db.session.commit()
    return  json.dumps({"apikey":token})

@bp_usuarios.route('/recovery', methods=['GET'])
def recovery():
  usuarios = Usuario.query.all()
  return render_template('usuarios_recovery.html', usuarios=usuarios)

@bp_usuarios.route('/gerar/<test>', methods=['GET'])
def compara(test):
  valor = db.session.query(Usuario).filter_by(token=test).first()
  if(valor):
    
    numero = random.randint(0, 1000000)
    return  json.dumps({"nome": valor.nome,
                        "numero": numero})
  


  