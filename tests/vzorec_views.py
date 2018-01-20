# class NameTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#
#         user = UserFactory()
#         user.save()
#         user.set_password('medomedo')
#         user.save()
#
#
#     def test_url_path(self):
#         login = self.client.login(username='vaspav', password='medomedo')
#         model_object = Model.objects.first()
#         url = ''.format()
#         resp = self.client.get(url)
#         self.assertEquals(resp.status_code, 200)
#
#
#     def test_url_namespace(self):
#         login = self.client.login(username='vaspav', password='medomedo')
#         model_object = Model.objects.first()
#         url = reverse('', kwargs={'pk': })
#         resp = self.client.get(url)
#         self.assertEquals(resp.status_code, 200)
#
#     def test_correct_template(self):
#         login = self.client.login(username='vaspav', password='medomedo')
#         model_object = Model.objects.first()
#         url = reverse('', kwargs={'pk': })
#         resp = self.client.get(url)
#         self.assertTemplateUsed('/planiranje/plan/update.html')
#
#     def test_redirect_if_not_logged_in(self):
#         model_object = Model.objects.first()
#         url = reverse('', kwargs={'pk': })
#         resp = self.client.get(url)
#         self.assertEquals(resp.status_code, 302)
#         self.assertTemplateUsed('login.html')
