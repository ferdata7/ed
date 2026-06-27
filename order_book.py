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

# insere ordem de compra mantendo ordem decrescente de preço
    def insere_ordenado(self, order: Order):
        novo  = Node(order)
        atual = self.inicio
        # se a lsita estiver vazia
        if self.inicio is None:
            self.inicio = novo
            self.final = novo
            self.tamanho += 1
            return
        #se o novo preço é maior que o primeiro
        if order.preco > self.inicio.data.preco:
            novo.next = self.inicio
            self.inicio.prev = novo
            self.inicio = novo
            self.tamanho += 1
            return
        #percorre até achar onde encaixar
        while atual.next is not None:
            if order.preco > atual.next.data.preco:
                break
            atual = atual.next
        novo.next = atual.next
        novo.prev = atual
        if atual.next is not None:
            atual.next.prev = novo
        else:
            self.final = novo
        atual.next = novo
        self.tamanho += 1
    # remover ordem pelo id
    def remove_por_id(self, order_id: int):
        item = self.inicio
        while item is not None:
            if item.data.id == order_id:
                if item.prev is not None:
                    item.prev.next = item.next
                else:
                    self.inicio = item.next
                if item.next is not None:
                    item.next.prev = item.prev
                else:
                    self.final = item.prev
                self.tamanho -= 1
                return True
            item = item.next
        print(f"Erro! Ordem #{order_id} não encontrada na lista de compras.")
        return False
    # retorna (sem remover) a melhor oferta de compra
    def melhor_oferta(self):
        if self.inicio is None:
            return None
        return self.inicio.data
    # verifica se está vazia
    def esta_vazia(self):
        return self.tamanho == 0
    # imprime a lista de compras formatada
    def imprime(self):
        item = self.inicio
        if item is None:
            print("  (lista de compras vazia)")
            return
        while item is not None:
            print(f"  COMPRA  | Preço: R${item.data.preco:>8.2f} | "
                  f"Qtd: {item.data.quantidade:>5} | ID: #{item.data.id}")
            item = item.next
            
class SellList:
    #Lista de ordens de venda ordenada por preço crescente. Melhor vendedor (menor preço) sempre no início.

    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamanho = 0

    # insere ordem de venda mantendo ordem crescente de preço
    def insere_ordenado(self, order: Order):
        novo = Node(order)
        atual = self.inicio

        #se a lista está vazia
        if self.inicio is None:
            self.inicio = novo
            self.final = novo
            self.tamanho += 1
            return

        # se novo preço é menor que o primeiro, vai para o início
        if order.preco < self.inicio.data.preco:
            novo.next = self.inicio
            self.inicio.prev = novo
            self.inicio = novo
            self.tamanho += 1
            return

        # percorre até achar onde encaixar
        while atual.next is not None:
            if order.preco < atual.next.data.preco:
                break
            atual = atual.next

        # insere novo entre atual e atual.next
        novo.next = atual.next
        novo.prev = atual
        if atual.next is not None:
            atual.next.prev = novo
        else:
            self.final = novo
        atual.next = novo
        self.tamanho += 1

    # remove ordem pelo ID
    def remove_por_id(self, order_id: int):
        item = self.inicio
        while item is not None:
            if item.data.id == order_id:
                if item.prev is not None:
                    item.prev.next = item.next
                else:
                    self.inicio = item.next
                if item.next is not None:
                    item.next.prev = item.prev
                else:
                    self.final = item.prev
                self.tamanho -= 1
                return True
            item = item.next
        print(f"Erro! Ordem #{order_id} não encontrada na lista de vendas.")
        return False

    # retorna (sem remover) a melhor oferta de venda
    def melhor_oferta(self):
        if self.inicio is None:
            return None
        return self.inicio.data

    def esta_vazia(self):
        return self.tamanho == 0

    # imprime a lista de vendas formatada
    def imprime(self):
        item = self.inicio
        if item is None:
            print("  (lista de vendas vazia)")
            return
        while item is not None:
            print(f"  VENDA   | Preço: R${item.data.preco:>8.2f} | "
                  f"Qtd: {item.data.quantidade:>5} | ID: #{item.data.id}")
            item = item.next

class OrderBook:
    """
    Agrega BuyList e SellList em um único Livro de Ofertas.
    Oferece métodos para inserir, remover e exibir as ordens.
    """

    def __init__(self):
        self.compras = BuyList()    # lista de ordens de compra
        self.vendas  = SellList()   # lista de ordens de venda

    # insere a ordem na lista correta conforme o tipo
    def insere_ordem(self, order: Order):
        if order.tipo == 'C':
            self.compras.insere_ordenado(order)
        elif order.tipo == 'V':
            self.vendas.insere_ordenado(order)
        else:
            print(f"Erro! Tipo de ordem inválido: {order.tipo}")

    # remove pelo ID (busca nas duas listas)
    def remove_por_id(self, order_id: int, tipo: str):
        if tipo == 'C':
            return self.compras.remove_por_id(order_id)
        elif tipo == 'V':
            return self.vendas.remove_por_id(order_id)
        return False

    # exibe o livro de ofertas completo
    def display(self):
        print("\n" + "=" * 50)
        print("      LIVRO DE OFERTAS")
        print("=" * 50)
        print(f"  Ordens de VENDA ({self.vendas.tamanho} ordens):")
        self.vendas.imprime()
        print("-" * 50)
        print(f"  Ordens de COMPRA ({self.compras.tamanho} ordens):")
        self.compras.imprime()
        print("=" * 50)

    # acesso rápido às melhores ofertas
    def melhor_compra(self):
        return self.compras.melhor_oferta()

    def melhor_venda(self):
        return self.vendas.melhor_oferta()


if __name__ == "__main__":
    from datetime import datetime

    print("=" * 55)
    print("TESTE — OrderBook: inserção ordenada")
    print("=" * 55)

    livro = OrderBook()

    # Ordens de compra em preços variados
    livro.insere_ordem(Order(1, 'C', 50.00, 100, datetime.now()))
    livro.insere_ordem(Order(2, 'C', 55.00, 200, datetime.now()))
    livro.insere_ordem(Order(3, 'C', 48.00,  50, datetime.now()))

    # Ordens de venda
    livro.insere_ordem(Order(4, 'V', 60.00, 150, datetime.now()))
    livro.insere_ordem(Order(5, 'V', 57.00, 300, datetime.now()))
    livro.insere_ordem(Order(6, 'V', 62.00,  80, datetime.now()))

    livro.display()

    print("\nMelhor compra:", livro.melhor_compra())
    print("Melhor venda: ", livro.melhor_venda())

    print("\n--- Removendo ordem #2 (compra) e #5 (venda) ---")
    livro.remove_por_id(2, 'C')
    livro.remove_por_id(5, 'V')
    livro.display()