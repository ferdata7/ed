#TRABALHO - SIMULADOR DE LIVRO DE OFERTAS

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
