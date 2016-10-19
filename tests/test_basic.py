import numpy as np
import rotlib
from numpy.testing import assert_array_almost_equal


def test_EV():
    assert_array_almost_equal(rotlib.rotate([1, 0, 0], 'EV', [0, 1, 0, np.pi/2]), [0, 0, 1])
    assert_array_almost_equal(rotlib.rotate([1, 0, 0], 'EV', [0, 1, 0, -np.pi/2]), [0, 0, -1])
    assert_array_almost_equal(rotlib.rotate([1, 0, 0], 'EV', [0, 1, 0, np.pi]), [-1, 0, 0])
    assert_array_almost_equal(rotlib.rotate([1, 0, 0], 'EV', [1, 0, 0, np.pi/4]), [1, 0, 0])
    assert_array_almost_equal(rotlib.rotate([0, 1, 0], 'EV', [1, 0, 0, -np.pi/2]), [0, 0, 1])
    assert_array_almost_equal(rotlib.rotate([0, 1, 0], 'EV', [1, 0, 0, np.pi/6]), [0, np.cos(np.pi/6), -np.sin(np.pi/6)])