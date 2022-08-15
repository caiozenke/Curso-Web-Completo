
class Campeonato:
    def __init__(self, torneio= '' , ano = ' ', mvp = None):
        self.torneio = torneio
        self.ano = ano
        self.mvp = mvp 


    def __str__(self) -> str:
        return f'Campeonato = {self.torneio} ' + f'Do Ano {self.ano}, ' + f'Com Mvp: {str(self.mvp)}'


class Mostvp:
    def __init__(self, nome='' , idade = '', rota= '', equipe = ''):
        self.nome = nome
        self.idade= idade
        self.rota = rota
        self.equipe = equipe
        
    def __str__(self) -> str:
        return   self.nome  + ", " + self.idade + ", " + self.rota + ", " + self.equipe



if __name__ == '__main__':

    mvp= Mostvp(nome= 'Caio Zenke' , idade= '18', rota= 'Midlaner' , equipe= 'intz')
    camp = Campeonato(torneio='Cblol', ano= '2023' , mvp=mvp)

    print (camp)