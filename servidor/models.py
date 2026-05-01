from database import db


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    email = db.Column(db.String(120))
    senha = db.Column(db.String(80))
    token = db.Column(db.String(120))
   
    def __init__(self, nome, email, senha, token):
      self.nome = nome
      self.email = email
      self.senha = senha
      self.token = token
        
      
      
    def __repr__(self):
        return "Usuario: {}".format(self.token)

  