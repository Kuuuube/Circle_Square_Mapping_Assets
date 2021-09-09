from fgs_3_squircular import to_circle, to_square
from PIL import Image
import numpy as np

import warnings
warnings.filterwarnings("ignore")

square = np.asarray(Image.open('base\square_grid_thick_checkerboard.png'))
circle = to_square(square, 'fgs')
circ = Image.fromarray(circle)
circ.save('generated\\fgs_3_squircular_square_grid_thick_checkerboard.png')
