# eleicao/urna.py


class Urna:
    def __init__(self, zona: int, secao: int):
        self._zona = zona
        self._secao = secao
        # Voto em branco fica guardado na chave "BRANCOS".
        self._votos_prefeito: dict = {}
        self._votos_vereador: dict = {}

    # zona e secao não podem ser trocadas depois de criar a urna
    @property
    def zona(self) -> int:
        return self._zona

    @property
    def secao(self) -> int:
        return self._secao

    @property
    def votos_prefeito(self) -> dict:
        return self._votos_prefeito

    @property
    def votos_vereador(self) -> dict:
        return self._votos_vereador

    def registrar_voto_prefeito(self, voto: str) -> None:
        if voto.strip() == "":
            voto = "BRANCO"

        if voto in self._votos_prefeito:
            self._votos_prefeito[voto] += 1
        else:
            self._votos_prefeito[voto] = 1

    def registrar_voto_vereador(self, voto: str) -> None:
        if voto.strip() == "":
            voto = "BRANCO"

        if voto in self._votos_vereador:
            self._votos_vereador[voto] += 1
        else:
            self._votos_vereador[voto] = 1

    # Sobrecarga do operador +: para poder escrever urna1 + urna2.
    def __add__(self, outra_urna: "Urna") -> "Urna":
        nova_urna = Urna(None, None)

        for candidato, quantidade in self._votos_prefeito.items():
            nova_urna._votos_prefeito[candidato] = quantidade

        for candidato, quantidade in outra_urna._votos_prefeito.items():
            if candidato in nova_urna._votos_prefeito:
                nova_urna._votos_prefeito[candidato] += quantidade
            else:
                nova_urna._votos_prefeito[candidato] = quantidade

        for candidato, quantidade in self._votos_vereador.items():
            nova_urna._votos_vereador[candidato] = quantidade

        for candidato, quantidade in outra_urna._votos_vereador.items():
            if candidato in nova_urna._votos_vereador:
                nova_urna._votos_vereador[candidato] += quantidade
            else:
                nova_urna._votos_vereador[candidato] = quantidade

        return nova_urna
