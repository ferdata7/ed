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

