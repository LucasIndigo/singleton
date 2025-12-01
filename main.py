from auth_manager import GerenciadorAutenticacao


def mostrar_estado(rotulo: str, ga: GerenciadorAutenticacao) -> None:
    print(rotulo)
    print("Usuário logado:", ga.obter_usuario_atual())
    print("Há usuário logado:", ga.ha_usuario_logado())
    print("-")


def main() -> None:
    g1 = GerenciadorAutenticacao()
    g2 = GerenciadorAutenticacao()
    print("Mesma instância:", g1 is g2)

    mostrar_estado("Estado inicial", g1)

    g1.entrar("alice", "token-123")
    mostrar_estado("Após login", g2)

    g2.sair()
    mostrar_estado("Após logout", g1)


if __name__ == "__main__":
    main()
