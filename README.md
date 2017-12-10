# sdProj2
Repositório do projeto de sistemas discretos

Estrutura dos arquivos
======================

Na pasta doc estão os arquivos do relatório (a mesma coisa que está no Overleaf). Na pasta src vai estar código fonte. 

Estrutura do Simulador
======================

O simulador está divido nos seguintes módulos:

- architecture: Base para o funcionamento da aplicação
- channel_codes: Implementação dos códigos de canais
- interface: Interface para o usuário
- simulation: Motor de simulação
- misc: Classes e funções úteis

--- Completar descrições

Módulo architecture
===================
No módulo architecture estão as classes básicas para o simulador.
Com efeito, estas são:

- MatrixBasedImage: representação de imagens usando matrizes
- BinVecBasedImage: representação de imagens usando vetor binário
- ImageConverter: conversor de representações.

GenericImage
------------
Classe que serve de base para as outras. Define os seguintes métodos (que são herdados pelas filhas):
- getRows(): retorna a quantidade de linhas da imagem.
- getCols(): retorna a quantidade de colunas da image.

MatrixBasedImage
----------------
Esse tipo de imagem possui os seguintes métodos:

- getRedMatrix(): retorna a matriz de vermelho da imagem.
- getGreenMatrix(): retorna a matriz de verde da imagem.
- getBlueMatrix(): retorna a matriz de azul da imagem.
- getColor(x,y): retorna uma tupla com três valores, que correspondem,
respectivamente, à quantidade de vermelho, verde e azul no pixel (x,y) informado
- setColor(x,y, red, green, blue): define os valores de vermelho, verde e azul no 
pixel informado como sendo a partir dos valores red, green e blue informados

Exemplo de uso:
<pre>
>>> from src.archtecture.Images import MatrixBasedImage
>>> im = MatrixBasedImage(10,20)
>>> im.getRows()

10

>>> im.getColor(1,1)

(0,0,0)

</pre>

Módulo channel_codes
====================
Lorem ipsum

Módulo interface
================
Lorem ipsum

Módulo simulation
==================
Lorem ipsum

Módulo misc
===========

Lorem ipsum