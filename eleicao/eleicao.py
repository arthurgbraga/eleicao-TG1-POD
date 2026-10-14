# eleicao/eleicao.py
from .eleitor import Eleitor
from .partido import Partido
from .urna import Urna
from .prefeito_vereador import Prefeito, Vereador
from .excecoes import ErroCadastro


class Eleicao:
    def __init__(self):
        # Listas básicas para armazenar tudo
        self.eleitores: list = []
        self.partidos: list = []
        self.urnas: list = []
        self.erros: list = []

    # --- MÉTODOS DE INSERÇÃO ---
    def adicionar_eleitor(self, eleitor: Eleitor) -> None:
        self.eleitores.append(eleitor)

    def adicionar_partido(self, partido: Partido) -> None:
        self.partidos.append(partido)

    def adicionar_urna(self, urna: Urna) -> None:
        self.urnas.append(urna)

    def registrar_erro(self, erro: ErroCadastro) -> None:
        self.erros.append(erro)

    # --- MÉTODOS DE BUSCA (com for tradicional) ---
    def buscar_partido_por_numero(self, numero: int):
        for partido in self.partidos:
            if partido.numero == numero:
                return partido
        return None

    def buscar_candidato_prefeito(self, numero: str):
        for eleitor in self.eleitores:
            if isinstance(eleitor, Prefeito):
                if str(eleitor.numero) == str(numero):
                    return eleitor
        return None

    def buscar_candidato_vereador(self, numero: str):
        for eleitor in self.eleitores:
            if isinstance(eleitor, Vereador):
                if str(eleitor.numero) == str(numero):
                    return eleitor
        return None

    # --- RELATÓRIOS (Sem truques, apenas if/else e loops básicos) ---
    def relatorio_eleitores(self) -> str:
        total_eleitores = len(self.eleitores)

        # Contadores tradicionais
        total_prefeitos = 0
        total_vereadores = 0

        for eleitor in self.eleitores:
            if isinstance(eleitor, Prefeito):
                total_prefeitos += 1
            elif isinstance(eleitor, Vereador):
                total_vereadores += 1

        relatorio = "Sobre os eleitores:\n"
        relatorio += f"Total de eleitores: {total_eleitores}\n"
        relatorio += f"Total de candidatos a prefeito: {total_prefeitos}\n"
        relatorio += f"Total de candidatos a vereador: {total_vereadores}\n\n"

        # Agrupamento manual com dicionários para Zona e Seção
        zonas_secoes = {}
        for eleitor in self.eleitores:
            zona = eleitor.zona
            secao = eleitor.secao

            if zona not in zonas_secoes:
                zonas_secoes[zona] = {}

            if secao not in zonas_secoes[zona]:
                zonas_secoes[zona][secao] = 0

            zonas_secoes[zona][secao] += 1

        for zona in zonas_secoes:
            relatorio += f"Zona {zona}:\n"
            for secao in zonas_secoes[zona]:
                quantidade = zonas_secoes[zona][secao]
                relatorio += f"  - Seção {secao}: {quantidade} eleitores\n"

        return relatorio

    def relatorio_partidos(self) -> str:
        relatorio = "Sobre os partidos:\n"
        relatorio += f"Total de partidos: {len(self.partidos)}\n\n"

        for partido in self.partidos:
            prefeitos_do_partido = 0
            vereadores_do_partido = 0

            for eleitor in self.eleitores:
                # Se for prefeito E for deste partido
                if isinstance(eleitor, Prefeito) and eleitor.partido == partido:
                    prefeitos_do_partido += 1
                # Se for vereador E for deste partido
                elif isinstance(eleitor, Vereador) and eleitor.partido == partido:
                    vereadores_do_partido += 1

            relatorio += f"Partido: {partido.nome} - Sigla: {partido.sigla}\n"
            relatorio += (
                f"  - Número de candidatos a prefeito: {prefeitos_do_partido}\n"
            )
            relatorio += (
                f"  - Número de candidatos a vereador: {vereadores_do_partido}\n\n"
            )

        return relatorio

    def relatorio_erros(self) -> str:
        relatorio = "Sobre os erros e exceções:\n"
        relatorio += "Mensagens geradas pelas classes de erro:\n"
        for erro in self.erros:
            relatorio += f" - {erro}\n"

        relatorio += "\nAtributos que contabilizam os erros (Classes):\n"
        relatorio += f" - Partido: {Partido.erros_validacao}\n"
        relatorio += f" - Prefeito: {Prefeito.erros_validacao}\n"
        relatorio += f" - Vereador: {Vereador.erros_validacao}\n"

        return relatorio
