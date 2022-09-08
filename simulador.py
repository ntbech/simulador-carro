from tkinter import *
#Uma importação de interface será executada utilizando o Tkinter.

from tkinter.messagebox import *
#Importação de uma caixa de mensagem, será mostrada na interface gráfica


class Carro: 
  """Criação da classe Carro"""

  def __init__(self, car=0, velocidade=0.0, combustivel=0.0, km_percorrido=0.0):
    self.velocidade = velocidade
    self.combustivel = combustivel
    self.km_percorrido = km_percorrido
    self.car = car
    #Quando o objeto for instanciado, dará inicio as funções estabelecida nas propriedades do def, onde o método __init__ é chamado imediatamente quando o objeto é criado, podendo o atributo pertencente a cada método ser criado, assim como modificado por meio de self. nome do atributo

    lab = Label(self.car, text= "Digite as informações")
    lab.pack()
    #Será mostrado na interface gráfica através do código label um texto não editável pedindo para o usário digitar as informações
    
    lab_acel = Label(self.velocidade, text="Aceleração:")
    lab_acel.pack()
    self.ent_acel = Entry(self.velocidade)
    self.ent_acel.pack()
    #Será mostrado na interface gráfica através do código label um texto não editável e através do código entry será mostrada um campo de entrada que o usuário poderá digitar a informação pedida.
    
    lab_comb = Label(self.combustivel, text="Combustível:")
    lab_comb.pack()
    self.ent_comb = Entry(self.combustivel)
    self.ent_comb.pack()
    #Será mostrado na interface gráfica através do código label um texto não editável e através do código entry será mostrada um campo de entrada que o usuário poderá digitar a informação pedida.

    lab_kmperc = Label(self.km_percorrido, text="Km Percorrido:")
    lab_kmperc.pack()
    self.ent_kmperc = Entry(self.km_percorrido)
    self.ent_kmperc.pack()
    #Será mostrado na interface gráfica através do código label um texto não editável e através do código entry será mostrada um campo de entrada que o usuário poderá digitar a informação pedida.

    bot = Button(self.car, text="Ok", command=self.clique)
    bot.pack()
    #Na interface gráfica será mostrado um botão, ao qual o usuário irá clicar assim que terminar de fornecer as informações pedida pelo programa.
  
  def verifica(self, valor):
    try:
      int(valor)
      return True
    except ValueError:
      return False  
      #O programa irá verificar se o valor digitado pelo usuário é um número inteiro ou não.

  def valida(self,valor):
    inteiro = self.verifica(valor)
    if inteiro == False:
      return False
      #O programa irá primeiro validar se o valor fornecido pelo usuário é inteiro, caso não seja, ele irá reportar um false.

    else:
      valorConvertido = int(valor)
      if valorConvertido <=0:
        return False
      else:
        return True
        #O programa irá verificar se o valor fornecido pelo usuário é menor ou igual a 0, caso seja retorna false, caso não seja irá retornar true.

  def clique(self):
    tex =  self.ent_comb.get()
    aux = self.valida(tex)
    if aux == False:
      return showerror('Erro', "Não é possível acelerar o carro sem combustível")
      #"O programa irá verificar se a informação passada no parâmetro anterior é falso ou verdadeiro, caso seja verdadeiro ele dá seguimento ao programa, caso não, ele irá mostrar uma mensagem de erro ao usuário.

    else:
      text_acel = self.ent_acel.get()
      text_comb = self.ent_comb.get()
      text_km = self.ent_kmperc.get()
      lab = Label(self.car, text= "As informações inseridas são:  \n Aceleração: " +text_acel)
      lab.pack()
      lab = Label(self.car, text="Combustível: " +text_comb)
      lab.pack()
      lab = Label(self.car, text="Km Percorridos: " +text_km)
      lab.pack()
      #O programa irá armazenar e mostrar na tela as informações fornecidas pelo usuário, caso todas as suas informações esteja de acordo com os parâmetros passados ao programa.

NM=Tk()
NM.title("Simulador de Carro")
app = Carro(NM)
NM.geometry("500x300")
#Parâmetros passados para a interface gráfica, como o nome do título, comprimento e largura da interface. 

barraMenus=Menu(NM)
menuInfo=Menu(barraMenus)
menuInfo.add_separator()
menuInfo.add_command(label="Sair", command=NM.quit)
#Um menu será impresso na interface gráfica, com a opção para o usuário encerrar o progragama. 

NM.config(menu=menuInfo)
#Utilizado para poder imprimir os parâmetros passados para o menu

NM.mainloop()
#Utilizado para exibir a tela em que será mostrado toda a interface gráfica e os parâmetro passados no programa.