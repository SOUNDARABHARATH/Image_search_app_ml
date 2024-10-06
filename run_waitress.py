from image_searcher import Search

searcher = Search(image_dir_path="C:/Users/Soundara Barath/Downloads/Images", 
                  traverse=True, 
                  include_faces=False)

# Option 1: Pythonic API
from PIL import Image

ranked_images = searcher.rank_images("A photo of a bird.", n=5)
for image in ranked_images:
    Image.open(image.image_path).convert('RGB').show()

# Option 2: Launch Flask api from code
from image_searcher.api import run
run(searcher=searcher)