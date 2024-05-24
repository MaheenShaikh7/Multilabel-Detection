#pip install Augmentor

import Augmentor
p=Augmentor.Pipeline(r"C:\Users\AYESHA\Desktop\MultiLabelDetection\data\images\cracks")


from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
# p.flip_top_bottom(probability=0.5)
# p.rotate(probability=1, max_left_rotation=5, max_right_rotation=5)
p.flip_left_right(probability=0.5)
p.zoom_random(probability=0.5, percentage_area=0.8)
p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)
p.random_brightness(probability=0.5, min_factor=0.3, max_factor=0.7)

p.sample(500)