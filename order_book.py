""" 
O que é o Livro de Ofertas?
É o "quadro de avisos" do mercado financeiro. Mostra quem quer comprar e a que preço, e quem quer vender e a que preço.

Lista de COMPRAS: ordenada do MAIOR preço para o MENOR
O melhor comprador (paga mais) fica na frente.
Lista de VENDAS: ordenada do MENOR preço para o MAIOR
O melhor vendedor (cobra menos) fica na frente.
"""
from structures import Node, Order

class BuyList:

    #lista de ordens de compra

    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamanho = 0
