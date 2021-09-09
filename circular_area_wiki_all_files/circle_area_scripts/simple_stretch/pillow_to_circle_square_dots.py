from fgs_3_squircular import to_circle, to_square
from PIL import Image
import numpy as np

import warnings
warnings.filterwarnings("ignore")

square = np.asarray(Image.open('base\dot_grid_square_rgb_gradient.png'))
circle = to_circle(square, 'stretch')
circ = Image.fromarray(circle)
circ.save('generated\\fgs_3_squircular_dot_grid_square_rgb_gradient.png')
