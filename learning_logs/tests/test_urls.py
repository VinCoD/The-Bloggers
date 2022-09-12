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
    
    def test_new_topic_url_resolve(self):

        url = reverse('learning_logs:new_topic')

        self.assertEquals(resolve(url).func, new_topic)
    
    def test_topic_url_resolve(self):
        url = reverse('learning_logs:topic', args=[1])

        self.assertEquals(resolve(url).func, topic)
    
    def test_new_entry_url_resolve(self):
        """ tests the new_entry url"""
        url = reverse('learning_logs:new_entry', args=[1])
        
        self.assertEquals(resolve(url).func, new_entry)
    
    def test_edit_entry_url_resolved(self):
        url = reverse('learning_logs:edit_entry', args=[1])

        self.assertEquals(resolve(url).func, edit_entry)

        self.assertEquals(resolve(url).func, new_entry)

