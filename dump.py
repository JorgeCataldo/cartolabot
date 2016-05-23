# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:40:52 2016

@author: Jorge
""" 
import csv
from sqlalchemy import create_engine
conn = "mysql+pymysql://inf2290:^inf2290$@mysql.mosconi.eti.br/cartola"
engine = create_engine(conn)


#IMPORTA E MONTA GAME.CSV
game_sql='''
SELECT 
    game_id,
    nome_txt AS game_name,
    temporada_num AS game_season,
    rodada_atual_num AS current_round
FROM 
    game 
'''
result = engine.execute(game_sql)
c = csv.writer(open("game.csv", "w"))  
c.writerow(result)


#IMPORTA E MONTA PLAYERS.CSV
players_sql='''
SELECT
    atleta_id AS player_id,
    nome_txt AS player_name
FROM
    atleta_2015
'''
result = engine.execute(players_sql)
c = csv.writer(open("players.csv", "w"))  
c.writerow(result)


#IMPORTA E MONTA SEASON.CSV
season_sql='''
SELECT
    ar.atleta_id AS player_id,
    ar.rodada_id AS round,
    pos.nome_txt AS position,
    st.nome_txt AS status,
    ar.preco_num AS price,
    ar.pontos_num AS score
FROM
    atleta_rodada_2015 AS ar
JOIN 
posicao AS pos ON (ar.posicao_id = pos.posicao_id)
JOIN 
status AS st ON (ar.status_id = st.status_id)
'''

result = engine.execute(season_sql)
c = csv.writer(open("season.csv", "w"))  
c.writerow(result)

