# Automação de parâmetros no Autodesk Inventor via interface HTML e scripts Python/iLogic

Este projeto demonstra uma arquitetura de automação do Autodesk Inventor baseada em uma interface web.
A solução permite que parâmetros de um produto sejam definidos externamente por meio de uma interface HTML e aplicados automaticamente a modelos 3D e montagens no Inventor.

Os dados inseridos na interface são processados por um backend em Python (Flask), que gera um arquivo de parâmetros em formato JSON e aciona regras iLogic responsáveis por atualizar parâmetros do modelo e da montagem.

## Passo a passo para execução

- Abrir a peça **sample-object.ipt**, acessar a regra iLogic **UpdateParameters** dentro do Autodesk Inventor e ajustar o diretório onde o arquivo **myParameters.json** é lido
- Abrir o arquivo **server.py** e alterar o parâmetro **FOLDER_PATH**
- Executar o arquivo **server.py**
- Abrir, preencher e executar o arquivo **main.html**

## Tecnologias e dependências

- Autodesk Inventor (testado com versão 2020)
- Python 3.13+
  - Flask 3.x
  - flask-cors 6.x
  - pywin32 311+
- HTML

## Disclaimer

Os arquivos disponibilizados neste repositório têm como objetivo apenas demonstrar a funcionalidade da automação.
Abaixo é possível visualizar o mesmo recurso aplicado a um objeto montado.


![Demo](doc/demo.gif)
