
Considere uma classe para representar um `Ponto2D`. Esta classe deve ter como atributos as coordenadas `x` e `y` do ponto.

Implemente o restante da classe como a seguir.

* Sobrecarregue o operador `+` (método mágico `__add__`): ele deve poder operar com o parâmetro sendo uma tupla de dois números ou uma instância de `Ponto2D`, retornando o resultado em um objeto da mesma classe do parâmetro.

* Sobrecarregue o operador `*` (método mágico `__mul__`): ele deve poder operar com o parâmetro sendo um número real ou um `Ponto2D`. No primeiro caso, o método deve retornar uma instância de `Ponto2D` resultante da multiplicação do parâmetro pelas coordenadas do ponto. No segundo caso, o método deve retornar o produto interno entre os dois pontos (o produto interno é igual ao produto das coordenadas `x` dos dois pontos somado com o produto das coordenadas `y` dos dois pontos).

* Sobrecarregue o operador `==` (método mágico `__eq__`): dele deve poder operar com o parâmetro sendo uma tupla de dois números ou uma instância de `Ponto2D`, retornando verdadeiro caso as coordenadas dos pontos sejam iguais ou falso caso contrário.

* Sobrecarregue o operador `[]` para retornar a coordenada `x` do ponto se for usado o índice 0 e a coordenada `y` se for usado o índice 1

* Sobrecarregue o operador `[]` para atribuir um valor à coordenada `x` do ponto se for usado o índice 0 e à coordenada `y` se for usado o índice 1
Utilize o código a seguir para testar o seu programa.

 

```python
#Saída esperada:

    `Ponto2D`(0.0, 0.0)
    (7.0, 3.0)
    `Ponto2D`(8.0, -8.0)
    -8.0
    True
    False
    `x`: 7.0, `y`: 6.0
```