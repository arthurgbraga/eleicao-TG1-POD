# eleicao/candidato.py
from abc import ABC, abstractmethod
from .eleitor import Eleitor
from .partido import Partido

# Herda de Eleitor porque todos os candidatos também votam então são eleitoesr.
# herdam de ABC para ser classe abstrata: não dá para criar um candidato direto,só um Prefeito ou um Vereador.


class Candidato(Eleitor, ABC):
    def __init__(
        self,
        nome: str,
        cpf: str,
        data_nascimento: str,
        titulo_eleitor: str,
        zona: str,
        secao: str,
        numero: str,
        partido: Partido,
    ):
        # Reaproveita o INIT do eleitor 9e seus atributos de nome, cpf, etc....)
        super().__init__(nome, cpf, data_nascimento, titulo_eleitor, zona, secao)
        # Essa atribuição passa pelo setter de numero, que chama validar_numero
        # porque cada um tem seu tamanho especifico para valdar
        self.numero = numero
        self.partido = partido

    # Cada subclasse tem sua própria regra (prefeito 2 dígitos, vereador 5)
    @abstractmethod
    def validar_numero(self, numero: str) -> None:
        pass

    # numero fica como str para não perder zero (07 é diferente de 7 ai não iria computar certo)
    @property
    def numero(self) -> str:
        return self._numero

    @numero.setter
    def numero(self, valor: str) -> None:
        self.validar_numero(valor)
        self._numero = valor

    @property
    def partido(self) -> Partido:
        return self._partido

    @partido.setter
    def partido(self, valor: Partido) -> None:
        self._partido = valor
