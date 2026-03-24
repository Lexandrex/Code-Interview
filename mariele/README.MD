# Code Interview – Estruturas de Dados

## 1) Problema com Pilha (Stack)

**Nome do problema:**
Valid Parentheses

**Link:**
https://leetcode.com/problems/valid-parentheses/

**Plataforma:**
LeetCode

**Estrutura de dados principal:**
Pilha (Stack)

**Justificativa:**
A pilha é ideal para esse problema porque segue o princípio LIFO (Last In, First Out). Ao percorrer a string, cada caractere de abertura é empilhado. Quando aparece um caractere de fechamento, verifica-se se ele corresponde ao último elemento inserido na pilha. Isso garante a validação correta da ordem e do balanceamento dos parênteses.

---

## 2) Problema com Array 1

**Nome do problema:**
Two Sum

**Link:**
https://leetcode.com/problems/two-sum/

**Plataforma:**
LeetCode

**Estrutura de dados principal:**
Array

**Justificativa:**
O problema envolve percorrer um array em busca de dois elementos cuja soma seja igual a um valor alvo. O uso de array é natural pois os dados já estão organizados sequencialmente. Além disso, pode ser otimizado com uma tabela hash para reduzir a complexidade de tempo.

---

## 3) Problema com Array 2

**Nome do problema:**
Maximum Subarray

**Link:**
https://leetcode.com/problems/maximum-subarray/

**Plataforma:**
LeetCode

**Estrutura de dados principal:**
Array

**Justificativa:**
Esse problema utiliza arrays para encontrar a sublista contínua com maior soma. A estrutura é adequada porque permite percorrer os elementos de forma sequencial, aplicando o algoritmo de Kadane, que resolve o problema de forma eficiente com complexidade O(n).

---

## 4) Problema com Lista Encadeada 1

**Nome do problema:**
Reverse Linked List

**Link:**
https://leetcode.com/problems/reverse-linked-list/

**Plataforma:**
LeetCode

**Estrutura de dados principal:**
Lista Encadeada

**Justificativa:**
Esse problema explora diretamente a manipulação de ponteiros em uma lista encadeada. A estrutura é essencial porque o desafio consiste em inverter os nós sem usar memória extra significativa, apenas reorganizando as referências entre eles.

---

## 5) Problema com Lista Encadeada 2

**Nome do problema:**
Merge Two Sorted Lists

**Link:**
https://leetcode.com/problems/merge-two-sorted-lists/

**Plataforma:**
LeetCode

**Estrutura de dados principal:**
Lista Encadeada

**Justificativa:**
A lista encadeada é ideal porque permite inserir e reorganizar elementos dinamicamente sem necessidade de deslocamento de memória (como ocorreria em arrays). Isso torna o processo de merge mais eficiente ao apenas ajustar os ponteiros entre os nós.
