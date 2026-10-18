# app.py
# Uso: python app.py <arquivo_partidos> <arquivo_eleitores> <arquivo_urnas>
import sys

from eleicao.partido import Partido
from eleicao.eleitor import Eleitor
from eleicao.prefeito_vereador import Prefeito, Vereador
from eleicao.eleicao import Eleicao
from eleicao.excecoes import ErroCadastro


def ler_registros(caminho: str) -> list:
    # Lê um arquivo de entrada e devolve uma lista de (tipo, campos).
    registros = []
    with open(caminho, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha == "" or linha.startswith("#"):
                continue
            if ":" not in linha:
                continue
            # split(":", 1) corta só no primeiro ":" separa o tipo do resto
            tipo, resto = linha.split(":", 1)
            campos = [c.strip() for c in resto.split(",")]
            registros.append((tipo.strip().upper(), campos))
    return registros


def ler_partidos(sistema: Eleicao, caminho: str) -> None:
    for tipo, dados in ler_registros(caminho):
        try:
            if tipo != "PARTIDO":
                raise ErroCadastro("Linha", "tipo", tipo)
            if len(dados) != 4:
                raise ErroCadastro("Partido", "quantidade de campos", len(dados))

            partido = Partido(dados[0], dados[1], dados[2], dados[3])
            sistema.adicionar_partido(partido)
        # Se der erro a linha não é cadastrada e o for segue para a próxima
        except ErroCadastro as e:
            # Linha inválida é ignorada e o erro é registrado
            sistema.registrar_erro(str(e))


def ler_eleitores(sistema: Eleicao, caminho: str) -> None:
    for tipo, dados in ler_registros(caminho):
        try:
            if tipo == "ELEITOR":
                if len(dados) != 6:
                    raise ErroCadastro("Eleitor", "quantidade de campos", len(dados))
                nome, cpf, nasc, titulo, zona, secao = dados
                eleitor = Eleitor(nome, cpf, nasc, titulo, zona, secao)
                sistema.adicionar_eleitor(eleitor)

            elif tipo == "PREFEITO" or tipo == "VEREADOR":
                if len(dados) != 10:
                    raise ErroCadastro(
                        tipo.capitalize(), "quantidade de campos", len(dados)
                    )
                nome, cpf, nasc, titulo, zona, secao, numero, num_partido = dados[:8]

                # O candidato recebe o objeto Partido, então busca pelo número
                partido = sistema.buscar_partido(num_partido)
                if partido is None:
                    raise ErroCadastro(tipo.capitalize(), "partido", num_partido)

                if tipo == "PREFEITO":
                    candidato = Prefeito(
                        nome,
                        cpf,
                        nasc,
                        titulo,
                        zona,
                        secao,
                        numero,
                        partido,
                        dados[8],
                        dados[9],
                    )
                else:
                    candidato = Vereador(
                        nome,
                        cpf,
                        nasc,
                        titulo,
                        zona,
                        secao,
                        numero,
                        partido,
                        dados[8],
                        dados[9],
                    )
                sistema.adicionar_eleitor(candidato)

            else:
                raise ErroCadastro("Linha", "tipo", tipo)

        except ErroCadastro as e:
            sistema.registrar_erro(str(e))


def ler_urnas(sistema: Eleicao, caminho: str) -> None:
    for tipo, dados in ler_registros(caminho):
        try:
            if tipo != "VOTO":
                raise ErroCadastro("Linha", "tipo", tipo)
            if len(dados) != 5:
                raise ErroCadastro("Voto", "quantidade de campos", len(dados))
            if not dados[0].isdigit():
                raise ErroCadastro("Voto", "zona", dados[0])
            if not dados[1].isdigit():
                raise ErroCadastro("Voto", "secao", dados[1])

            cargo = dados[3].upper()
            if cargo != "PREFEITO" and cargo != "VEREADOR":
                raise ErroCadastro("Voto", "cargo", dados[3])

            numero = dados[4].strip(
                '"'
            )  # remove aspas: "" vira vazio, que é voto branco
            sistema.registrar_voto(int(dados[0]), int(dados[1]), cargo, numero)
        except ErroCadastro as e:
            sistema.registrar_erro(str(e))


def salvar(caminho: str, conteudo: str) -> None:
    with open(caminho, "w", encoding="utf-8", newline="\n") as f:
        f.write(conteudo + "\n")


def main() -> None:
    if len(sys.argv) != 4:
        print(
            "Uso: python app.py <arquivo_partidos> <arquivo_eleitores> <arquivo_urnas>"
        )
        return

    arquivo_partidos = sys.argv[1]
    arquivo_eleitores = sys.argv[2]
    arquivo_urnas = sys.argv[3]

    sistema = Eleicao()

    print("Lendo arquivos de entrada...")
    try:
        # A ordem importa: candidatos precisam dos partidos já cadastrados
        ler_partidos(sistema, arquivo_partidos)
        ler_eleitores(sistema, arquivo_eleitores)
        ler_urnas(sistema, arquivo_urnas)
    except FileNotFoundError as e:
        # e.filename tem o nome do arquivo que não foi encontrado
        print(f"Erro: arquivo '{e.filename}' não encontrado.")
        return

    try:
        salvar("output/eleitores.out", sistema.relatorio_eleitores())
        salvar("output/partidos.out", sistema.relatorio_partidos())
        salvar("output/urnas.out", sistema.relatorio_urnas())
        salvar("output/geral.out", sistema.relatorio_geral())
        salvar("output/erros.out", sistema.relatorio_erros())
    except FileNotFoundError:
        print("Erro: a pasta 'output' não existe.")
        return

    print(
        f"Pronto! Relatórios gerados na pasta 'output'. Erros encontrados: {len(sistema.erros)}"
    )


# Só roda o main quando o arquivo é executado direto (python app.py),
# e não quando ele é importado por outro arquivo
if __name__ == "__main__":
    main()
