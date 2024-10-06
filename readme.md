# Transformar lista de imagens em arquivo de texto

Esse repositório transforma um ou múltiplos arquivos de imagem em um arquivo de texto usando python3 e  Tesseract

baseado no código de [Hemilibeatriz](https://github.com/Hemilibeatriz/ImagetoText) clique para ver o repositório



## Instalação  
1. Baixe o [python3](https://www.python.org/downloads/) para seu sistema operacional.
2. Verifique se o `pip` do python está instalado com o comando:  ``python3 -m pip --version`` e se nao tiver, baixe-o.
3. Verifique também se o `tkinter` veio instalado com seu python, para testar, execute: ``python3 -m tkinter`` Se uma janela vazia aparecer, o tkinter foi instalado corretamente.
4. Instale os módulos necessários com o comando: ``pip install -r requirements.txt
``.
5. Agora instale o `Tesseract` para seu sistema operacional seguindo a [documentação oficial](https://tesseract-ocr.github.io/tessdoc/Installation.html).
6. se necessário, altere o `path` do Tesseract no arquivo `main.py` na linha `21`.
    - Obs: se voce usar linux, provavelmente nao será necessário tal mudança.

## Execução
- Execute o comando ``python3 main.py`` e em seguida, selecione as imagem através do modal que irá abri e aguarde a finalização.
- após finalização, selecione o local onde o arquivo de texto será salvo.

- exemplo

<img src="https://github.com/parlandin/imagens-to-text-script/blob/ab8467b9bd8041efcc367f30076a837eab5333ca/exe.jpeg" alt="exemplo">


# Tecnologias usadas
- python3
- Tesseract
- opencv-python
- pytesseract
- tk
- tqdm
