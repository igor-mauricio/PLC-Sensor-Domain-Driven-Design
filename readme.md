# Atividade 01 - Exibir os valores das grandezas dos instrumentos de medição em uma indústria

## Descrição

Você precisa desenvolver um programa capaz de exibir os valores das grandezas dos instrumentos de medição (sensores de temperatura, sensores de vazão e sensores de pressão) em uma indústria. Cada conjunto de instrumento deve estar associado a um CLP específico.

Então, o usuário do programa deve indicar o CLP e o instrumento que deseja obter o valor da medição, e seu programa deve indicar o valor da grandeza medida correspondente ao instrumento.
 33
Seu programa deve ser capaz de detectar, sem interromper a execução, erros de entrada de dados. Sendo assim, crie uma função para validar a entrada de dados e, caso necessário, trate exceções.

Além disso, crie funções para formatar os dados para cada tipo de instrumento, bem como para gerar um valor aleatório que emule a leitura do instrumento. Por exemplo, uma função denominada lerSensorTemperatura, que recebe como parâmetro o nome do sensor indicado pelo usuário do programa e deve retornar a temperatura medida (um valor aleatório, porém com sentido físico) com a unidade ºC.

Para implementar este programa, utilize lista e/ou dicionário e/ou tupla etc. Atenção, escolha o tipo adequado para implementar este programa.

Para facilitar, caso necessário, fixe a quantidade de CLPs e instrumentos da indústria.

## Como executar o programa principal
### Programa Principal
```bash
python3 main.py
```

### Criação de Ambiente virtual (Linux)
```bash
python3 -m pip install virtualenv
python3 -m virtualenv .venv
source virtualenv .venv
```
### Instalação de dependências
```bash
pip install -r requirements.txt
```
### Rodar Testes
```bash
pytest
```


