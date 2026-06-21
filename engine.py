#TRABALHO - SIMULADOR DE LIVRO DE OFERTAS

from structures   import Order, Stack
from queue_ordens import Queue
from order_book   import OrderBook
from datetime     import datetime

class Transaction:
    _contador = 1

    def __init__(self, id_compra: int, id_venda: int, preco: float, quantidade: int):
        self.id = Transaction._contador
        Transaction._contador += 1
        self.id_compra = id_compra
        self.id_venda = id_venda
        self.preco = preco
        self.quantidade = quantidade
        self.timestamp = datetime.now()

    def __str__(self):
        return (f"[Transação #{self.id} | "
                f"Compra#{self.id_compra} x Venda#{self.id_venda} | "
                f"Preço:R${self.preco:.2f} | Qtd:{self.quantidade} | "
                f"{self.timestamp.strftime('%H:%M:%S')}]")

#segunda atualizacao

class MatchEngine:

    def __init__(self):
        self.fila = Queue() #fila de ordens
        self.livro = OrderBook() #livro de compras e vendas
        self.undo_stack = Stack() #pilha para permitir desfazer ações
        self.transacoes = []  #historico das transacoes
        self._historico_tipo = {}  # id -> tipo, para o undo

    # recebe uma ordem, coloca na fila e processa
    def recebe_ordem(self, order: Order):
        self.fila.enqueue(order)
        self._processar_fila()

    # esvazia a fila processando cada ordem
    def _processar_fila(self):
        while not self.fila.esta_vazia():
            ordem = self.fila.dequeue()
            self.process_order(ordem)
