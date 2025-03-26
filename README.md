Usa o Pyautogui para realizar a movimentação automática do cursor do mouse em uma posição aleatória da tela dentro de um intervalo determinado, repetindo o processo um número específico de vezes para simular um comportamento de usuário e evitar que a tela entre em modo de descanso.

---

### **Resumo do Funcionamento**

1. O código pede um número de repetições (`count`).
2. Para cada repetição:
   - Gera uma posição aleatória `(x, y)`.
   - Move o mouse até essa posição em **1 segundo**.
   - Aguarda um tempo aleatório entre **0 e 2 segundos**.
   - Exibe informações no console.
   - Diminui `count`.
3. O loop continua até `count` chegar a 0.

---

### **Possíveis Aplicações**

- Simular movimentos humanos no computador.
- Evitar que a tela entre em modo de descanso.
- Automatizar pequenas interações no sistema operacional.

Esse código é um **script de automação simples** e pode ser modificado para incluir mais ações, como cliques e interações com janelas.

---

### **Explicação do Código**

1. **Importação das bibliotecas**:

   ```python
   import random
   import time
   import pyautogui as pg
   ```

   - `random`: Usada para gerar números aleatórios.
   - `time`: Usada para manipular pausas (delays) na execução.
   - `pyautogui`: Usada para controlar o mouse e o teclado de forma programática.

2. **Definição do número de repetições**:

   ```python
   count = int(input() or 1000)
   ```

   - Solicita um valor do usuário via `input()`, que será convertido para um número inteiro.
   - Caso o usuário não forneça um valor, assume **1000** como valor padrão.

3. **Loop principal**:

   ```python
   while count > 0:
   ```

   - O loop continuará rodando enquanto `count` for maior que zero.

4. **Geração de coordenadas aleatórias**:

   ```python
   x = random.randint(500, 700)
   y = random.randint(100, 1000)
   ```

   - Gera valores aleatórios para a posição `x` (entre **500 e 700**) e `y` (entre **100 e 1000**) onde o cursor será movido.

5. **Definição do tempo de espera aleatório**:

   ```python
   time_to_wait = random.random() * 2
   ```

   - `random.random()` gera um número decimal aleatório entre **0 e 1**.
   - Multiplicando por **2**, o tempo de espera variará entre **0 e 2 segundos**.

6. **Exibição dos valores gerados**:

   ```python
   print(time_to_wait)
   print(count)
   ```

   - Exibe no terminal o tempo de espera gerado e a quantidade de iterações restantes.

7. **Movimentação do mouse**:

   ```python
   pg.moveTo(x, y, 1)
   ```

   - Move o cursor do mouse para a posição `(x, y)`.
   - O movimento leva **1 segundo** para ser concluído.

8. **Espera antes da próxima iteração**:

   ```python
   time.sleep(time_to_wait)
   ```

   - Aguarda um tempo aleatório antes de repetir o processo.

9. **Decremento do contador**:
   ```python
   count = count - 1
   ```
   - Diminui `count` em **1** a cada iteração.
   - Quando `count` chega a **0**, o loop para.

---
