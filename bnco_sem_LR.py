
from config import *

class Campeonato (db.Model):
    id = db.Column(db.Integer, primary_key=True) #id do campeonato
    torneio = db.Column(db.String(254)) 

    def __str__(self) -> str:
        return f'Campeonato:{self.torneio}' #retornando o valor da tabela


#A partir daqui Acontece o Erro!
class Pessoa(db.Model):
    #definindo os valores

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    idade = db.Column(db.String(254))
    rota = db.Column(db.String(254))
    equipe = db.Column(db.String(254))

    campeonato_id = db.Column(db.Integer , db.ForeignKey(Campeonato.id),nullabel=False)
    campeonato = db.relationship("Campeonato")
    def __str__(self):
        d = f'Jogador: {self.nome}, idade:{self.idade}, rota:{self.rota}, equipe:{self.equipe} em: {str(self.campeonato)}' #retornando os valores em str
        d += f'Campeonato = {self.campeonato}'
        return d



if __name__ == '__main__':

    if os.path.exists(arquivobd):  #se ja existir o banco

        os.remove(arquivobd)    #exclue o banco

    db.create_all() #criando o banco


    c1 = Campeonato(torneio ='Cblol')

    db.session.add(c1)
    db.session.commit()
    

    print(c1)


