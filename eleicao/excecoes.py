class ErroCadastro(Exception):
    def __init__(self, tipo_objeto: str, campo: str, valor: str):
        self.tipo_objeto = tipo_objeto
        self.campo = campo
        self.valor = valor
        self.mensagem = f"Erro no cadastro de {tipo_objeto}: O campo '{campo}' com valor '{valor}' é inválido."
        super().__init__(self.mensagem)
