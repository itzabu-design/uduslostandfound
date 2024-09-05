from django.test import TestCase
from django.urls import reverse


class LostItemViewTests(TestCase):

    def setUp(self):
        # Setup run before every test method.
        self.item = LostItem.objects.create(name="Black Wallet", description="Leather wallet with cards", location="Library"),

   def test_view_renders_correct_template(self):
        # Test if the correct template is used by the view.
        response = self.client.get(reverse('lost_item_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/lost_report.html')

    def test_view_contains_lost_item(self):
        # Test if the created lost item is in the view context.
        response = self.client.get(reverse('lost_report'))
        self.assertContains(response, self.item.name)