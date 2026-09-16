import unittest
import numpy as np
from src.posture_detector import PostureDetector
from src.eye_detector import EyeDetector

class TestCVMetrics(unittest.TestCase):

    def test_neck_angle_upright(self):
        # shoulder straight below ear
        shoulder = [100.0, 300.0]
        ear = [100.0, 100.0]
        deg = PostureDetector.get_neck_angle(shoulder, ear)
        self.assertAlmostEqual(deg, 0.0, places=1)

    def test_neck_angle_slouched(self):
        # 45 degree tilt forward
        shoulder = [0.0, 100.0]
        ear = [100.0, 0.0]
        deg = PostureDetector.get_neck_angle(shoulder, ear)
        self.assertAlmostEqual(deg, 45.0, places=1)

    def test_synthetic_ear_values(self):
        # synthetic open eye points
        eye_pts = np.array([
            [0.0, 0.0],
            [5.0, 4.0],
            [15.0, 4.0],
            [20.0, 0.0],
            [15.0, -4.0],
            [5.0, -4.0]
        ])
        # formula: (8 + 8) / (2 * 20) = 16 / 40 = 0.40
        ear_val = EyeDetector.calc_ear(eye_pts)
        self.assertAlmostEqual(ear_val, 0.40, places=2)

    def test_closed_eye_ear_values(self):
        # flat eyelids close to zero
        flat_eye = np.array([
            [0.0, 0.0],
            [5.0, 0.1],
            [15.0, 0.1],
            [20.0, 0.0],
            [15.0, -0.1],
            [5.0, -0.1]
        ])
        ear_val = EyeDetector.calc_ear(flat_eye)
        self.assertTrue(ear_val < 0.05)

if __name__ == "__main__":
    unittest.main()