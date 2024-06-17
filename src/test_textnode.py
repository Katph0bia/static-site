import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

class T2stTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("test, 3, 2, 1", "bold")
        self.assertEqual(node, node2)

class T4stTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "italic", "www.url.com")
        node2 = TextNode("This is a text node", "italic", "www.nodesite.pt")
        self.assertEqual(node, node2)

class T3stTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("Quick node", "bold", "www.url.com")
        node2= TextNode("Quick node", "normal", "www.url.com")
        self.assertEqual(node, node2)



if __name__ == "__main__":
    unittest.main()
