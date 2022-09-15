class Campeonato:
    def __init__(self, torneio= '' , ano = ' '):
        self.torneio = torneio
        self.ano = ano 
        self.campeonatos = []


    def __str__(self) -> str:
        return f'Campeonato = {self.torneio} ' + f'Do Ano {self.ano}'


class Mostvp:
    def __init__(self, nome='' , idade = '', rota= '', equipe = '', campeonato=None):
        self.nome = nome
        self.idade= idade
        self.rota = rota
        self.equipe = equipe

      

        if campeonato is None:
            raise Exception('Precisa informar o campeonato')
        self.campeonato = campeonato
    def __str__(self) -> str:
        return   f'Jogador: {self.nome} , Idade =  {str(self.idade)}, Rota =  {self.rota}, No campeonato = {self.campeonato}'



if __name__ == '__main__':

    c1 = Campeonato(torneio='Cblol', ano= '2023')
    print(c1)
    j1 = Mostvp('Caio' , 18, 'Jungle', 'Intz', campeonato=c1)
    j2 = Mostvp('Felipe', 17 , 'TopLaner', 'Fúria', campeonato=c1)

    c1.campeonatos = [j1,j2]


    for q in c1.campeonatos:
        print(str(q))
       