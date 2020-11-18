# Ana
Assistente feita em python, usando speech recognition e APIs do Google de TTS e STT. para IoT e controle de PC.

## Dependencias:

* ### Python:
    Para utilizar a assistente vc precisara de um interpretador python 3.xx.

* ### Microfone:
    Sera necessario um microfone para realização dos comandos de voz.

## Instalação:

Para instalar as bibliotecas utilize:
```pip install -r requirements.txt ```


## Credenciais:

Para utilizar a assistente sera necessario uma chave de autenticação do Google Cloud e do openweathermap, sendo essas possivies conseguir nos sites dos mesmos.
Na pasta config tem um exemplo de arquivo **keys.json**
## Utilização:

Para rodar a assitente utilize :
```python3 ana.py```

## Estrutura:

* Arquivo principal = 'ana.py'.
* Pasta audios contem o audio padrão e os audios pre-definidos. 
* Pasta config com as autenticações e configurações principais. 
* Pasta func com arquivo fbase com as funções de comando e criaaudio para geração dos audios. 
* Pasta utils com informações uteis e ferramentas.
