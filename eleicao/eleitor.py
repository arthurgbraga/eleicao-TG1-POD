# eleicao/eleitor.py
from .excecoes import ErroCadastro

class Eleitor:
    def __init__(self, nome: str, cpf: str, data_nascimento: str, titulo_eleitor: str, zona: int, secao: int):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.titulo_eleitor = titulo_eleitor
        self.zona = zona
        self.secao = secao

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str) -> None:
        if len(valor) > 50:
            raise ErroCadastro("Eleitor", "nome", valor)
        self._nome = valor

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, valor: str) -> None:
        # CPF deve ter exatamente 11 caracteres numéricos
        if len(str(valor)) != 11 or not str(valor).isdigit():
            raise ErroCadastro("Eleitor", "CPF", str(valor))
        self._cpf = str(valor)