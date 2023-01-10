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
