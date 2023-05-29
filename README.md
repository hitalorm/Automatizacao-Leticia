# Automatização para o código de simulação Monte Carlo PENELOPE

Automatização para salvar a energia depositada em um material usando o _tallyEnergyDeposition_ e salvar o arquivo de saída do _tallyPixelImageDetector_.
Esta é uma versão simples da automatização, em que somente a energia inicial, número de histórias e material de detecção podem ser mudados.


Posição da fonte, tipo e tamanho de campo, etc, deverão ser setadas manualmente pelo usuário.


Bibliotecas Python necessárias (que não são built-in)

- pandas

- numpy

- regex


Comece acessando o arquivo **create_dat.py**.

A Figura 1 mostra uma parte do arquivo **create_dat.py**.
Para determinar a(s) energia(s) do feixe incidente altere a linha 30, o(s) nome(s) do(s) arquivo(s) de geometria a ser(em) utilizado(s) pode(m) ser modificado(s) na linha 33, o(s) material(ais) do detector pode(m) ser alterado(s) na linha 36 e o número de histórias pode ser alterado na linha 39.

![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/ef3fd82d-9064-425a-bd27-613de4754a65)

<p align="center">
Figura 1 - Print screen do arquivo create_dat.py
</p>

No arquivo **general.cfg** é possível determinar o número máximo de simulações simultâneas que serão realizadas.
Na figura abaixo o valor é 16, o que significa que 16 threads serão usadas nesta automatização.

![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/8621a028-c915-4585-b47f-5de0ccb0cde9)

<p align="center">
Figura 2- Arquivo general.cfg
</p>

**IMPORTANTE**

Caso você queira fazer simulações com mais de um thread é necessário copiar a pasta '0' e renomeá-la. Se forem 2 threads deve ter a pasta '0' e '1', se forem 3 threads deve conter as pastas '0' '1' e '2' e assim em diante.

O próximo passo é editar o arquivo **main.py**

A função **set_in** mostrada na imagem abaixo é responsável por editar o arquivo **penEasy.in**
![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/98d11a65-2fbc-4070-9d26-5b92c71a0d12)

<p align="center">
Figura 3 - Print screen do arquivo main.py mostrando a função set_in sendo chamada.  
</p>

A função set_in precisa das variáveis (filename, hist, update, energy, material, mat_id, name_geo, seed1,seed2)
somente **update** e **mat_id** devem ser setadas manualmente pelo usuário, as outras são obtidos do arquivo **dataframe.csv** criado pela função **create_dat.py**.

**update** é o intervalo de tempo em que o arquivo de resultado será atualizado (normalmente coloco como 600), 
**mat_id** é o ID do material no arquivo **penEasy.in**. Por exemplo, se mat_id = 1 então o material na linha destacada na figura abaixo no arquivo penEasy.in será mudado para o nome do material que você gostaria.

![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/98ee465f-7dbc-42e4-9c68-cd2eea9906e3)

<p align="center">
Figura 4 - Print screen do arquivo penEasy.in mostrando o material de interesse que será mudado na simulação.  
</p>


Voltando ao arquivo **main.py**, para obter o valor da energia depositada em um material específico (obtida usando o tallyEneryDeposition) é necessário usar a função **get_out** que tem como parâmetros de entrada o número da pasta em que ocorreu a simulação e também o número de materiais no arquivo **tallyEnergyDeposition.dat**.
Logo abaixo os valores são salvos no arquivo **dataframe.csv**, sendo que no caso mostrado na figura abaixo somente a energia depositada no primeiro material foi salva, caso queira mudar isso, é necessário mudar o índice no vetor **results[]**

![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/9851c2aa-893f-4f28-9ee2-43c5e00b49f4)

<p align="center">
Figura 5 - Print screen do arquivo main.py mostrando as etapas de coleção dos resultados.  
</p>

Além disso, caso queira salvar o arquivo de resultado do **tallyPixelImageDetect** é necessário editar as linhas 147 e 148, sendo que a primeira é para determinar a localização (no caso da figura pasta v1) e o nome (no caso da figura foi (energia+ '-' + material + '.dat')

Para iniciar as simulações entre no terminal e digite **python3 main.py** e aparecerá a seguinte pergunta:

![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/7aa49973-8160-4ab6-bca6-b2f2dceb22d6)

<p align="center">
Figura 6 - Print screen do terminal iniciando as simulações.  
</p>


É possível começar um batch de simulações do zero ou também continuar um que já foram realizadas algumas simulações, logo:

Se responder 'y' a função create_dat será chamada e um arquivo **dataframe.csv** totalmente novo será criado.
Se responder 'n' então o arquivo **dataframe.csv** já criado na pasta será usado e a simulação continuará do ponto anterior. O arquivo **checkpoint.dat** é usado para controlar quantas simulações do batch já foram realizadas.

Se responder 'y' ocorrerá o seguinte:
![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/38ae4b4a-9fc7-4d08-87fd-bbaf4ce11561)

<p align="center">
Figura 7 - Print screen do terminal mostrando o resultado após digitar 'y' para a pergunta se deseja criar um dataframe.csv novo.  
</p>


Se responder 'n' e algumas simulações já foram realizadas ocorrerá o seguinte:

![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/e00c415c-cc51-4ce7-af7f-8e700d741f16)

<p align="center">
Figura 8 - Print screen do terminal mostrando o resultado após digitar 'n' para a pergunta se deseja criar um dataframe.csv novo e as simulações irão continuar de onde pararam.  
</p>



Uma vez que uma simulação termine a seguinte mensagem aparecerá:

![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/2bb0b926-0b86-4460-9eef-9efa1865ed4c)

<p align="center">
Figura 9 - Print screen do terminal mostrando o resultado após uma simulação terminar.  
</p>


Nesta etapa os arquivos de resultado estão sendo lidos e as variáveis de interesse estão sendo salvas no **dataframe.csv**, como pode ser visualizado na imagem abaixo:

![image](https://github.com/hitalorm/Automatizacao-Leticia/assets/32619150/955548ca-056f-4b31-aaae-9acebed45583)

<p align="center">
Figura 10 - dataframe.csv após a primeira simulação ter terminado.  
</p>


Quando todas as simulações forem realizadas o script encerrará automaticamente e todos os resultados estarão salvos no arquivo **dataframe.csv** e na pasta **v1**





