# select odd, count(*) from (
# 	select id, odd_team2 as odd from matches
# 	where winner = 2 and odd_team2 > 0
# 	union
# 	select id, odd_team1 as odd from matches
# 	where winner = 1 and odd_team1 > 0) as tb 
# group  by odd 
# order by odd asc;

from gerenciador_grafico import GerenciadorGrafico
gerenciador=GerenciadorGrafico([])
gerenciador.desenhar_dispersao()
gerenciador.desenhar_histograma()

# Fim do método Main
