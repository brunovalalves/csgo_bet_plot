from gerenciador_grafico import GerenciadorGrafico
import psycopg2

#Establishing the connection
conn = psycopg2.connect(
database='csgo_bet_analysis', user='postgres', password='postgres', host='localhost', port= '5432'
)
# Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL queries to INSERT a record into the database.
cursor.execute('select * from public.matches')

dados = cursor.fetchall()

# dados=[
#     (2357689, 'aravt-vs-d13-5e-arena-asia-cup-2022-closed-qualifier', 1.7, 1.95, 1),
#     (2357543, 'furia-academy-vs-astralis-talent-weplay-academy-league-season-5', 0, 0, 2),
#     (2357690, 'nkt-vs-lynn-vision-5e-arena-asia-cup-2022-closed-qualifier', 2.42, 1.55, 2),
#     (2357544, 'spirit-academy-vs-og-academy-weplay-academy-league-season-5', 1.52, 2.49, 1),
#     (2357691, 'catevil-vs-ihc-5e-arena-asia-cup-2022-closed-qualifier', 5.5, 1.1, 1),
#     (2357753, 'wolsung-vs-cryptova-cct-central-europe-series-1-closed-qualifier', 0, 0, None),
#     (2357545, 'navi-junior-vs-furia-ac-astralis-t-winner-weplay-academy-league-season-5', 0, 0, None),
#     (2357776, 'daotsu-vs-stars-horizon-cct-south-america-series-1', 1.52, 5.25, None),
#     (2357822, 'ec-kyiv-vs-yodagus-elisa-invitational-fall-2022-contenders', 1.13, 6.0, None),
#     (2357877, 'order-vs-encore-iem-road-to-rio-2022-oceania-open-qualifier-1', 1.3, 4.2, None),
#     (2357878, 'rooster-vs-morbin5-iem-road-to-rio-2022-oceania-open-qualifier-1', 1.85, 2.8, None),
#     (2357883, 'rare-atom-vs-wings-up-iem-road-to-rio-2022-china-open-qualifier-1', 1.46, 2.65, None),
#     (2357884, 'lynn-vision-vs-tyloo-iem-road-to-rio-2022-china-open-qualifier-1', 4.81, 1.17, None),
#     (2357889, 'ihc-vs-d13-iem-road-to-rio-2022-asia-open-qualifier-1', 1.14, 5.3, None),
#     (2357890, 'nkt-vs-aravt-iem-road-to-rio-2022-asia-open-qualifier-1', 1.48, 2.77, None),
#     (2357823, 'b8-vs-777-elisa-invitational-fall-2022-contenders', 1.5, 2.7, None)
# ]


gerenciador=GerenciadorGrafico(dados)
gerenciador.desenhar_histograma()

# select odd, count(*) from (
# 	select id, odd_team2 as odd from matches
# 	where winner = 2 and odd_team2 > 0
# 	union
# 	select id, odd_team1 as odd from matches
# 	where winner = 1 and odd_team1 > 0) as tb 
# group  by odd 
# order by odd asc;


# Chamando métodos da classe GerenciadorGrafico

# gerenciador.desenhar_dispersao(dados)
# gerenciador.desenhar_histograma()

# Fim do método Main
