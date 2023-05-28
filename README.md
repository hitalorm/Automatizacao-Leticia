# Automatização para o código de simulação Monte Carlo PENELOPE

Automatização para salvar a energia depositada em um material usando o _tallyEnergyDeposition_ e salvar o arquivo de saída do _tallyPixelImageDetector_
Esta é uma versão simples da automatização, em que somente a energia inicial é mudada.

Posição da fonte, tipo e tamanho de campo, material, etc, serão vari
Comece acessando o arquivo **create_dat.py**.

A Figura 1 mostra uma parte do arquivo **create_dat.py**.
Para determinar a(s) energia(s) do feixe incidente altere a linha 31, o nome do arquivo de geomtria é modificado na linha 34, o(s) material(ais) do detector pode ser alterado na linha 37 e o número de histórias pode ser alterado na linha 40.

![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/f06ea247-2b84-4dae-80a6-e0f22114184d)

<p align="center">
Figura 1 - Print screen do arquivo **create_dat.py**
</p>

No arquivo **general.cfg** é possível determinar o núnero máximo de simulações simultâneas que serão realizadas.
Na figura abaixo o valor é 16, o que significa que 16 threads serão usadas nesta automatização.

![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/8621a028-c915-4585-b47f-5de0ccb0cde9)

<p align="center">
Figura 2- Arquivo **general.cfg**
</p>


