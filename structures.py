# TRABALHO - SIMULADOR DE LIVRO DE OFERTAS
# MEMBRO 1 - Fundação e Estruturas Base
# Descrição: Implementa as classes base que serão usadas por
#            todos os outros membros do grupo.

# ===========
# VERSAO 1
# ===========
class Node:
    # cada nó guarda próximo e anterior
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


# Ordem: registro de uma intenção de compra ou venda
class Order:
    def __init__(self, id: int, tipo: str, preco: float, quantidade: int, timestamp):
        self.id = id # identificador
        self.tipo = tipo # C para compra e V para venda
        self.preco = preco # preço
        self.quantidade = quantidade # volume de ações
        self.timestamp = timestamp # time de recebimento da ordem

    # representação textual da ordem
    def __str__(self):
        return (f"[Ordem #{self.id} | Tipo:{self.tipo} | "
                f"Preço:R${self.preco:.2f} | Qtd:{self.quantidade} | "
                f"Hora:{self.timestamp}]")
    
# ===========
# VERSÃO 2
# ===========
class DoublyLinkedList:

    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamanho = 0

    # insere um novo nó no INÍCIO da lista
    def insere_inicio(self, dado):
        novo = Node(dado)
        if self.inicio is None:
            self.inicio = novo
            self.final = novo
        else:
            novo.next = self.inicio
            self.inicio.prev = novo
            self.inicio = novo
        self.tamanho += 1

    # insere um novo nó no FINAL da lista
    def insere_final(self, dado):
        novo = Node(dado)
        if self.final is None:
            self.inicio = novo
            self.final = novo
        else:
            novo.prev = self.final
            self.final.next = novo
            self.final = novo
        self.tamanho += 1

    # remove o nó que guarda determinado dado: 
    # liga o anterior ao próximo e o próximo ao anterior, 
    # tirando o nó do meio e não deixando nenhum orfão
    def remove(self, dado):
        item = self.inicio
        while item is not None:
            if item.data == dado:
                # Religar o ponteiro do nó anterior
                if item.prev is not None:
                    item.prev.next = item.next
                else:
                    self.inicio = item.next
                # Religar o ponteiro do próximo nó
                if item.next is not None:
                    item.next.prev = item.prev
                else:
                    self.final = item.prev
                self.tamanho -= 1
                return True        # remoção bem sucedida
            item = item.next
        return False        # dado não encontrado

    # remove por ID de Order 
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
        return False

    # imprime todos os elementos da lista
    def imprime(self):
        item = self.inicio
        while item is not None:
            print(" ", item.data)
            item = item.next

    # verifica se a lista está vazia
    def esta_vazia(self):
        return self.tamanho == 0

# ===========
# VERSÃO 3
# ===========
class Stack:

    def __init__(self):
        self.topo    = Node("topo") # nó sentinela: não guarda dado real
        self.tamanho = 0

    # empilha um valor no topo 
    def push(self, valor):
        novo = Node(valor)
        novo.next = self.topo.next
        self.topo.next = novo
        self.tamanho += 1

    # desempilha e retorna o valor do topo
    def pop(self):
        if self.esta_vazia():
            print("Erro! Pilha vazia — não é possível desfazer!")
            return None
        removido = self.topo.next
        self.topo.next = removido.next
        self.tamanho -= 1
        return removido.data

    # apenas espia o topo sem remover
    def peek(self):
        if self.esta_vazia():
            return None
        return self.topo.next.data

    # verifica se a pilha está vazia
    def esta_vazia(self):
        return self.tamanho == 0

    # representação textual
    def __str__(self):
        atual  = self.topo.next
        saida  = "Pilha(undo): "
        while atual:
            saida += str(atual.data) + " -> "
            atual = atual.next
        return saida

# ===========
# VERSÃO 4
# ===========
if __name__ == "__main__":
    from datetime import datetime

    print("=" * 50)
    print("TESTE — Node e Order")
    print("=" * 50)
    o1 = Order(1, 'C', 50.00, 100, datetime.now())
    o2 = Order(2, 'V', 48.50, 200, datetime.now())
    print(o1)
    print(o2)

    print("\n" + "=" * 50)
    print("TESTE — DoublyLinkedList")
    print("=" * 50)
    lista = DoublyLinkedList()
    lista.insere_final(o1)
    lista.insere_final(o2)
    print("Lista após inserções:")
    lista.imprime()
    lista.remove_por_id(1)
    print("Lista após remover ordem #1:")
    lista.imprime()

    print("\n" + "=" * 50)
    print("TESTE — Stack (Pilha de Undo)")
    print("=" * 50)
    pilha = Stack()
    pilha.push(1)
    pilha.push(2)
    pilha.push(3)
    print(pilha)
    print("Pop:", pilha.pop())
    print("Pop:", pilha.pop())
    print(pilha)
