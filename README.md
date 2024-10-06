# PALAVRA
Palavra é um jogo baseado na web, inspirado no popular jogo online Wordle (ou term.ooo).<br>
No Palavra, os jogadores devem adivinhar uma palavra oculta dentro de um número limitado de tentativas.<br>
O jogo fornece feedback sobre a precisão das tentativas para ajudar os jogadores a deduzirem a palavra correta.

#### NENHUMA ALTERAÇÃO PODE SER FEITA NESTE PROJETO SEM A DEVIDA COMUNICAÇÃO E AUTORIZAÇÃO.

## Funcionalidades
- Interface interativa e amigável
- Feedback em tempo real sobre as tentativas
- Jogabilidade simples e envolvente
- Possibilidade de salvar a evolução no jogo
- Sistema de conquistas e recompensas

## Instalação

### Clonando o repositório
```bash
git clone https://github.com/leticia-pontes/eng-software-3bcc
cd eng-software-3bcc
```

### Com Docker

1. Construa a imagem Docker:
   ```bash
   docker build -t termo-oo .
   ```
2. Execute o container:
   ```bash
   docker run -d -p 5200:5200 --name palavra-container palavra
   ```
3. Acesse o aplicativo em seu navegador:
   ```bash
   http://localhost:5200
   ```

### Sem Docker

1. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```
2. Instale as dependências:
   ```bash
   pip install django unittest coverage termcolor unidecode python-decouple dj-database-url psycopg2-binary Pillow
   ```

3. Aplique as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
4. Execute o script de inserção no banco de dados:
   ```bash
   python palavra/criar_dicionario.py
   ```
5. Execute o servidor de desenvolvimento do Django:
   ```bash
   python manage.py runserver
   ```
6. Acesse o aplicativo em seu navegador:
   ```bash
   http://localhost:8000
   ```

## Como Jogar
1. Inicie o jogo visitando o servidor de desenvolvimento local e clicando em JOGAR.
2. Efetue o Login. Se não tiver um usuário, crie um em `Cadastre-se`.
2. Insira sua tentativa no campo de entrada.
3. Envie sua tentativa e receba o feedback.
4. Use o feedback para adivinhar a palavra dentro das tentativas dadas.

## Testes

Execute os testes para garantir que a aplicação está funcionando corretamente:
```
python manage.py test
```
Para verificar a cobertura de código:
```
coverage run --source='.' manage.py test
coverage report
```

## Pipeline de CI/CD
O projeto utiliza o GitLab CI/CD para integração e implantação contínuas. O pipeline está definido no arquivo `.gitlab-ci.yml` e inclui etapas para testes, construção e implantação da aplicação.

## Docker e Registro de Imagens
O projeto é containerizado usando Docker. A imagem Docker é construída e armazenada no Registro de Contêineres do GitLab.

## Licença
Nenhuma (até o momento).

## Contribuidores (integrantes do grupo)
- [Beatriz Barbosa Bandeira](https://github.com/BiabBandeira)
- [Giovana Cristina dos Santos Castro](https://github.com/GiCCastro)
- [Giovana dos Santos Oliveira](https://github.com/giovanaoliveira-14)
- [Isabella Estella de Oliveira](https://github.com/IsaEstellaa)
- [Letícia Alves de Pontes](https://github.com/leticia-pontes)

## Agradecimentos
- Inspirado nos originais [Wordle](https://www.nytimes.com/games/wordle/index.html) e [Termo](https://term.ooo/)
