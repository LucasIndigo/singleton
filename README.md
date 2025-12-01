# Atividade – Padrão Singleton (Python)

## Objetivo
Implementar o padrão de projeto Singleton em Python para gerenciar um recurso compartilhado na aplicação. Nesta solução foi escolhido o cenário de Gerenciamento de Autenticação com a classe `GerenciadorAutenticacao`.

## Cenário Implementado: GerenciadorAutenticacao
- Mantém um dicionário em memória com dados de login de usuários.
- Permite registrar login com `username` e `senha`/`token`.
- Permite verificar se existe usuário logado e obter o usuário atual.
- Permite efetuar logout.
- Garante que todos os módulos da aplicação compartilhem o mesmo estado por meio de uma única instância.

## Como o Singleton foi implementado
- A classe `GerenciadorAutenticacao` usa o método mágico `__new__` para garantir que apenas uma instância seja criada.
- A primeira chamada a `GerenciadorAutenticacao()` cria a instância e inicializa o estado interno; chamadas subsequentes retornam a mesma instância.
- A inicialização idempotente é controlada por um flag interno, evitando re-inicialização em chamadas futuras de `__init__`.

### Estrutura
```
GerenciadorAutenticacao
├─ __new__(): controla a criação única da instância
├─ __init__(): inicializa dicionário de sessões e usuário atual
├─ entrar(usuario, segredo)
├─ ha_usuario_logado()
├─ obter_usuario_atual()
└─ sair()
```

## Executar o exemplo (main)
Pré-requisitos: Python 3.9+

Passos:
1. Abra um terminal na pasta do projeto.
2. Execute:
   ```
   python main.py
   ```

Saída esperada (exemplo):
```
Mesma instância: True
Estado inicial
Usuário logado: None
Há usuário logado: False
-
Após login
Usuário logado: alice
Há usuário logado: True
-
Após logout
Usuário logado: None
Há usuário logado: False
-
```

## Arquivos principais
- `auth_manager.py`: implementação da classe Singleton `GerenciadorAutenticacao`.
- `main.py`: script de demonstração do login, obtenção do usuário atual e logout.

## Observações
- O padrão Singleton aqui não usa bibliotecas externas; toda a lógica está no código.
- Em cenários multi-thread, é possível adicionar uma trava (lock) em `__new__` para garantir segurança de concorrência.
- Caso deseje o segundo cenário (logger global), pode-se criar uma classe `FileLogger` com `__new__` semelhante, mantendo um único arquivo de log aberto e métodos `info`, `warning`, `error`.

## Licença
Uso acadêmico.
