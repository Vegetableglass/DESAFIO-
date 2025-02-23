"""
>>> Desafio: Criar uma Calculadora com Classes  

Você deve criar uma classe chamada Calculadora que permita realizar operações matemáticas básicas, como adição, subtração, multiplicação e divisão. A calculadora também deve ser capaz de armazenar o histórico das operações realizadas. 
Requisitos:  

Classe Calculadora:  
Deve ter um atributo chamado historico, que será uma lista para armazenar as operações realizadas.
Deve ter os seguintes métodos:
- adicionar(a, b): Retorna a soma de a e b e registra a operação no histórico.
- subtrair(a, b): Retorna a diferença entre a e b e registra a operação no histórico.
- multiplicar(a, b): Retorna o produto de a e b e registra a operação no histórico.
- dividir(a, b): Retorna a divisão de a por b e registra a operação no histórico. Caso b seja zero, deve lançar uma exceção informando que a divisão por zero não é permitida.
- mostrar_historico(): Exibe todas as operações realizadas na calculadora, incluindo os números envolvidos e o resultado.

Exemplo de Funcionalidade:  

O usuário deve poder instanciar a classe Calculadora e usar seus métodos para realizar operações.
Após realizar algumas operações, o usuário pode chamar o método mostrar_historico() para ver o histórico completo.

Bônuss (opcional):  
Adicione um método chamado limpar_historico() que limpa o histórico de operações.
<<<

----ESSE DESAFIO É PRA QUANDO??-----
É uma atividade, na segunda feira iremos discutir.<--- OBRIGADO!
Para praticar e revisar os conceitos apresentados nos ultimos dias.
"""
historico = []
class Calculadora:
    def __init__ (self, a, b):
        self.a = a
        self.b = b
        self.total = 0

    def add (self):
        self.total = self.a + self.b
        historico.append (f"Adição:{self.a} + {self.b} = {self.total}")
        return self.total
    def remove (self):
        self.total = self.a - self.b
        historico.append (f"Subtrção:{self.a} - {self.b} = {self.total}")
        return self.total
    def multiply (self):
        self.total = self.a * self.b
        historico.append (f"Multiplicação:{self.a} * {self.b} = {self.total}")
        return self.total
    def divide (self):
        self.total = self.a / self.b
        historico.append (f"Dividir:{self.a} / {self.b} = {self.total}")
        return self.total
    def historico (self):
        if len(historico) > 0:
            for operation in historico:
                print (operation)
        else: 
            print ("Mermão, não tem nada.")
    def limpar(self):
        historico.clear()
        print ("Agora não tem nada, mermão.")       
            
rodando = True
while rodando:
    pergunta = int(input("Adição: 1 \nSubtração: 2 \nMultiplicar: 3 \nDividir: 4 \nHistorico: 5 \nLimpar Historico: 6 \nSair: 7 \nEscolha uma ação:"))
    if pergunta < 5:
        a = int(input("Escolha um número:"))
        b = int(input("Escolha outro número (pode ser o mesmo):"))
        calculadora = Calculadora(a, b)
    else:
        calculadora = Calculadora(0, 0)
    if pergunta == 1:
        total = calculadora.add()
        print(total)
    elif pergunta == 2:
        total = calculadora.remove()
        print(total)
    elif pergunta == 3:
        total = calculadora.multiply()
        print(total)
    elif pergunta == 4:
        total = calculadora.divide()
        print(total)
    elif pergunta == 5:
        calculadora.historico()
    elif pergunta == 6:
        calculadora.limpar()
    elif pergunta == 7:
        rodando = False
    
    else:
        print ("Lain não permite...")







    









   



    


     


