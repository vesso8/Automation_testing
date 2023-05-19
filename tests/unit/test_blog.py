from unittest import TestCase

from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test", "Test Author")

        self.assertEqual("Test", b.title)
        self.assertEqual("Test Author", b.author)
        self.assertEqual(0, len(b.posts))

    def test_repr(self):
        b = Blog("Test", "Test Author")
        b2 = Blog("My Day", "Veso")

        self.assertEqual(b.__repr__(), "Test by Test Author has (0 posts)")
        self.assertEqual(b2.__repr__(), "My Day by Veso has (0 posts)")
    def test_repr_multiple_posts(self):
        b = Blog("Test", "Test Author")
        b.posts = ["tests"]
        self.assertEqual(b.__repr__(), "Test by Test Author has (1 posts)")
        b2 = Blog("My Day", "Veso")
        b2.posts = ["testing", "progress"]
        self.assertEqual(b2.__repr__(), "My Day by Veso has (2 posts)")
    def test_json(self):
        b = Blog("Test", "Test Author")
        expected = {"title": "Test", "author": "Test Author", "posts": b.posts}
        self.assertDictEqual(expected, b.json())


