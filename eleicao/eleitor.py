# eleicao/eleitor.py
from .excecoes import ErroCadastro


class Eleitor:
    def __init__(
        self,
        nome: str,
        cpf: str,
        data_nascimento: str,
        titulo_eleitor: str,
        zona: str,
        secao: str,
    ):
        # Cada self. chama o  valor abaixo chama o setter correspondente
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.titulo_eleitor = titulo_eleitor
        self.zona = zona
        self.secao = secao

    # porperty valida antes de salvar
    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str) -> None:
        if len(valor) == 0 or len(valor) > 50:
            raise ErroCadastro(type(self).__name__, "nome", valor)
        self._nome = valor

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, valor: str) -> None:
        if len(valor) != 11 or not valor.isdigit():
            raise ErroCadastro(type(self).__name__, "cpf", valor)
        self._cpf = valor

    @property
    def data_nascimento(self) -> str:
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, valor: str) -> None:
        self._data_nascimento = valor

    @property
    def titulo_eleitor(self) -> str:
        return self._titulo_eleitor

    @titulo_eleitor.setter
    def titulo_eleitor(self, valor: str) -> None:
        self._titulo_eleitor = valor

    @property
    def zona(self) -> int:
        return self._zona

    @zona.setter
    def zona(self, valor: str) -> None:
        if not str(valor).isdigit():
            raise ErroCadastro(type(self).__name__, "zona", valor)
        self._zona = int(valor)

    @property
    def secao(self) -> int:
        return self._secao

    @secao.setter
    def secao(self, valor: str) -> None:
        if not str(valor).isdigit():
            raise ErroCadastro(type(self).__name__, "secao", valor)
        self._secao = int(valor)
