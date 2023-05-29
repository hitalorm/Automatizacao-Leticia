# Automatização para o código de simulação Monte Carlo PENELOPE

Automatização para salvar a energia depositada em um material usando o _tallyEnergyDeposition_ e salvar o arquivo de saída do _tallyPixelImageDetector_.
Esta é uma versão simples da automatização, em que somente a energia inicial é mudada.


Posição da fonte, tipo e tamanho de campo, material, etc, deverão ser setadas manualmente pelo usuário.


Bibliotecas Python necessárias (que não são built-in)
pandas
numpy
regex


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

O próximo passo é editar o arquivo **main.py**

A função **set_in** mostrada na imagem abaixo é responsável por editar o arquivo **penEasy.in**
![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/98d11a65-2fbc-4070-9d26-5b92c71a0d12)
<p align="center">
Figura 3 - Print screen do arquivo **main.py** mostrando a função **set_in** sendo chamada.  
</p>

A função set_in precisa das variáveis (filename, hist, update, energy, material, mat_id, name_geo, seed1,seed2)
filename, hist, energy, material, name_geo, seed1 e seed2 são obtidos do arquivo **dataframe.csv** criado pela função **create_dat.py**
**update** é o intervalo de tempo em que o arquivo de resultado será atualizado (normalmente coloco como 600), 
**mat_id** é o ID do material no arquivo **penEasy.in**. Por exemplo, se mat_id = 1 então o material na linha destacada na figura abaixo no arquivo penEasy.in será mudado para o nome do material que você gostaria.

![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/98ee465f-7dbc-42e4-9c68-cd2eea9906e3)


Voltando ao arquivo **main.py**, para obter o valor da energia depositada em um material específico (obtida usando o tallyEneryDeposition) é necessário usar a função get_out que tem como parâmetros de entrada o número da pasta em que ocorreu a simulação e também o número de materiais no arquivo tallyEnergyDeposition.dat.
Logo abaixo os valores são salvos no arquivo **dataframe.csv**, sendo que no caso mostrado na figura abaixo somente a energia depositada no primeiro material foi salva, caso queira mudar isso, é necessário mudar o índice no vetor **results[]**

![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/9851c2aa-893f-4f28-9ee2-43c5e00b49f4)

Além disso, caso queira salvar o arquivo de resultado do **tallyPixelImageDetect** é necessário editar as linhas 147 e 148, sendo que a primeira é para determinar a localização (no caso da figura pasta v1) e o nome (no caso da figura foi (int(parameters['Energy(eV)'].iloc[index]/1000))+ '-' + parameters['Material'].iloc[index] + '.dat')

Para iniciar as simulações entre no terminal e digite **python3 main.py** e aparecerá a seguinte pergunta:

![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/7aa49973-8160-4ab6-bca6-b2f2dceb22d6)

É possível começar um batch de simulações do zero ou também continuar um que já foram realizadas algumas simulações, logo:

Se responder 'y' a função create_dat será chamada e um arquivo dataframe.csv totalmente novo será criado.
Se responder 'n' então o arquivo dataframe.csv já criado na pasta será usado e a simulação continuará do ponto anterior. O arquivo checkpoint.dat é usado para controlar quantas simulações do batch já foram realizadas.

Se responder 'y' ocorrerá o seguinte:
![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/38ae4b4a-9fc7-4d08-87fd-bbaf4ce11561)

Se responder 'n' e algumas simulações já foram realizadas ocorrerá o seguinte:








