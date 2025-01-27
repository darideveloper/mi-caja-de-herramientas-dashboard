from rest_framework import status

from blog import models
from core.test_base.test_views import BlogTestCase


class GroupViewSetTestCase(BlogTestCase):

    def setUp(self):
        # Set endpoint
        super().setUp(endpont="/api/groups/")

    def test_unauthenticated_user_get(self):
        """ Test that unauthenticated users can not access the endpoint """
        
        # Validate response
        self.client.logout()
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_authenticated_user_get(self):
        """ Test that authenticated users can access the endpoint """
        
        # Validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Validate extra content
        json_data = response.json()
        self.assertEqual(json_data["count"], 6)
        self.assertIsNone(json_data["next"])
        self.assertIsNone(json_data["previous"])
        self.assertEqual(len(json_data["results"]), 6)
        
        # Validate data
        groups = models.Group.objects.all()
        results = json_data["results"]
        self.assertEqual(len(groups), 6)
        for group in groups:
            result = list(filter(lambda result: result["id"] == group.id, results))[0]
            self.assertEqual(group.name, result["name"])
            self.assertIn(group.icon.url, result["icon"])
    
    def test_authenticated_user_post(self):
        """ Test that authenticated users can not post to the endpoint """
        
        self.validate_invalid_method("post")
        
    def test_authenticated_user_put(self):
        """ Test that authenticated users can not put to the endpoint """
        
        # add id to endpoint
        self.endpoint += "1/"
        self.validate_invalid_method("put")
        
    def test_authenticated_user_patch(self):
        
        # add id to endpoint
        self.endpoint += "1/"
        self.validate_invalid_method("patch")


class CategoryViewSetTestCase(BlogTestCase):

    def setUp(self):
        # Set endpoint
        super().setUp(endpont="/api/categories/")

    def test_unauthenticated_user_get(self):
        """ Test that unauthenticated users can not access the endpoint """
        
        # Validate response
        self.client.logout()
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_authenticated_user_get(self):
        """ Test that authenticated users can access the endpoint """
        
        # Validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Validate extra content
        json_data = response.json()
        self.assertEqual(json_data["count"], 5)
        self.assertIsNone(json_data["next"])
        self.assertIsNone(json_data["previous"])
        self.assertEqual(len(json_data["results"]), 5)
        
        # Validate data
        categories = models.Category.objects.all()
        results = json_data["results"]
        self.assertEqual(len(categories), 5)
        for category in categories:
            result = list(filter(lambda result: result["id"] == category.id, results))[0]
            self.assertEqual(category.name, result["name"])
            self.assertIn(category.icon.url, result["icon"])
    
    def test_authenticated_user_post(self):
        """ Test that authenticated users can not post to the endpoint """
        
        self.validate_invalid_method("post")
        
    def test_authenticated_user_put(self):
        """ Test that authenticated users can not put to the endpoint """
        
        # add id to endpoint
        self.endpoint += "1/"
        self.validate_invalid_method("put")
        
    def test_authenticated_user_patch(self):
        
        # add id to endpoint
        self.endpoint += "1/"
        self.validate_invalid_method("patch")


class PostViewSetTestCase(BlogTestCase):

    def setUp(self):
        # Set endpoint
        super().setUp(endpont="/api/posts/")
        
        # Create posts
        self.create_post(
            title="Post 1",
            duration=10,
            text="Post 1 text",
            image_name="sample.webp",
            audio_name="sample.mp3",
            video_name="sample.mp4",
        )
        self.create_post(
            title="Post 2",
            duration=20,
            text="Post 2 text",
            image_name="sample.webp",
            audio_name="sample.mp3",
            video_name="sample.mp4",
        )

    def test_unauthenticated_user_get(self):
        """ Test that unauthenticated users can not access the endpoint """
        
        # Validate response
        self.client.logout()
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_authenticated_user_get(self):
        """ Test that authenticated users can access the endpoint """
        
        # Validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Validate extra content
        json_data = response.json()
        self.assertEqual(json_data["count"], 2)
        self.assertIsNone(json_data["next"])
        self.assertIsNone(json_data["previous"])
        self.assertEqual(len(json_data["results"]), 2)
        
        # Loop through posts
        posts = models.Post.objects.all()
        results = json_data["results"]
        self.assertEqual(len(posts), 2)
        for post in posts:
            result = list(filter(lambda result: result["id"] == post.id, results))[0]
            
            # Validate data text
            self.assertEqual(post.title, result["title"])
            self.assertEqual(post.duration, result["duration"])
            self.assertEqual(post.text, result["text"])
            
            # Validate data links
            links = post.links.all()
            self.assertEqual(len(post.links.all()), len(result["links"]))
            self.assertEqual(len(post.links.all()), 2)
            for link in links:
                result_link = list(filter(
                    lambda result_link: result_link["id"] == link.id, result["links"]
                ))[0]
                self.assertEqual(link.name, result_link["name"])
                self.assertEqual(link.url, result_link["url"])
            
            self.assertIn(post.image.url, result["image"])
            self.assertIn(post.audio.url, result["audio"])
            self.assertIn(post.video.url, result["video"])
    
    def test_authenticated_user_post(self):
        """ Test that authenticated users can not post to the endpoint """
        
        self.validate_invalid_method("post")
        
    def test_authenticated_user_put(self):
        """ Test that authenticated users can not put to the endpoint """
        
        # add id to endpoint
        self.endpoint += "1/"
        self.validate_invalid_method("put")
        
    def test_authenticated_user_patch(self):
        
        # add id to endpoint
        self.endpoint += "1/"
        self.validate_invalid_method("patch")
    