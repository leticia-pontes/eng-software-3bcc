# Palavra

Palavra é um jogo baseado na web, inspirado no popular jogo online Wordle (term.ooo). No Palavra, os jogadores devem adivinhar uma palavra oculta dentro de um número limitado de tentativas. O jogo fornece feedback sobre a precisão das tentativas para ajudar os jogadores a deduzirem a palavra correta.

## Funcionalidades

- Interface interativa e amigável
- Feedback em tempo real sobre as tentativas
- Jogabilidade simples e envolvente
- Possibilidade de salvar a evolução no jogo
- Sistema de conquistas e recompensas

## Instalação

1. Clone o repositório:
   ```
   git clone https://gitlab.com/leticia-pontes/eng-software-termooo
   ```

.. A SER COMPLETADO
   
4. Execute o servidor de desenvolvimento do Django:
   ```
   python manage.py runserver
   ```

## Como Jogar

1. Inicie o jogo visitando o servidor de desenvolvimento local e clicando em JOGAR.
2. Insira sua tentativa no campo de entrada.
3. Envie sua tentativa e receba o feedback.
4. Use o feedback para adivinhar a palavra dentro das tentativas dadas.

## Testes

Execute os testes para garantir que a aplicação está funcionando corretamente:
```
python manage.py test palavra.tests
```
Para verificar a cobertura de código:
```
python -m coverage run manage.py test
coverage report
```

## Pipeline de CI/CD

O projeto utiliza o GitLab CI/CD para integração e implantação contínuas. O pipeline está definido no arquivo `.gitlab-ci.yml` e inclui etapas para testes, construção e implantação da aplicação.

## Docker e Registro de Imagens

O projeto é containerizado usando Docker. A imagem Docker é construída e armazenada no Registro de Contêineres do GitLab.

## Licença

Nenhuma (até o momento).

## Contribuidores

- [Beatriz Barbosa Bandeira](https://github.com/BiabBandeira)
- [Giovana Cristina dos Santos Castro](https://github.com/GiCCastro)
- [Giovana dos Santos Oliveira](https://github.com/giovanaoliveira-14)
- [Isabella Estella de Oliveira](https://github.com/IsaEstellaa)
- [Letícia Alves de Pontes](https://github.com/leticia-pontes)

## Agradecimentos

- Inspirado nos originais [Wordle](https://www.nytimes.com/games/wordle/index.html) e [Termo](https://term.ooo/)
