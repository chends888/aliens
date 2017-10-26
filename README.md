# Projeto 8: Modulação/DeModulação BPSK

## Implementação de um chat entre dois computadores com comunicação BPSK (Binary Phase Shift Keying).

## Modulação digital via BPSK:
 É  uma modulação digital utilizada neste projeto para realizar um canal de comunicação entre dois computadores por meio de ondas eletromagnéticas. Nesse esquema, as fases das portadoras representam os níveis 0 e 1. Durante a alteração de um nível 0 para o 1 e vice e versa, a fase da portadora se altera 180º em relação à que era antes.

## Implementação da modulação

 A comunicação criada para esse projeto consiste em um server, que ficará sempre preparado para o recebimento de uma mensagem e um client, que fará requisições e enviará as mensagens. Os dois são softwares desenvolvidos em Python. Há também, dois arquivos do GNURadio, um que representa o transmissor da mensagem, e o outro o receptor desta. A interface criada para a interação do usuário é bem simples, consiste em um chat onde em uma seção é possível enviar as mensagens e na outra é possível ver as mensagens já enviadas (caso do client) ou ver as mensagens recebidas (no caso do server). Para isso acontecer, a mensagem a ser enviada é primeiro modulada e então enviada pelo socket criado e especificado no arquivo. Nesse momento, o receptor da mensagem já deve ter estabelecido uma conexão com este e deve estar preparado para receber a mensagem, demodular esta e exibir os caracteres da dela, um a um.

## Frequência de transmissão e banda

 Para definir a frequência de transmissão (portadora) realizamos testes com o GNURadio para encontrar um valor adequado ao microfone e speaker utilizados, analisando a recepção e o diagrama de constelação. Para isso, alteramos o valor da frequência de modo que os pontos apresentados no diagrama se concentrassem em dois polos, indicando assim, baixa quantidade de ruído e/ou perdas no sinal. A imagem abaixo exemplifica o resultado do diagrama de constelação com a frequência de 2200Hz utilizada:

----------------------------------------------------------------------------------------

O sinal ocupa uma banda de XX.

## Gráficos:

## Validação:
 Para validar o funcionamento desse projeto, ele terá que ser capaz de transmitir uma mensagem de um computador, por meio de uma interface de chat e ela deve ser recebida sem erros em outro computador, na mesma inteface por meio de ondas eletromagnéticas.
