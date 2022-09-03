from django.test import SimpleTestCase
from django.urls import resolve, reverse
from learning_logs.views import index, topics, topic, new_topic, new_entry, edit_entry

class TestUrls(SimpleTestCase):

    def test_index_url_resolve(self):

        url = reverse('learning_logs:index')

        self.assertEquals(resolve(url).func, index)
    
    def test_topics_url_resolve(self):

        url = reverse('learning_logs:topics')

        self.assertEquals(resolve(url).func, topics)
    
    def test_new_topics_url_resolve(self):

        url = reverse('learning_logs:new_topic')

        self.assertEquals(resolve(url).func, new_topic)


