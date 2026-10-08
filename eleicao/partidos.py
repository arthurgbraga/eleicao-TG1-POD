
from .excecoes import ErroCadastro

class Partido:
    erros_validacao: int = 0

    @classmethod
    def incrementar_erro(cls) -> None:
        cls.erros_validacao += 1

    def __init__(self, numero: int, sigla: str, nome: str, cnpj: str):
        self.numero = numero
        self.sigla = sigla
        self.nome = nome
        self.cnpj = cnpj

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str) -> None:
        if len(valor) > 50:
            Partido.incrementar_erro()
            raise ErroCadastro("Partido", "nome", valor)
        self._nome = valor

    @property
    def cnpj(self) -> str:
        return self._cnpj

    @cnpj.setter
    def cnpj(self, valor: str) -> None:
        if len(str(valor)) != 14 or not str(valor).isdigit():
            Partido.incrementar_erro()
            raise ErroCadastro("Partido", "CNPJ", str(valor))
        self._cnpj = str(valor)