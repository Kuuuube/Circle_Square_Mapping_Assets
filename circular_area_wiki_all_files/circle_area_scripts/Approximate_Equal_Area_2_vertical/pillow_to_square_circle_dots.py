from squircle_orig import to_circle, to_square
from PIL import Image
import numpy as np

import warnings
warnings.filterwarnings("ignore")

square = np.asarray(Image.open('base\dot_grid_circle_rgb_gradient.png'))
circle = to_square(square, 'stretch')
circ = Image.fromarray(circle)
circ.save('generated\\simple_stretch_dot_grid_circle_rgb_gradient_circle.png')
