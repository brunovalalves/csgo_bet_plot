import matplotlib.pyplot as plt
import numpy as np

class GerenciadorGrafico:
    def __init__(self, dados):
        self.dados = dados
    
    def desenhar_histograma(self):
        plt.style.use('_mpl-gallery')

        # make data:
        np.random.seed(3)
        x = np.arange(0,100,20)
        y = np.arange(5)

        # plot
        
        fig, ax = plt.subplots()
        ax.hist(self.dados)
        # ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
        plt.show()
            
    def desenhar_dispersao(self):

        # make data: correlated + noise
        np.random.seed(1)
        x = np.arange(0,125,5)
        y = np.random.random(len(x))

        plt.scatter(x,y, color = 'c', marker ='*')
        plt.xlabel('eixo x', fontsize = 16)
        plt.ylabel('eixo y',fontsize = 16)
        plt.title ('dispersão',fontsize = 20)
        plt.xlim([0,125])
        plt.ylim([0,1])

        plt.show()
        pass
