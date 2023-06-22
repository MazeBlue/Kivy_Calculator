# todo from xxx import xxx é sobre uma classe sendo importada de um módulo, como nas duas próximas explicações da classes importas
# a mesma sintaxe seguirá para todas as próximas classes

#importa a classe App do módulo kivy.app é responsável pela base de criação dos aplicativos kivy
from kivy.app import App

# importa a classe BoxLayout do módulo kivy.uia.boxlayout, é um layout responsável por organizar seus filhos em uma única linha, ou coluna
from kivy.uix.boxlayout import BoxLayout

# essa classe é responsável por representar um botão interativo na interface do usuário
from kivy.uix.button import Button

# A classe TextInput permite que o usuário digite texto
from kivy.uix.textinput import TextInput


# a classe Main App herda a App que representa o aplicativo principal que armazena a lógica e os elementos da interface do usuário
class MainApp(App):
    
    # o método build é chamado quando o aplicativo é inicializado, ele retorna o widget raiz (interface principal) que será exibido na tela
    def build(self):
        
        # criação da lista de operadores
        self.operators= ["/", "*", "+", "-"]
        
        # inicializa a variavel last_was_operator com valor nulo que poderá ser definido posteriormente
        self.last_was_operator= None
        
        # inicializa a variavel last_button com valor nulo que poderá ser definido posteriormente
        self.last_button= None
        
        # main_layout é uma instancia de BoxLayout e definida na posição vertical
        main_layout= BoxLayout(orientation= 'vertical')
        
        # instancia de TextInput com configurações especificas a serem exibidas na interface do usuário
        self.solution= TextInput(
            multiline=False, readonly=True, halign='right', font_size=55
        )
        
        # associa o widget solution ao main_layout
        main_layout.add_widget(self.solution)
        
        # lista de botões da calculadora
        buttons= [
            ["7", "8", "9", "/"], 
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        
        # loop que percorre cada linha na lista buttons para organiza-los com o próximo comando
        for row in buttons: 
            
            # define o layout horizontal
            h_layout= BoxLayout()
            
            # inicia o loop que percorre cada rótulo na linha atual para ler e armazenar a opção selecionada no próximo comando
            for label in row:
                button= Button(
                    # define a posição e o tamanho do botão dentro do layout
                    text=label,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                )
                # evento do botão pressionado
                button.bind(on_press=self.on_button_press)
                
                # adiciona o botão pressionado ao hlayout
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
        # cria uma instancia de button
        equals_button= Button(
            # define a posição e o tamanho do botão =
            text="=", pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        # vincula o eveneot de pressionar (on_press) ao metodo de solução (on_solution)
        equals_button.bind(on_press=self.on_solution)
        
        # adiciona o widget = ao layout
        main_layout.add_widget(equals_button)
        
        # executa o layout com todas as configurações definidas acima
        return main_layout
    
    
    # método chamado quando um botão é pressionado
    def on_button_press(self, instance):
        
        # lê o texto armazenado no widget wolution e armazena na current
        current= self.solution.text
        button_text= instance.text
        
        # para limpar o botão selecionado
        if button_text== "C": 
            
            # retorna vazio em caso de C pressionado
            self.solution.text= ""
        
        # ou então
        else:
            
            # trata os seguintes erros de digitação do usuário abaixo
            if current and (
                # trata o erro de selecionar dois operadores ao mesmo tempo
                self.last_was_operator and button_text in self.operators): 
                return
            
            # trata o erro de selecionar um operador antes de um numero
            elif current== "" and button_text in self.operators: 
                return
            
            # caso nenhum erro seja encontrado, então executa o codigo abaixo
            else:
                
                #junta os valores pressionados, exemplo 2+2
                new_text= current+ button_text
                self.solution.text= new_text
                
                # armazena o texto do botão pressionado anteriormente na variavel last_button
            self.last_button= button_text
            
            # verifica se o ultimo botão esta na lista de operadores e armazena o resultado na variavel last_was_operator
            self.last_was_operator= self.last_button in self.operators
          
          
          #metodo de solução da calculadora  
    def on_solution(self, instance):
        
        # obtém o texto do widget solution (resultado da expressão) e armazena em text
        text= self.solution.text
        if text:
            
            # avalia a expressão e armazena o resultado como string
            solution= str(eval(self.solution.text))
            self.solution.text= solution

if __name__== '__main__': # verifica se o módulo está sendo executado diretamente e não importando como um módulo
    app= MainApp()
    # inicia a execução do aplicativo kivy
    app.run()