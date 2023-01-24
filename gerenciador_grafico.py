import matplotlib.pyplot as plt
import numpy as np

class GerenciadorGrafico:
    def __init__(self, dados):
        self.dados = dados
            
    def desenhar_histograma(self):
        # plt.style.use('_mpl-gallery')

        # make data:
        times_1,times_2 = 0,0
        for dado in self.dados:
            if dado[4] == 1:
                times_1 += 1
            elif dado[4] == 2:
                times_2 += 1            

        np.random.seed(1)
        x = [1,2]
        y = [times_1,times_2]

        # plot
        
        fig, ax = plt.subplots()
        # ax.hist(self)#.dados)
        bar = ax.bar(x, y, width=1, edgecolor="white", color = (.0, .0, .0))
        ax.bar_label(bar)
        plt.xlabel("Times", size = 12, color = (.0, .0, .0))
        plt.xticks(range(1, 3, 1))
        plt.ylabel("Vitórias", size = 12, color = (.0, .0, .0))

        plt.title("Vitórias por time", 
          fontdict={'family': 'serif', 
                    'color' : 'blue',
                    'weight': 'bold',
                    'size': 16})
        plt.show()          

    def desenhar_dispersao(self):

        # make data: correlated + noise
        # np.random.seed(1)
        for dado in self.dados:
            if dado[2] == 0 or dado[3] == 0 or dado[4] is None: 
                continue
            elif dado[4] == 1:
                x = dado[2]
                y = dado[3]
            elif dado[4] == 2:
                x = dado[3]
                y = dado[2]

            print(dado[4],x,y)
            plt.scatter(x,y, color = 'c', marker='*')

        plt.xlabel('Odd do ganhador', fontsize = 16)
        plt.ylabel('Odd do perdedor',fontsize = 16)
        plt.title ('Dispersão',fontsize = 20)

        plt.show()
        pass
    
    def desenhar_ganho_apostas(self):
        ganho_favorito, ganho_zebra, perda_favorito, perda_zebra = 0, 0, 0, 0
        for dado in self.dados:
            winner, odd_1, odd_2 = dado[4], dado[2], dado[3]
            if winner is None or odd_1 == 0 or odd_2 == 0 or odd_1 == odd_2:
                continue
            if odd_1 < odd_2 and winner == 1 or odd_2 < odd_1 and winner == 2:
                ganho_favorito += min(odd_1,odd_2) - 1
                perda_zebra += 1
            else:
                ganho_zebra += max(odd_1,odd_2) - 1
                perda_favorito += 1
                
            
        resultado_favorito = ganho_favorito - perda_favorito       
        resultado_zebra = ganho_zebra - perda_zebra
        
        x = ['Profit favorito','Profit zebra']
        y = [resultado_favorito, resultado_zebra]     

        fig, ax = plt.subplots()        
        bar = ax.bar(x, y, width=1, edgecolor="white", color = (.0, .0, .0))
        ax.bar_label(bar)
        plt.xlabel("Favorito/Zebra", size = 12, color = (.0, .0, .0))        
        plt.ylabel("Profit", size = 12, color = (.0, .0, .0))
        plt.title("Profit por tipo de aposta", 
          fontdict={'family': 'serif', 
                    'color' : 'gray',
                    'weight': 'bold',
                    'size': 14})
        plt.show()