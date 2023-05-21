from PIL import Image, ImageFilter
from pathlib import Path

filenames = ["1.jpeg", "2.jpg", "3.jpg", "4.jpg", "5.jpeg"]
current_dir = Path.cwd()
filenames = Path(current_dir).glob('*')
Path('new_dir').mkdir(parents=True, exist_ok=True)

for file in filenames:
    with Image.open(file) as img:
        img.load()
        new_img = img.filter(ImageFilter.CONTOUR)
        # new_img.show()
        new_img.save(Path("new_dir/new_" + f"new_{file}"))