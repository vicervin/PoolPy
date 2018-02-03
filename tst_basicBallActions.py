import Pool
import unittest
from kivy.app import App

class TestOne(unittest.TestCase):

    def test_bounce(self):
        """
            Sets up a ball collision to the wall
            and checks if the ball's velocity is updated correctly

        """
        ball = Pool.PoolBall()
        wall = Pool.PoolSide()
        wall.pos = (0, 0)
        ball.pos = (0, 0)
        wall.orient = 0
        speed = (2, 2)

        ball.velocity = speed
        wall.bounce_ball(ball)
        self.assertNotEqual(speed, ball.velocity, "The ball cannot bounce correctly")


    def test_movingBall(self):
        """
            Tests the ball's motion

        """

        ball = Pool.PoolBall()
        ball.velocity = (1, 1)
        ball.pos = (0, 0)

        ball.move()
        self.assertEqual([1, 1], ball.pos, "The ball should have moved to 1, 1")


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
