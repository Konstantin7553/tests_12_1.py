import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("Иван")

        for _ in range(10):
            runner.walk()

        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Пётр")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Алексей")
        runner2 = Runner("Михаил")
        for _ in range(10):
            runner1.run()
        for _ in range(10):
            runner2.walk()

        self.assertNotAlmostEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()
