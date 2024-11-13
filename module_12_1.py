import unittest as ut
from Module_12.runner import Runner


class RunnerTest(ut.TestCase):
    def test_walk(self):
        self.runner = Runner('Stiv')
        for _ in range(10):
            self.runner.walk()
        self.assertEqual(self.runner.distance, 50)

    def test_run(self):
        self.runner = Runner('Tod')
        for _ in range(10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 100)

    def test_challenge(self):
        self.runner1 = Runner('Anna')
        self.runner2 = Runner('Nikita')
        for _ in range(10):
            self.runner1.run()
        for _ in range(10):
            self.runner2.walk()
        self.assertNotEqual(self.runner1.distance, self.runner2.distance)