
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
        
# execução
if __name__ == "__main__":

    print("=" * 55)
    print("Teste Comportamento FIFO")
    print("=" * 55)

    gen  = OrderGenerator()
    fila = Queue()

    # Insere 5 ordens e mostra a sequência de entrada
    print("\n Inserindo 5 ordens na fila")
    for i in range(5):
        ordem = gen.gera_ordem()
        fila.enqueue(ordem)
        print(f"Entrou: {ordem}")

    print(f"\nTamanho da fila: {fila.size()}")
    print(f"Próxima a sair (peek): {fila.peek()}")

    # Remove todas e confirma que sai na ordem certa (FIFO)
    print("\n Removendo todas as ordens (deve sair na mesma ordem)")
    while not fila.esta_vazia():
        saiu = fila.dequeue()
        print(f"  Saiu: {saiu}")

    print(f"\nFila vazia? {fila.esta_vazia()}")

    print("\n" + "=" * 55)
    print("Teste OrderGenerator: lote de 3 ordens")
    print("=" * 55)
    fila2 = Queue()
    gen2  = OrderGenerator()
    gen2.preenche_fila(fila2, 3)
    print(f"Ordens na fila: {fila2.size()}")
    print(fila2)
