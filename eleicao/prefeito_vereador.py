# eleicao/prefeito_vereador.py
from .candidato import Candidato
from .partido import Partido
from .excecoes import ErroCadastro


class Prefeito(Candidato):
    # Cada subclasse declara o seu próprio contador, assim os erros de
    # prefeito e de vereador são contados separadamente
    erros_validacao: int = 0

    @classmethod
    def incrementar_erro(cls) -> None:
        cls.erros_validacao += 1

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
        cpf_vice: str,
        plano_governo: str,
    ):
        super().__init__(
            nome, cpf, data_nascimento, titulo_eleitor, zona, secao, numero, partido
        )
        self.cpf_vice = cpf_vice
        self.plano_governo = plano_governo

    # Implementação Candidato

    def validar_numero(self, numero: str) -> None:
        if len(numero) != 2 or not numero.isdigit():
            Prefeito.incrementar_erro()
            raise ErroCadastro("Prefeito", "numero", numero)

    @property
    def cpf_vice(self) -> str:
        return self._cpf_vice

    @cpf_vice.setter
    def cpf_vice(self, valor: str) -> None:
        if len(valor) != 11 or not valor.isdigit():
            raise ErroCadastro("Prefeito", "cpf_vice", valor)
        self._cpf_vice = valor

    @property
    def plano_governo(self) -> str:
        return self._plano_governo

    @plano_governo.setter
    def plano_governo(self, valor: str) -> None:
        self._plano_governo = valor


class Vereador(Candidato):
    erros_validacao: int = 0

    @classmethod
    def incrementar_erro(cls) -> None:
        cls.erros_validacao += 1

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
        bairro: str,
        projeto_lei: str,
    ):
        super().__init__(
            nome, cpf, data_nascimento, titulo_eleitor, zona, secao, numero, partido
        )
        self.bairro = bairro
        self.projeto_lei = projeto_lei

    # Regra dos 5 digitos para vereador, diferente disso da erro
    def validar_numero(self, numero: str) -> None:
        if len(numero) != 5 or not numero.isdigit():
            Vereador.incrementar_erro()
            raise ErroCadastro("Vereador", "numero", numero)

    @property
    def bairro(self) -> str:
        return self._bairro

    @bairro.setter
    def bairro(self, valor: str) -> None:
        self._bairro = valor

    @property
    def projeto_lei(self) -> str:
        return self._projeto_lei

    @projeto_lei.setter
    def projeto_lei(self, valor: str) -> None:
        self._projeto_lei = valor
