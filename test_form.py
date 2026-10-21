"""Automated tests for index.html (no external dependencies, Python 3 only)."""
import unittest
from html.parser import HTMLParser


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms = []
        self.inputs = []
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "form":
            self.forms.append(attrs)
        elif tag == "input":
            self.inputs.append(attrs)
        elif tag == "button":
            self.buttons.append(attrs)


def load():
    parser = FormParser()
    with open("index.html", encoding="utf-8") as f:
        parser.feed(f.read())
    return parser


class TestHtmlForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = load()

    def find_input(self, field_id):
        return next((i for i in self.page.inputs if i.get("id") == field_id), None)

    def test_form_exists(self):
        self.assertEqual(len(self.page.forms), 1, "Exactly one <form> expected")

    def test_name_field(self):
        field = self.find_input("name")
        self.assertIsNotNone(field, "Name input missing")
        self.assertEqual(field.get("type"), "text")
        self.assertIn("required", field)

    def test_email_field(self):
        field = self.find_input("email")
        self.assertIsNotNone(field, "Email input missing")
        self.assertEqual(field.get("type"), "email")
        self.assertIn("required", field)

    def test_contact_field(self):
        field = self.find_input("contact")
        self.assertIsNotNone(field, "Contact Number input missing")
        self.assertEqual(field.get("type"), "tel")
        self.assertIn("required", field)

    def test_submit_button(self):
        submits = [b for b in self.page.buttons if b.get("type") == "submit"]
        self.assertGreaterEqual(len(submits), 1, "Submit button missing")


if __name__ == "__main__":
    unittest.main(verbosity=2)
