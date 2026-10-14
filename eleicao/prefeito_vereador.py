# eleicao/prefeito_vereador.py
from .candidato import Candidato
from .partido import Partido
from .excecoes import ErroCadastro


class Prefeito(Candidato):
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
        zona: int,
        secao: int,
        partido: Partido,
        numero: int,
        cpf_vice: str,
        plano_governo: str,
    ):
        super().__init__(
            nome, cpf, data_nascimento, titulo_eleitor, zona, secao, partido, numero
        )
        self.cpf_vice = cpf_vice
        self.plano_governo = plano_governo

    @property
    def numero(self) -> int:
        return self._numero

    @numero.setter
    def numero(self, valor: int) -> None:

        if len(str(valor)) != 2 or not str(valor).isdigit():
            Prefeito.incrementar_erro()
            # Corrigido para o padrão (tipo_objeto, campo, valor)
            raise ErroCadastro("Prefeito", "número", str(valor))
        self._numero = int(valor)

    @property
    def cpf_vice(self) -> str:
        return self._cpf_vice

    @cpf_vice.setter
    def cpf_vice(self, valor: str) -> None:
        if len(str(valor)) != 11 or not str(valor).isdigit():
            raise ErroCadastro("Prefeito", "CPF do Vice", str(valor))
        self._cpf_vice = str(valor)


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
        zona: int,
        secao: int,
        partido: Partido,
        numero: int,
        bairro: str,
        projeto_lei: str,
    ):
        super().__init__(
            nome, cpf, data_nascimento, titulo_eleitor, zona, secao, partido, numero
        )
        self.bairro = bairro
        self.projeto_lei = projeto_lei

    @property
    def numero(self) -> int:
        return self._numero

    @numero.setter
    def numero(self, valor: int) -> None:
        if len(str(valor)) != 5 or not str(valor).isdigit():
            Vereador.incrementar_erro()

            raise ErroCadastro("Vereador", "número", str(valor))
        self._numero = int(valor)
