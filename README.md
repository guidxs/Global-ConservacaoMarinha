# Otimização de Alocação de Recursos para Conservação de Áreas Marinhas

Este é um exemplo de código Python que demonstra como otimizar a alocação de recursos para a conservação de áreas marinhas, considerando diferentes critérios como biodiversidade, vulnerabilidade e conectividade.

## Grupo:

- Guilherme Doretto Sobreiro | RM:99674
- Henrique Lima | RM:551528
- Guilherme Fazito | RM:550539

## Descrição

O código utiliza programação dinâmica para maximizar o valor total das áreas selecionadas para conservação, enquanto respeita as restrições de custo e os critérios estabelecidos para cada área.

O algoritmo consiste em calcular um valor único para cada área, com base em seus critérios de biodiversidade, vulnerabilidade e conectividade, utilizando uma média ponderada simples. Em seguida, utiliza programação dinâmica para determinar as áreas a serem selecionadas, considerando os recursos disponíveis e os custos das áreas.

## Como usar

1. Clone o repositório para sua máquina local:
```python
git clone https://github.com/guidxs/Global-ConservacaoMarinha.git
```   
2. Navegue até o diretório do projeto:
```
cd Global-ConservacaoMarinha
```
3. Execute o script Python:
```
python globalmarinha.py
```
4. O resultado será exibido no console, mostrando o valor total otimizado e as áreas selecionadas para conservação, juntamente com seus custos e valores calculados.

## Requisitos

- Python 3.x
- NumPy

## Dados

Os dados das áreas marinhas são fornecidos no formato de uma lista de dicionários, onde cada dicionário representa uma área com suas características, como nome, biodiversidade, vulnerabilidade, conectividade e custo. Estes são dados fictícios utilizados apenas como exemplo no código.

## Referências

- Bellman, R. (1957). Dynamic Programming. Princeton University Press.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms (3rd ed.). MIT Press.

### Artigos Científico

- Yakowitz, S. (1978). Dynamic programming applications in water resources. *Water Resources Research*, 18(4), 673-678. [DOI](https://doi.org/10.1029/wr018i004p00673)
  

