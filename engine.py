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


# terceira atualizacao

    #insere a ordem no livro e empilha o ID para undo
    def process_order(self, order: Order):
        self.livro.insere_ordem(order)
        self.undo_stack.push(order.id)
        self._historico_tipo[order.id] = order.tipo   # guarda o tipo para desfazer
        print(f"  Ordem inserida no livro: {order}")
        self.check_match()

    # verifica se há match entre a melhor compra e a melhor venda
    # a regra é: preço da melhor compra >= preço da melhor venda
    def check_match(self):
        while True:
            melhor_c = self.livro.melhor_compra()
            melhor_v = self.livro.melhor_venda()

            if melhor_c is None or melhor_v is None:
                break   # um dos lados está vazio

            if melhor_c.preco >= melhor_v.preco:
                self.execute_trade(melhor_c, melhor_v)
            else:
                break   # sem match possível

    #executa a transação entre as duas melhores ordens
    def execute_trade(self, ordem_compra: Order, ordem_venda: Order):
        # quantidade negociada é o mínimo entre as duas ordens
        qtd_negociada = min(ordem_compra.quantidade, ordem_venda.quantidade)
        preco_exec = ordem_venda.preco   # o vendedor define o preço

        # Registra a transação
        tx = Transaction(ordem_compra.id, ordem_venda.id,
                         preco_exec, qtd_negociada)
        self.transacoes.append(tx)
        print(f"\n  *** MATCH ENCONTRADO! *** {tx}")

        # Atualiza as quantidades
        ordem_compra.quantidade -= qtd_negociada
        ordem_venda.quantidade  -= qtd_negociada

        # Remove do livro quem ficou com quantidade zero
        if ordem_compra.quantidade == 0:
            self.livro.remove_por_id(ordem_compra.id, 'C')
            print(f"  Ordem de compra #{ordem_compra.id} totalmente executada e removida.")

        if ordem_venda.quantidade == 0:
            self.livro.remove_por_id(ordem_venda.id, 'V')
            print(f"  Ordem de venda  #{ordem_venda.id} totalmente executada e removida.")

# QUARTA ATUALIZAÇAO

    #desfaz a última inserção usando a pilha
    def undo(self):
        id_desfazer = self.undo_stack.pop()
        if id_desfazer is None:
            print("Nenhuma ação para desfazer!")
            return

        tipo = self._historico_tipo.get(id_desfazer)
        if tipo is None:
            print(f"Erro: tipo da ordem #{id_desfazer} não encontrado.")
            return

        removeu = self.livro.remove_por_id(id_desfazer, tipo)
        if removeu:
            print(f"  Undo realizado: ordem #{id_desfazer} ({tipo}) removida do livro.")
        else:
            print(f"  Aviso: ordem #{id_desfazer} não estava mais no livro "
                  f"(pode já ter sido executada).")

    #exibe o histórico de transações
    def historico_transacoes(self):
        print("\n" + "=" * 55)
        print("  HISTÓRICO DE TRANSAÇÕES")
        print("=" * 55)
        if not self.transacoes:
            print("  Nenhuma transação executada.")
        for tx in self.transacoes:
            print(" ", tx)
        print("=" * 55)



