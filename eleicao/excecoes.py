# eleicao/excecoes.py


class ErroCadastro(Exception):
    def __init__(self, tipo: str, campo: str, valor: str):
        self.tipo = tipo
        self.campo = campo
        self.valor = valor
        mensagem = (
            f"Erro ao cadastrar {tipo}: campo '{campo}' com valor inválido '{valor}'"
        )
        # Passa a mensagem para a Exception, assim str(erro) devolve esse texto
        super().__init__(mensagem)
