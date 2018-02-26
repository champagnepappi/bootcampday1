import unittest
from business import Business

class BusinessTestCase(unittest.TestCase):
  def test_create_business(self):
    business = Business()
    response = business.create_business("andela", "TRM")
    self.assertEqual(response["message"], "Business created successfully")

  def test_cannot_create_duplicate_business(self):
    pass

