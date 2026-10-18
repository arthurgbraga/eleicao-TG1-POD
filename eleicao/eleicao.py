# eleicao/eleicao.py
from .partido import Partido
from .eleitor import Eleitor
from .urna import Urna
from .prefeito_vereador import Prefeito, Vereador

SEPARADOR = "-" * 40


class Eleicao:
    def __init__(self):
        self.eleitores: list = []
        self.partidos: list = []
        self.urnas: list = []
        self.erros: list = []  # mensagens de erro (na ordem em que aconteceram)

    # métodos de inserção
    def adicionar_eleitor(self, eleitor: Eleitor) -> None:
        self.eleitores.append(eleitor)

    def adicionar_partido(self, partido: Partido) -> None:
        self.partidos.append(partido)

    def adicionar_urna(self, urna: Urna) -> None:
        self.urnas.append(urna)

    def registrar_erro(self, mensagem: str) -> None:
        self.erros.append(mensagem)

    # métodos de busca
    # devolve none se não achar
    def buscar_partido(self, numero: str):
        for partido in self.partidos:
            if partido.numero == numero:
                return partido
        return None

    def buscar_urna(self, zona: int, secao: int):
        for urna in self.urnas:
            if urna.zona == zona and urna.secao == secao:
                return urna
        return None

    # "isinstance" confere se o objeto é de uma classe (pra separar candidatos de eleitores comuns)
    def buscar_prefeito(self, numero: str):
        for eleitor in self.eleitores:
            if isinstance(eleitor, Prefeito) and eleitor.numero == numero:
                return eleitor
        return None

    def buscar_vereador(self, numero: str):
        for eleitor in self.eleitores:
            if isinstance(eleitor, Vereador) and eleitor.numero == numero:
                return eleitor
        return None

    def listar_prefeitos(self) -> list:
        prefeitos = []
        for eleitor in self.eleitores:
            if isinstance(eleitor, Prefeito):
                prefeitos.append(eleitor)
        return prefeitos

    def listar_vereadores(self) -> list:
        vereadores = []
        for eleitor in self.eleitores:
            if isinstance(eleitor, Vereador):
                vereadores.append(eleitor)
        return vereadores

    # VOTOS
    def registrar_voto(self, zona: int, secao: int, cargo: str, numero: str) -> None:
        urna = self.buscar_urna(zona, secao)
        # A urna é "criada" no primeiro voto daquela zona
        if urna is None:
            urna = Urna(zona, secao)
            self.adicionar_urna(urna)

        if cargo == "PREFEITO":
            urna.registrar_voto_prefeito(numero)
        elif cargo == "VEREADOR":
            urna.registrar_voto_vereador(numero)

    def contar_votos(self, votos: dict, cargo: str) -> tuple:
        """Separa os votos de uma urna em (validos, brancos, nulos)."""
        validos = 0
        brancos = 0
        nulos = 0
        for numero, quantidade in votos.items():
            if numero == "BRANCO":
                brancos += quantidade
                continue  # pula para o próximo voto

            if cargo == "PREFEITO":
                candidato = self.buscar_prefeito(numero)
            else:
                candidato = self.buscar_vereador(numero)

            # Nulo = número que não pertence a nenhum candidato cadastrado
            if candidato is None:
                nulos += quantidade
            else:
                validos += quantidade
        # Devolve uma tupla; quem chama separa assim: v, b, n = self.contar_votos(...)
        return validos, brancos, nulos

    def somar_urnas(self) -> Urna:
        # Soma todas as urnas usando(__add__)
        total = Urna(None, None)
        for urna in self.urnas:
            total = total + urna
        return total

    def resultado_prefeito(self) -> str:
        total = self.somar_urnas()

        votos_validos = 0
        maior = 0
        prefeito_eleito = None
        for prefeito in self.listar_prefeitos():
            votos = total.votos_prefeito.get(prefeito.numero, 0)
            votos_validos += votos
            if votos > maior:
                maior = votos
                prefeito_eleito = prefeito

        # Precisa de mais da metade dos votos válidos, se não   vai para o segundo turno
        if prefeito_eleito is not None and maior > votos_validos / 2:
            return prefeito_eleito.nome
        return "Segundo Turno"

    def vereadores_mais_votados(self) -> list:
        total = self.somar_urnas()

        vereadores = []
        for vereador in self.listar_vereadores():
            votos = total.votos_vereador.get(vereador.numero, 0)
            vereadores.append((votos, vereador))
        # Ordena pela quantidade de votos (posição 0 da tupla), do maior para o menor,

        vereadores.sort(key=lambda par: par[0], reverse=True)
        return vereadores[:10]

    # RELATÓRIOS (aqui deu red mlk)
    def relatorio_eleitores(self) -> str:
        zonas_secoes = {}
        for eleitor in self.eleitores:
            if eleitor.zona not in zonas_secoes:
                zonas_secoes[eleitor.zona] = {}
            if eleitor.secao not in zonas_secoes[eleitor.zona]:
                zonas_secoes[eleitor.zona][eleitor.secao] = 0
            zonas_secoes[eleitor.zona][eleitor.secao] += 1

        relatorio = f"{SEPARADOR}\nRelatorio de Eleitores\n{SEPARADOR}\n"
        relatorio += f"Eleitores: {len(self.eleitores)}\n"
        relatorio += f"Candidatos a prefeito: {len(self.listar_prefeitos())}\n"
        relatorio += f"Candidatos a vereador: {len(self.listar_vereadores())}\n"

        for zona in sorted(zonas_secoes):
            relatorio += f"\nZona {zona}:\n"
            for secao in sorted(zonas_secoes[zona]):
                relatorio += (
                    f" - Seção {secao}: {zonas_secoes[zona][secao]} eleitores\n"
                )

        relatorio += f"{SEPARADOR}\n"
        return relatorio

    def relatorio_partidos(self) -> str:
        relatorio = f"{SEPARADOR}\nRelatorio de Partidos\n{SEPARADOR}\n"
        relatorio += f"Total de partidos: {len(self.partidos)}\n"

        for partido in self.partidos:
            prefeitos = 0
            vereadores = 0
            for eleitor in self.eleitores:
                # Compara o objeto partido do candidato com o partido do laço
                if isinstance(eleitor, Prefeito) and eleitor.partido == partido:
                    prefeitos += 1
                elif isinstance(eleitor, Vereador) and eleitor.partido == partido:
                    vereadores += 1

            relatorio += f"\n{partido.nome} ({partido.sigla}):\n"
            relatorio += f" - Prefeitos candidatos: {prefeitos}\n"
            relatorio += f" - Vereadores candidatos: {vereadores}\n"

        relatorio += f"{SEPARADOR}\n"
        return relatorio

    def relatorio_urnas(self) -> str:
        # Ordena pela zona e se empatar pela seçao
        urnas_ordenadas = sorted(self.urnas, key=lambda u: (u.zona, u.secao))
        blocos = []
        # o key define o critério de ordenação. O lambda é a funçao curta que para cada urna
        # ela devolve uma tupla com respectivo (zona , secao)
        for urna in urnas_ordenadas:
            vp, bp, np_ = self.contar_votos(urna.votos_prefeito, "PREFEITO")
            vv, bv, nv = self.contar_votos(urna.votos_vereador, "VEREADOR")
            bloco = f"{SEPARADOR}\n"
            bloco += f"Relatorio da Urna - Zona {urna.zona} - Seção {urna.secao}\n"
            bloco += f"{SEPARADOR}\n"
            bloco += f"Votos validos para prefeito: {vp}\n"
            bloco += f"Votos brancos para prefeito: {bp}\n"
            bloco += f"Votos nulos para prefeito: {np_}\n"
            bloco += f"Votos validos para vereador: {vv}\n"
            bloco += f"Votos brancos para vereador: {bv}\n"
            bloco += f"Votos nulos para vereador: {nv}\n"
            bloco += f"{SEPARADOR}\n"
            blocos.append(bloco)
        return "\n".join(blocos)

    def relatorio_geral(self) -> str:
        relatorio = f"{SEPARADOR}\nRelatorio Geral da Eleicao\n{SEPARADOR}\n"
        relatorio += f"Prefeito eleito: {self.resultado_prefeito()}\n"
        relatorio += "Vereadores eleitos:\n"
        for votos, vereador in self.vereadores_mais_votados():
            relatorio += f" - {vereador.nome}: {votos} votos\n"
        relatorio += SEPARADOR
        return relatorio

    def relatorio_erros(self) -> str:
        relatorio = ""
        for mensagem in self.erros:
            relatorio += f"{mensagem}\n"

        relatorio += f"{SEPARADOR}\nRelatorio de Erros\n{SEPARADOR}\n"
        #
        relatorio += f"Partidos com nome ou CNPJ inválido: {Partido.erros_validacao}\n"
        relatorio += (
            f"Candidatos a prefeito com número inválido: {Prefeito.erros_validacao}\n"
        )
        relatorio += (
            f"Candidatos a vereador com número inválido: {Vereador.erros_validacao}\n"
        )
        relatorio += f"{SEPARADOR}\n"
        return relatorio
