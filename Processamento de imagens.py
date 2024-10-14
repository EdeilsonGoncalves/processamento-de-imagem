# Estrutura de diretórios:
image_processor/
    ├── __init__.py
    ├── processor.py
    └── filters.py

# __init__.py
from .processor import ImageProcessor
from .filters import apply_filter

# processor.py
from PIL import Image

class ImageProcessor:
    def __init__(self, image_path):
        self.image = Image.open(image_path)

    def resize(self, width, height):
        """Redimensiona a imagem para o tamanho especificado."""
        self.image = self.image.resize((width, height))
        return self

    def save(self, output_path, format=None):
        """Salva a imagem no caminho especificado."""
        self.image.save(output_path, format=format)

    def show(self):
        """Exibe a imagem."""
        self.image.show()

# filters.py
from PIL import ImageFilter

def apply_filter(image, filter_type):
    """Aplica um filtro à imagem."""
    if filter_type == 'blur':
        return image.filter(ImageFilter.BLUR)
    elif filter_type == 'sharpen':
        return image.filter(ImageFilter.SHARPEN)
    elif filter_type == 'contour':
        return image.filter(ImageFilter.CONTOUR)
    else:
        raise ValueError("Filtro não reconhecido. Use 'blur', 'sharpen' ou 'contour'.")

# exemplo.py
from image_processor import ImageProcessor, apply_filter

def main():
    # Carrega a imagem
    processor = ImageProcessor("exemplo.jpg")

    # Redimensiona a imagem
    processor.resize(800, 600)

    # Aplica um filtro
    filtered_image = apply_filter(processor.image, 'sharpen')

    # Salva a imagem filtrada
    filtered_image.save("exemplo_filtrado.jpg")

    # Exibe a imagem original
    processor.show()

if __name__ == "__main__":
    main()
