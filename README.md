# CPF (Cadastro de Pessoa Física)

Toda pessoa que se inscreve no Cadastro de Pessoas Físicas da Receita Federal do Brasil recebe um número de inscrição de onze dígitos decimais com a seguinte configuração: ABC.DEF.GHI-JK.

* Os primeiros oito dígitos, ABCDEFGH, formam o número-base definido pela Receita Federal no momento da inscrição. <br>
* O nono dígito, I, define a Região Fiscal responsável pela inscrição. <br>
* O penúltimo, J, é o dígito verificador dos nove primeiros. <br>
* O último, K, é o dígito verificador dos noves anteriores a ele. <br>

![image](https://github.com/RafaSalomao/validador-de-cpf/assets/107009450/c59d9ef5-3244-4d39-9f4f-88d927104589)

A Região Fiscal onde é emitido o CPF (definida pelo nono dígito) tem as seguintes identificações:

1 - DF, GO, MS, MT e TO <br>
2 - AC, AM, AP, PA, RO e RR <br>
3 - CE, MA e PI <br>
4 - AL, PB, PE, RN <br>
5 - BA e SE <br>
6 - MG <br>
7 - ES e RJ <br>
8 - SP <br>
9 - PR e SC <br>
0 - RS <br>
