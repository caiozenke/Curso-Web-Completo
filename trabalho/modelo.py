
from config import *

#Preciso de uma tabela ralacional entre os alunos e personais, para poder adicionar os alunos a tabela pessoas
#Como adicionar os alunos a tabel pessoa e os alunos sem personais?
class Pessoa(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    
    tipo = db.Column(db.String(50))


    __mapper_args__= {
        'polymorphic_identity':'pessoa', 
        'polymorphic_on':tipo
        }
    
    def __str__(self):
        return f'{self.nome}, email ={self.email} , Função: {self.tipo}'



class Professor(Pessoa):
    id = db.Column(db.Integer ,db.ForeignKey('pessoa.id'),primary_key=True)
    __mapper_args__= {
        'polymorphic_identity':'professor', 
        }

    salario =  db.Column(db.String(254))

    def __str__(self):
        return super().__str__() + f", salario= {self.salario}"
           


class Personal(Pessoa):
    id = db.Column(db.Integer, db.ForeignKey('pessoa.id'),primary_key =True)
    __mapper_args__= {
        'polymorphic_identity': 'personal',
    }

    quantidade_alunos = db.Column(db.String(254))
    personais = db.relationship("Aluno", backref ="personal")

    def __str__(self):
        return super().__str__() + f', Tem {self.quantidade_alunos} de Alunos '




class Aluno(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    ativo = db.Column(db.Boolean)
    valor_mensalidade = db.Column(db.String(254))

    personal_id = db.Column(db.Integer, db.ForeignKey(Personal.id), 
                nullable=False)


    def __str__(self):
        s = f'Aluno: {self.nome}, email: {self.email},Está Ativo :{self.ativo}, Pagamento {self.valor_mensalidade} , tem o Personal: {self.personal.nome}'
        return s


#teste

if os.path.exists(arquivobd):
    os.remove(arquivobd)

db.create_all()

caio = Professor(nome="Caio Luan Zenke", 
            email="caiozdbja@gmail.com", salario=7)

#print(f'Professor: {caio}\n')

db.session.add(caio)
db.session.commit()

zenke = Personal(nome= 'Jorgao', email='ajbncsabcai@',quantidade_alunos ='30')
#print(zenke)
db.session.add(caio)
db.session.commit()

jose = Aluno(nome='José Augusto', email='joséaugusto@gmail.com' , ativo =True , valor_mensalidade= '200', personal = zenke)
#print(f'Aluno: {jose}' )

db.session.add(jose)
db.session.commit()

print ('Retornando Todas As Pessoas:')
for p in db.session.query(Pessoa).all():
    print (f'\t{p}')

print()
for a in zenke.personais:
    print(f'Busca dos Alunos do Personal {zenke.nome}:\n\t{a}')