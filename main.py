import os
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
from pathlib import Path
import subprocess

# Função para varrer a pasta e identificar arquivos
def scan_folder(input_folder):
    files = list(Path(input_folder).glob('*.*'))
    return files

# Função para separar os arquivos em subpastas por número de unidades
def organize_files(files, output_folder):
    for file in files:
        # Determinar o termo específico ou número de unidades a partir do nome do arquivo
        category = extract_category(file.name)
        subfolder = output_folder / category
        subfolder.mkdir(exist_ok=True)
        shutil.move(str(file), str(subfolder))

# Função fictícia para extrair o número de unidades do nome do arquivo


def extract_category(filename):
    # Termos específicos a serem verificados
    terms = ["A4", "A3", "Bottons", "Adesivos"]

    # Verificar se algum dos termos específicos está no nome do arquivo
    for term in terms:
        if term in filename:
            # Tentar extrair o número de unidades após o termo
            try:
                # Supondo que o formato seja algo como "A4_10.jpg" ou "Bottons_5.png"
                unit_count = int(''.join(filter(str.isdigit, filename.split(term)[-1])))
                return f'{term}_{unit_count} unidades'
            except ValueError:
                return f'{term}_1 unidade'  # Valor padrão se não puder extrair o número

    # Caso nenhum termo específico seja encontrado, usar 'Outros'
    return 'Outros'

# Função para criar a pasta de output
def create_output_folder(output_folder):
    Path(output_folder).mkdir(parents=True, exist_ok=True)

# Função para executar o script do InDesign
'''def execute_indesign_script(input_folder, output_folder):
    # Exemplo de execução de um script do InDesign
    # Certifique-se de ajustar esse comando para o seu ambiente
    subprocess.run(["C:/xampp/htdocs/website/Coletivo_app/ExportPDF.jsx", str(input_folder), str(output_folder)])'''

# Função para apagar as pastas que não sejam a de output
'''def clean_folders(output_folder):
    for item in Path(output_folder).iterdir():
        if item.is_dir():
            shutil.rmtree(item)'''
def start_process():
    input_folder = Path(entry_input.get())
    output_folder = Path(entry_output.get())

    if not input_folder.exists():
        messagebox.showerror("Erro", "A pasta de entrada não existe.")
        return
# Main
if __name__ == "__main__":
    input_folder = Path("C:/Users/matheus.araujo/Pictures/Screenshots")
    output_folder = Path(input_folder) / "output"

    # Etapa 2: Fazer varredura na pasta
    files = scan_folder(input_folder)

    # Etapa 3: Criar a pasta de output
    create_output_folder(output_folder)

    # Etapa 4: Separar os arquivos em subpastas por número de unidades
    organize_files(files, output_folder)

    # Etapa 5: Executar o script do InDesign
    #execute_indesign_script(input_folder, output_folder)

    # Etapa 6: Apagar as pastas dentro da pasta de output
    #clean_folders(output_folder)

 #messagebox.showinfo("Sucesso", "Processo concluído com sucesso!")

def browse_input():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_input.delete(0, tk.END)
        entry_input.insert(0, folder_selected)

# Função para escolher a pasta de saída
def browse_output():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_output.delete(0, tk.END)
        entry_output.insert(0, folder_selected)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Organizador de Arquivos")

# Label e campo de entrada para a pasta de entrada
label_input = tk.Label(root, text="Pasta de Entrada:")
label_input.grid(row=0, column=0, padx=10, pady=10)
entry_input = tk.Entry(root, width=50)
entry_input.grid(row=0, column=1, padx=10, pady=10)
button_input = tk.Button(root, text="Procurar", command=browse_input)
button_input.grid(row=0, column=2, padx=10, pady=10)

# Label e campo de entrada para a pasta de saída
label_output = tk.Label(root, text="Pasta de Saída:")
label_output.grid(row=1, column=0, padx=10, pady=10)
entry_output = tk.Entry(root, width=50)
entry_output.grid(row=1, column=1, padx=10, pady=10)
button_output = tk.Button(root, text="Procurar", command=browse_output)
button_output.grid(row=1, column=2, padx=10, pady=10)

# Botão para iniciar o processo
button_start = tk.Button(root, text="Iniciar Processo", command=start_process)
button_start.grid(row=2, column=1, pady=20)

# Iniciar o loop da interface gráfica
root.mainloop()