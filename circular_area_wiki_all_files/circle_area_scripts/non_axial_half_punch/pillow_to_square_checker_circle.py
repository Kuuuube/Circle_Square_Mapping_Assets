from non_ax_2_pinch import to_circle, to_square
from PIL import Image
import numpy as np

import warnings
warnings.filterwarnings("ignore")

square = np.asarray(Image.open('base\circle_grid_thick_checkerboard.png'))
circle = to_square(square, 'fgs')
circ = Image.fromarray(circle)
circ.save('generated\\non_ax_2_pinch_circle_grid_thick_checkerboard.png')
