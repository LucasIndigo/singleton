from typing import Optional, Dict


class GerenciadorAutenticacao:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia

    def __init__(self):
        if self._inicializado:
            return
        self._sessoes: Dict[str, str] = {}
        self._usuario_atual: Optional[str] = None
        self._inicializado = True

    def entrar(self, usuario: str, segredo: str) -> None:
        self._sessoes[usuario] = segredo
        self._usuario_atual = usuario

    def ha_usuario_logado(self) -> bool:
        return self._usuario_atual is not None

    def obter_usuario_atual(self) -> Optional[str]:
        return self._usuario_atual

    def sair(self) -> None:
        if self._usuario_atual is not None:
            self._sessoes.pop(self._usuario_atual, None)
            self._usuario_atual = None

