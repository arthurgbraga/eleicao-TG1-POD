# Sistema de Votação - TG1 POD

Trabalho de POD: sistema simplificado de eleição municipal em Python, usando orientação a objetos e um pacote próprio chamado `eleicao`.

## Como rodar

Na pasta do projeto, rode:

```
python app.py Input/Partidos.txt Input/Eleitores.txt Input/Urnas.txt
```

Os relatórios são salvos na pasta `output`:

- `eleitores.out`: total de eleitores e candidatos, e eleitores por zona e seção
- `partidos.out`: partidos e quantidade de candidatos de cada um
- `urnas.out`: votos válidos, brancos e nulos de cada urna
- `geral.out`: prefeito eleito (ou "Segundo Turno") e os 10 vereadores mais votados
- `erros.out`: erros encontrados nos arquivos e os contadores de erro das classes

Se alguma linha dos arquivos estiver errada, ela é ignorada e o erro aparece no `erros.out`.

## Pacote eleicao

- `excecoes.py`: classe `ErroCadastro`, usada quando algum dado é inválido
- `partido.py`: classe `Partido`
- `eleitor.py`: classe `Eleitor`
- `candidato.py`: classe abstrata `Candidato`, que herda de `Eleitor`
- `prefeito_vereador.py`: classes `Prefeito` e `Vereador`, que herdam de `Candidato`
- `urna.py`: classe `Urna`, que pode ser somada com outra urna usando `+`
- `eleicao.py`: classe `Eleicao`, que guarda tudo em listas e gera os relatórios
