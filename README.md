# Sistema de Votação - TG1 POD

Trabalho de POD: sistema simplificado de eleição municipal em Python, usando orientação a objetos e um pacote próprio chamado `eleicao`.

## Como rodar

```
python app.py Input/Partidos.txt Input/Eleitores.txt Input/Urnas.txt
```

Os relatórios são gerados na pasta `output`.

## Pacote eleicao

- `excecoes.py`: classe `ErroCadastro`, usada quando algum dado é inválido
- `partido.py`: classe `Partido`
- `eleitor.py`: classe `Eleitor`
- `candidato.py`: classe abstrata `Candidato`, que herda de `Eleitor`
- `prefeito_vereador.py`: classes `Prefeito` e `Vereador`, que herdam de `Candidato`
- `urna.py`: classe `Urna`, que pode ser somada com outra urna usando `+`
- `eleicao.py`: classe `Eleicao`, que guarda tudo em listas e gera os relatórios
