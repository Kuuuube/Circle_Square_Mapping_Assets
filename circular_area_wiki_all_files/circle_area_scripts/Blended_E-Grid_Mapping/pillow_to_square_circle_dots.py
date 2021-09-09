from biased_squelch_blended import to_circle, to_square
from PIL import Image
import numpy as np

import warnings
warnings.filterwarnings("ignore")

square = np.asarray(Image.open('base\dot_grid_circle_rgb_gradient.png'))
circle = to_square(square, 'elliptical')
circ = Image.fromarray(circle)
circ.save('generated\\biased_squelch_blended_dot_grid_circle_rgb_gradient_circle.png')
