import cv2
import pytesseract
from tkinter import Tk
from tkinter import filedialog
from tqdm import tqdm
import time  # Apenas para simulação de tempo de processamento (opcional)

# Definições de cores ANSI
class Colors:
    RESET = "\033[0m"  # Reseta a cor
    GREEN = "\033[92m"  # Verde

# Inicializa o Tkinter para usar o diálogo de seleção de arquivos
root = Tk()
root.withdraw()  # Esconde a janela principal do Tkinter

# Abre o diálogo para selecionar múltiplas imagens
file_paths = filedialog.askopenfilenames(title="Selecione imagens", filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp")])

# Configura o caminho do Tesseract (Linux geralmente já vem configurado)
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"  # No Linux, o tesseract geralmente está em /usr/bin/

# Variável para armazenar todo o texto extraído
all_text = ""

# Processa cada imagem selecionada com uma barra de progresso verde
for file_path in tqdm(file_paths, desc="Processando imagens", unit="imagem", bar_format=f"{Colors.GREEN}{{l_bar}}{{bar}}{{r_bar}}{Colors.RESET}"):
    image = cv2.imread(file_path)
    
    # Realiza a OCR na imagem com linguagem em português
    text = pytesseract.image_to_string(image, lang="por")
    
    # Adiciona apenas o texto extraído ao texto final, seguido do separador
    all_text += f"{text}\n{'-' * 50}\n"
    
    time.sleep(0.1)  # Simula um tempo de processamento (opcional)

# Abre o diálogo para escolher onde salvar o arquivo de texto
save_path = filedialog.asksaveasfilename(title="Salvar arquivo", defaultextension=".txt", filetypes=[("Arquivo de Texto", "*.txt")])

# Se o usuário escolheu um local para salvar, escreve o texto no arquivo
if save_path:
    print("Salvando arquivo...")
    with open(save_path, "w", encoding="utf-8") as text_file:
        text_file.write(all_text)
    print(f"Texto salvo com sucesso em: {save_path}")
else:
    print("Nenhum local de salvamento foi escolhido.")
