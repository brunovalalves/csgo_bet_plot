# import matplotlib.pyplot as plt
# import numpy as np
# #plt.style.use('_mpl-gallery')

# # make data:
# np.random.seed(3)
# x = np.arange(0,100,20)
# y = np.arange(5)

# # plot
# fig, ax = plt.subplots()

# ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

# plt.show()

# # select odd, count(*) from (
# # 	select id, odd_team2 as odd from matches
# # 	where winner = 2 and odd_team2 > 0
# # 	union
# # 	select id, odd_team1 as odd from matches
# # 	where winner = 1 and odd_team1 > 0) as tb 
# # group  by odd 
# # order by odd asc;


# import matplotlib.pyplot as plt
# import numpy as np

# # make data: correlated + noise
# np.random.seed(1)
# x = np.arange(0,125,5)
# y = np.random.random(len(x))

# plt.scatter(x,y, color = 'c', marker ='*')
# plt.xlabel('eixo x', fontsize = 16)
# plt.ylabel('eixo y',fontsize = 16)
# plt.title ('dispersão',fontsize = 20)
# plt.xlim([0,125])
# plt.ylim([0,1])

# plt.show()

from gerenciador_grafico import GerenciadorGrafico
gerenciador=GerenciadorGrafico([])
gerenciador.desenhar_histograma()
