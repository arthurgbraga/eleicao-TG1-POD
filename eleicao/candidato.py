# eleicao/candidato.py
from abc import ABC, abstractmethod
from .eleitor import Eleitor
from .partido import Partido


class Candidato(Eleitor, ABC):
    def __init__(
        self,
        nome: str,
        cpf: str,
        data_nascimento: str,
        titulo_eleitor: str,
        zona: int,
        secao: int,
        partido: Partido,
        numero: int,
    ):
        super().__init__(nome, cpf, data_nascimento, titulo_eleitor, zona, secao)
        self.partido = partido

        self.numero = numero

    @property
    @abstractmethod
    def numero(self) -> int:
        pass

    @numero.setter
    @abstractmethod
    def numero(self, valor: int) -> None:
        pass
