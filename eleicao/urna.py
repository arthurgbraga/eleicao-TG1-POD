# eleicao/urna.py


class Urna:
    def __init__(self, zona: int, secao: int):
        self.zona = zona
        self.secao = secao

        self.votos_prefeito: dict = {}
        self.votos_vereador: dict = {}

    def registrar_voto_prefeito(self, voto: str) -> None:

        voto_formatado = voto
        if voto.strip() == "":
            voto_formatado = "BRANCO"

        if voto_formatado in self.votos_prefeito:
            self.votos_prefeito[voto_formatado] += 1
        else:
            self.votos_prefeito[voto_formatado] = 1

    def registrar_voto_vereador(self, voto: str) -> None:

        voto_formatado = voto
        if voto.strip() == "":
            voto_formatado = "BRANCO"

        if voto_formatado in self.votos_vereador:
            self.votos_vereador[voto_formatado] += 1
        else:
            self.votos_vereador[voto_formatado] = 1

    def __add__(self, outra_urna: "Urna") -> "Urna":

        nova_urna = Urna(zona=None, secao=None)

        for candidato, quantidade in self.votos_prefeito.items():
            nova_urna.votos_prefeito[candidato] = quantidade

        for candidato, quantidade in outra_urna.votos_prefeito.items():
            if candidato in nova_urna.votos_prefeito:
                nova_urna.votos_prefeito[candidato] += quantidade
            else:
                nova_urna.votos_prefeito[candidato] = quantidade

        for candidato, quantidade in self.votos_vereador.items():
            nova_urna.votos_vereador[candidato] = quantidade

        for candidato, quantidade in outra_urna.votos_vereador.items():
            if candidato in nova_urna.votos_vereador:
                nova_urna.votos_vereador[candidato] += quantidade
            else:
                nova_urna.votos_vereador[candidato] = quantidade

        return nova_urna
