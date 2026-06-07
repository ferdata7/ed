# Fundação e Estruturas Base

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