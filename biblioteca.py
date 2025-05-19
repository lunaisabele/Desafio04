class Atleta:
    def __init__(self, peso):
        self.aposentado = False
        self.peso = peso
        self.correndo = False
        self.nadando = False
        self.pedalando = False

    def Atletaaposentado(self):
        pergunta = input("O atleta é aposentado? Digite 'sim' ou 'nao': \n")
        if pergunta.lower() == "sim":
            self.aposentado = True
            print("O atleta está aposentado e não pode se aquecer.")

    def aquecerAtleta(self):
        if self.aposentado:
            print("O atleta está aposentado e não pode se aquecer.")
        else:
            print("O atleta está aquecendo.")

class Corredor(Atleta):
    def __init__(self, peso):
        super().__init__(peso)

    def correr(self):
        if self.aposentado:
            print("O atleta é aposentado, não pode correr.")
        elif self.nadando or self.pedalando:
            print("O atleta está fazendo outra atividade e não pode correr agora.")
        else:
            self.correndo = True
            self.nadando = False
            self.pedalando = False
            print("O atleta está correndo.")

class Nadador(Atleta):
    def __init__(self, peso):
        super().__init__(peso)

    def nadar(self):
        if self.aposentado:
            print("O atleta é aposentado, não pode nadar.")
        elif self.correndo or self.pedalando:
            print("O atleta está fazendo outra atividade e não pode nadar agora.")
        else:
            self.nadando = True
            self.correndo = False
            self.pedalando = False
            print("O atleta está nadando.")

class Ciclista(Atleta):
    def __init__(self, peso):
        super().__init__(peso)

    def pedalar(self):
        if self.aposentado:
            print("O atleta é aposentado, não pode pedalar.")
        elif self.correndo or self.nadando:
            print("O atleta está fazendo outra atividade e não pode pedalar agora.")
        else:
            self.pedalando = True
            self.correndo = False
            self.nadando = False
            print("O atleta está pedalando.")

class Triatleta(Corredor, Nadador, Ciclista):
    def __init__(self, peso):
        Atleta.__init__(self, peso)  # Chama o init direto da classe base






