from squircle_orig import to_circle, to_square
from PIL import Image
import numpy as np

import warnings
warnings.filterwarnings("ignore")

square = np.asarray(Image.open('base\circle_grid_thick_checkerboard.png'))
circle = to_square(square, 'stretch')
circ = Image.fromarray(circle)
circ.save('generated\\simple_stretch_circle_grid_thick_checkerboard.png')
