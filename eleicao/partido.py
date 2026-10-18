# eleicao/partido.py
from .excecoes import ErroCadastro


class Partido:
    # atributo da clazsse
    erros_validacao: int = 0

    @classmethod
    def incrementar_erro(cls) -> None:
        cls.erros_validacao += 1

    def __init__(self, numero: str, sigla: str, nome: str, cnpj: str):
        self.numero = numero
        self.sigla = sigla
        self.nome = nome
        self.cnpj = cnpj

    # Erro no número não conta no contador
    @property
    def numero(self) -> str:
        return self._numero

    @numero.setter
    def numero(self, valor: str) -> None:
        if not valor.isdigit():
            raise ErroCadastro("Partido", "numero", valor)
        self._numero = valor

    @property
    def sigla(self) -> str:
        return self._sigla

    @sigla.setter
    def sigla(self, valor: str) -> None:
        self._sigla = valor

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str) -> None:
        if len(valor) == 0 or len(valor) > 50:
            Partido.incrementar_erro()
            raise ErroCadastro("Partido", "nome", valor)
        self._nome = valor

    @property
    def cnpj(self) -> str:
        return self._cnpj

    @cnpj.setter
    def cnpj(self, valor: str) -> None:
        if len(valor) != 14 or not valor.isdigit():
            Partido.incrementar_erro()
            raise ErroCadastro("Partido", "cnpj", valor)
        self._cnpj = valor
