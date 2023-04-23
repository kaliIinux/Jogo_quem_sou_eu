import pandas as pd
import os
import openpyxl

class Jogador:
    
    """
    Classe do Jogador, onde tenho os atributos
    de cada jogador, os getters e setters e os 
    métodos para adicionar e manipular em um data 
    frame com pandas
    """
    
    def __init__(self, nome: str, idade:int) -> None:
        self.__nome = nome
        self.__pontos = 0
        self.__idade = idade
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        self.__nome = value
        
    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self, value):
        self.__pontos = value
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, value):
        self.__idade = value
    
    def adicionar_jogador(self, pontos):
        jogador = pd.read_excel("dados.xlsx")
        jogador.loc[len(jogador)] = [self.__nome, self.__idade, pontos]
        jogador.to_excel("dados.xlsx", index=False)
        
    @staticmethod
    def cria_planilha():
        d = {"Nome": [''], "Idade": [''], "Pontos": ['']}
        dados = pd.DataFrame(data=d)
        dados.to_excel("dados.xlsx", index=False)
        
        
    @staticmethod
    def limpa_planilha():
        os.remove("dados.xlsx")
    
    @staticmethod
    def ler_ranking():
        planilha = pd.read_excel("dados.xlsx")
        ranking = planilha.loc[:,['Nome','Pontos']]
        ranking = ranking.sort_values(by=['Pontos'], ascending=False, na_position='last',ignore_index=True).head(5)
        print(ranking)
        
