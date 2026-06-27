# Simulador de Livro de Ofertas
**Disciplina:** Estrutura de Dados  
**Professor:** Marcos Mansano Furlan  
**Grupo:** Anderson, Fernando, Geison, Paulo e Renato  
**Objetivo**: Aplicar conceitos de estruturas de dados lineares (Listas Encadeadas, Pilhas e Filas) no desenvolvimento de um motor de negociação financeira. Após isso, realizar análise assintótica do algoritmo para comparar sua performance em cenários de grande volume de dados

---

## Estrutura do Projeto

```
repositorio/
│
├── structures.py        (Node, Order, DoublyLinkedList, Stack)
├── queue_ordens.py      (Queue, OrderGenerator)
├── order_book.py        (BuyList, SellList, OrderBook)
├── engine.py            (MatchEngine, Transaction, main)
└── analysis.ipynb       (medições e gráficos)
```

---

## Como Rodar

### Simulador interativo (terminal)
```
python engine.py
```

### Análise de performance
```
python analysis.ipynb
```

### Testar cada módulo individualmente
```
python structures.py
python queue_ordens.py
python order_book.py
python analysis.py
```

---

## Dependência entre arquivos

```
structures.py
    │
    ├─── queue_ordens.py
    │
    └─── order_book.py
            │
            └─── engine.py -> integra tudo

 analysis.ipynb
```

---

## Fluxo do Sistema

```
Nova Ordem
    │
    ▼
Fila de Entrada (Queue - FIFO)
    │
    ▼
Motor de Match (MatchEngine)
    │
    ├──► Insere no Livro (BuyList ou SellList)
    │
    ├──► Empilha ID na Stack (para Undo)
    │
    └──► Verifica Match:
              compra.preco >= venda.preco?
              SIM → execute_trade() → registra Transaction
              NÃO → aguarda próxima ordem
```

---

## Regras do Trabalho

- **Proibido** usar `list` do Python como estrutura de dados principal
- Todas as estruturas devem ser baseadas em **nós encadeados**
- Entregar: `.py` + `.ipynb` + link do repositório
