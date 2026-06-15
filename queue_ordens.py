
from structures import Node, Order
import random
from datetime import datetime

class Queue:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    #  insere uma ordem no FIM da fila 
    def enqueue(self, order: Order):
        novo = Node(order)
        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.next = novo
            self.fim = novo
        self.tamanho += 1

    # dequeue: remove e retorna a ordem do INÍCIO
    def dequeue(self):
        if self.esta_vazia():
            print("Erro: Fila vazia, nenhuma ordem para processar!")
            return None
        removido = self.inicio
        self.inicio = self.inicio.next
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return removido.data
    # verifica se a fila ta vazia
    def esta_vazia(self):
        return self.tamanho == 0

    # retorna o tamanho da fila
    def size(self):
        return self.tamanho

    # espia a próxima ordem sem removê-la
    def peek(self):
        if self.esta_vazia():
            return None
        return self.inicio.data

    # representação textual da fila
    def __str__(self):
        atual = self.inicio
        saida = "Fila de entrada: "
        while atual is not None:
            saida += str(atual.data) + " -> "
            atual = atual.next
        return saida

class OrderGenerator:
    def __init__(self):
        self._contador_id = 1

    # gera uma única ordem com dados aleatórios
    def gera_ordem(self):
        id_ordem = self._contador_id
        self._contador_id += 1
        tipo = random.choice(['C', 'V']) #compra ou venda
        preco = round(random.uniform(10.0, 200.0), 2) #de 10 a R$200
        quantidade = random.randint(1, 1000) # de 1 a 1000 ações
        ts = datetime.now()
        return Order(id_ordem, tipo, preco, quantidade, ts)

    # gera um lote de N ordens e coloca na fila
    def preenche_fila(self, fila: Queue, n: int):
        for _ in range(n):
            fila.enqueue(self.gera_ordem())
        return fila
