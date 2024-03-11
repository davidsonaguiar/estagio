# TESTE PARA ESTAGIO

## Solução 1

Observe o trecho de código abaixo:

```
int INDICE = 13, SOMA = 0, K = 0;
enquanto K < INDICE faça
{
  K = K + 1;
  SOMA = SOMA + K;
}
imprimir(SOMA);
```
Link: [Solucão 1](./solucao1.py)
### Resultado: 91


## Solução 2

Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

Link: [Solucão 2](./solucao2.py)

## Solução 3

Descubra a lógica e complete o próximo elemento:

- a) 1, 3, 5, 7, ___ : Próximo elemento: **9 (7 + 2)**

- b) 2, 4, 8, 16, 32, 64, ____: Próximo elemento: **128 (2^7)**

- c) 0, 1, 4, 9, 16, 25, 36, ____: Próximo elemento: **49 (8^2)**

- d) 4, 16, 36, 64, ____: Próximo elemento: **100 (10^2)**

- e) 1, 1, 2, 3, 5, 8, ____: Próximo elemento: **13 (8 + 5)**

- f) 2,10, 12, 16, 17, 18, 19, ____: Próximo elemento: **20 ((19 - 18) + 19)**

## Solução 4

Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

**Obs.: Assisti uma série de tv que respondia esse problema.**

1. **Primeira ida à sala das lâmpadas:**
   - Ligue o primeiro interruptor e deixe-o ligado por alguns minutos.
   - Desligue o primeiro interruptor e ligue o segundo interruptor.
   - Deixe o segundo interruptor ligado e vá para a sala das lâmpadas.

2. **Na sala das lâmpadas:**
   - A lâmpada que estiver acesa está conectada ao interruptor que foi ligado e depois desligado. 
   - Toque a lâmpada que está acesa para verificar sua temperatura. 
      - Se a lâmpada estiver acesa, mas não estiver quente, então está conectada ao segundo interruptor.
      - Se a lâmpada estiver acesa e estiver quente, então está conectada ao terceiro interruptor.
      - Se a lâmpada estiver apagada, então está conectada ao primeiro interruptor.

Com essa abordagem, você consegue determinar qual interruptor controla qual lâmpada com apenas duas idas à sala das lâmpadas.

## Solução 5

Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

- a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
- b) Evite usar funções prontas, como, por exemplo, reverse;

Link: [Solucão 5](./solucao5.py)