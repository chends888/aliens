# Projeto 8: Modulação/DeModulação BPSK

## Implementação de um chat entre dois computadores com comunicação BPSK (Binary Phase Shift Keying).

## Modulação digital via BPSK:
 É  uma modulação digital utilizada neste projeto para realizar um canal de comunicação entre dois computadores por meio de ondas eletromagnéticas. Nesse esquema, as fases das portadoras representam os níveis 0 e 1. Durante a alteração de um nível 0 para o 1 e vice e versa, a fase da portadora se altera 180º em relação à que era antes.

## Implementação da modulação

 A comunicação criada para esse projeto consiste em um server, que ficará sempre preparado para o recebimento de uma mensagem e um client, que fará requisições e enviará as mensagens. Os dois são softwares desenvolvidos em Python. Há também, dois arquivos do GNURadio, um que representa o transmissor da mensagem, e o outro o receptor desta. A interface criada para a interação do usuário é bem simples, consiste em um chat onde em uma seção é possível enviar as mensagens e na outra é possível ver as mensagens já enviadas (caso do client) ou ver as mensagens recebidas (no caso do server). Para isso acontecer, a mensagem a ser enviada é primeiro modulada e então enviada pelo socket criado e especificado no arquivo. Nesse momento, o receptor da mensagem já deve ter estabelecido uma conexão com este e deve estar preparado para receber a mensagem, demodular esta e exibir os caracteres da dela, um a um.

## Frequência de transmissão e banda

 Para definir a frequência de transmissão (portadora) realizamos testes com o GNURadio para encontrar um valor adequado ao microfone e speaker utilizados, analisando a recepção e o diagrama de constelação. Para isso, alteramos o valor da frequência de modo que os pontos apresentados no diagrama se concentrassem em dois polos, indicando assim, baixa quantidade de ruído e/ou perdas no sinal. A frequência utilizada é de 2200Hz e a banda ocupada de 

## Gráficos:

## Gráfico no tempo do sinal não codificado da transferência
![1](img/1.1.png)
## Gráfico na frequênica do sinal não codificado da transferência
![2](img/1.2.png)
## Gráfico no tempo do sinal codificado da transferência
![3](img/2.1.png)
## Gráfico na frequênica do sinal codificado da transferência
![4](img/2.2.png)
## Gráfico no tempo do sinal modulado da transferência
![5](img/3.1.png)
## Gráfico na frequênica do sinal modulado da transferência
![6](img/3.2.png)
## Diagrama de constelação da transferência
![7](img/Constellation.png)


## Gráfico no tempo do sinal não codificado da recepção
## Gráfico na frequênica do sinal não codificado da recepção
## Gráfico no tempo do sinal codificado da recepção
## Gráfico na frequênica do sinal codificado da recepção
## Gráfico no tempo do sinal modulado da recepção
## Gráfico na frequênica do sinal modulado da recepção
## Diagrama de constelação da recepção



## Validação:
 Para validar o funcionamento desse projeto, ele terá que ser capaz de transmitir uma mensagem de um computador, por meio de uma interface de chat e ela deve ser recebida sem erros em outro computador, na mesma inteface por meio de ondas eletromagnéticas.
