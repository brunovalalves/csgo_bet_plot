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
        bar = ax.bar(x, y, width=1, edgecolor="white", color = (.76, .12, .98))
        ax.bar_label(bar)
        plt.xlabel("Times", size = 12, color = (.76, .12, .98))
        plt.xticks(range(1, 3, 1))
        plt.ylabel("Vitórias", size = 12, color = (.37, .98, .20))

        plt.title("Vitórias por time", 
          fontdict={'family': 'serif', 
                    'color' : 'orange',
                    'weight': 'bold',
                    'size': 16})
        plt.show()
            




    # def desenhar_dispersao(self,dados):

    #     # make data: correlated + noise
    #     np.random.seed(1)
    #     x = np.arange(0,125,5)
    #     y = np.random.random(len(x))

    #     plt.scatter(x,y, color = 'c', marker ='*')
    #     plt.xlabel('eixo x', fontsize = 16)
    #     plt.ylabel('eixo y',fontsize = 16)
    #     plt.title ('dispersão',fontsize = 20)
    #     plt.xlim([0,125])
    #     plt.ylim([0,1])

    #     plt.show()
    #     pass
