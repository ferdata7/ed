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