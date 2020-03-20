import png
import numpy as np


x = np.empty([5, 5], dtype="U1")

png.from_array(x).save(test.png)