import os
import shutil
from pathlib import Path

# Função para varrer a pasta e identificar arquivos
def scan_folder(input_folder):
    return list(Path(input_folder).glob('*.*'))

# Função para separar os arquivos em subpastas por categoria
def extract_category(filename):
    categories = ["A4", "A3", "Bottons", "Adesivos"]
    for category in categories:
        if category in filename:
            return category
    return "Outros"  # Categoria padrão se não puder identificar

# Função para extrair o número de unidades do nome do arquivo
def extract_unit_count(filename):
    try:
        return int(filename.split('_')[-1].split('.')[0])
    except (ValueError, IndexError):
        return 1  # Valor padrão se não puder extrair o número

# Função para organizar os arquivos em pastas por quantidade e categoria
def organize_files(files, output_folder):
    for file in files:
        # Extrair número de unidades e categoria do arquivo
        unit_count = extract_unit_count(file.name)
        category = extract_category(file.name)

        # Cria a pasta de quantidade dentro da pasta de output
        quantity_folder = output_folder / f'{unit_count} unidades'
        quantity_folder.mkdir(exist_ok=True)

        # Cria a subpasta de categoria dentro da pasta de quantidade
        category_folder = quantity_folder / category
        category_folder.mkdir(exist_ok=True)

        # Move o arquivo para a subpasta correta
        shutil.move(str(file), str(category_folder))

# Função para criar a pasta de output
def create_output_folder(output_folder):
    Path(output_folder).mkdir(parents=True, exist_ok=True)

# Função para executar o script do InDesign
def execute_indesign_script(input_folder, output_folder):
    # Aqui, vou supor que existe um script externo para o InDesign
    # que será executado por meio de uma chamada de sistema
    # Exemplo: subprocess.run(['indesign_script.sh', str(input_folder), str(output_folder)])
    pass

# Função para apagar as pastas que não sejam a de output
'''def clean_folders(input_folder, output_folder):
    for item in Path(input_folder).iterdir():
        if item.is_dir() and item != output_folder:
            shutil.rmtree(item)'''

# Main
if __name__ == "__main__":
    input_folder = Path("C:/Users/matheus.araujo/Pictures/Screenshots")
    output_folder = input_folder / "output"

    # Etapa 2: Fazer varredura na pasta
    files = scan_folder(input_folder)

    # Etapa 3: Criar a pasta de output
    create_output_folder(output_folder)

    # Etapa 4: Separar os arquivos em subpastas por número de unidades dentro de output
    organize_files(files, output_folder)

    # Etapa 5: Executar o script do InDesign
    #execute_indesign_script(input_folder, output_folder)

    # Etapa 6: Apagar as pastas que não sejam a de output
    #clean_folders(input_folder, output_folder)
