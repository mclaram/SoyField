import os
from PIL import Image

# Caminho para a pasta de entrada e saída
input_dir = 'output_images'
output_dir = 'split_images'

# Dividir a imagem em 20 pedaços (4x5)
num_chunks_x = 5  # Número de pedaços na horizontal
num_chunks_y = 4  # Número de pedaços na vertical

# Função para dividir uma imagem em pedaços
def split_image(image_path, num_chunks_x, num_chunks_y):
    image = Image.open(image_path)
    width, height = image.size

    chunk_width = width // num_chunks_x
    chunk_height = height // num_chunks_y

    image_name = os.path.splitext(os.path.basename(image_path))[0]

    # Cria a pasta de saída se não existir
    os.makedirs(output_dir, exist_ok=True)

    for row in range(num_chunks_y):
        for col in range(num_chunks_x):
            left = col * chunk_width
            top = row * chunk_height
            right = (col + 1) * chunk_width
            bottom = (row + 1) * chunk_height

            # Recorta um pedaço da imagem
            chunk = image.crop((left, top, right, bottom))

            # Salva o pedaço com um nome único
            chunk_path = os.path.join(output_dir, f'{image_name}_chunk{row}_{col}.png')
            chunk.save(chunk_path)
            print(f'Salvou: {chunk_path}')

# Função principal para processar todas as imagens da pasta
def process_images():
    try:
        files = [f for f in os.listdir(input_dir) if f.endswith('.png')]
        for file in files:
            image_path = os.path.join(input_dir, file)
            split_image(image_path, num_chunks_x, num_chunks_y)
            print(f'Imagem {file} dividida com sucesso.')
    except Exception as e:
        print(f'Erro ao processar imagens: {e}')

# Executa o processo
process_images()
