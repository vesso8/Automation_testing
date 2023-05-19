from unittest import TestCase

from blog import Blog


class BlogTest(TestCase):
    def test_create_post(self):
        b = Blog("Test", "Test Author")
        b.create_post("Test title", "Tester")

        self.assertEqual(b.posts[0].title, "Test title")
        self.assertEqual(len(b.posts), 1)


