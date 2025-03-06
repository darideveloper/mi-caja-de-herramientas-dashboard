from rest_framework import status

from blog import models
from core.test_base.test_views import BlogTestCase


class GroupViewSetTestCase(BlogTestCase):

    def setUp(self):
        # Set endpoint
        super().setUp(endpoint="/api/groups/")

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
        self.endpoint = f"{self.endpoint}1/"
        self.validate_invalid_method("put")
        
    def test_authenticated_user_patch(self):
        
        # add id to endpoint
        self.endpoint = f"{self.endpoint}1/"
        self.validate_invalid_method("patch")


class CategoryViewSetTestCase(BlogTestCase):

    def setUp(self):
        # Set endpoint
        super().setUp(endpoint="/api/categories/")

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
        self.endpoint = f"{self.endpoint}1/"
        self.validate_invalid_method("put")
        
    def test_authenticated_user_patch(self):
        
        # add id to endpoint
        self.endpoint = f"{self.endpoint}1/"
        self.validate_invalid_method("patch")


class PostViewSetTestCase(BlogTestCase):

    def setUp(self):
        # Set endpoint
        super().setUp(endpoint="/api/posts/")
        
        # Create posts
        self.post_1 = self.create_post(
            title="Post 1",
            text="Post 1 text",
            image_name="sample.webp",
            audio_name="sample.mp3",
            video_name="sample.mp4",
        )
        self.post_2 = self.create_post(
            title="Post 2",
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
            self.assertEqual(post.id, result["id"])
            self.assertEqual(post.title, result["title"])
            self.assertEqual(post.duration.value, result["duration"])
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
        self.endpoint = f"{self.endpoint}1/"
        self.validate_invalid_method("put")
        
    def test_authenticated_user_patch(self):
        
        # add id to endpoint
        self.endpoint = f"{self.endpoint}1/"
        self.validate_invalid_method("patch")
    
    def test_filter_group(self):
        """ Test that the group filter works """
        
        # Update first post
        group_1 = models.Group.objects.get(id=1)
        group_2 = models.Group.objects.get(id=2)
        self.post_1.group = group_2
        self.post_1.save()
        
        # Get filter
        self.endpoint = f"{self.endpoint}?group=1"
        
        # Validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Validate extra content
        json_data = response.json()
        self.assertEqual(json_data["count"], 1)
        self.assertIsNone(json_data["next"])
        self.assertIsNone(json_data["previous"])
        self.assertEqual(len(json_data["results"]), 1)
        
        # Validate result
        result = json_data["results"][0]
        self.assertTrue(result["id"], self.post_2.id)
        
        # Validate group
        self.assertEqual(result["group"], group_1.id)
    
    def test_filter_category(self):
        """ Test that the category filter works """
        
        # Update first post
        category_1 = models.Category.objects.get(id=1)
        category_2 = models.Category.objects.get(id=2)
        self.post_1.category = category_2
        self.post_1.save()
        
        # Get filter
        self.endpoint = f"{self.endpoint}?category=1"
        
        # Validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Validate extra content
        json_data = response.json()
        self.assertEqual(json_data["count"], 1)
        self.assertIsNone(json_data["next"])
        self.assertIsNone(json_data["previous"])
        self.assertEqual(len(json_data["results"]), 1)
        
        # Validate result
        result = json_data["results"][0]
        self.assertTrue(result["id"], self.post_2.id)
        
        # Validate category
        self.assertEqual(result["category"], category_1.id)
    
    def test_filter_duration(self):
        """ Test that the duration filter works """
        
        # Update first post
        duration_1 = models.Duration.objects.get(id=1)
        duration_2 = models.Duration.objects.get(id=2)
        self.post_1.duration = duration_2
        self.post_1.save()
        
        # Get filter
        self.endpoint = f"{self.endpoint}?duration={duration_1.value}"
        
        # Validate response
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Validate extra content
        json_data = response.json()
        self.assertEqual(json_data["count"], 1)
        self.assertIsNone(json_data["next"])
        self.assertIsNone(json_data["previous"])
        self.assertEqual(len(json_data["results"]), 1)
        
        # Validate result
        result = json_data["results"][0]
        self.assertTrue(result["id"], self.post_2.id)
        
        # Validate duration
        self.assertEqual(result["duration"], duration_1.value)
        
    def test_get_summary(self):
        """ Test that authenticated users can access the endpoint
        and use the summary parameter to get a summary of the posts
        """
        
        # Remove video from first post
        posts = models.Post.objects.all()
        self.post_1.video = None
        self.post_1.save()
        
        # Expected post types
        post_types = ["audio", "video"]
        
        # Get data
        response = self.client.get(f"{self.endpoint}?summary=true")
        json_data = response.json()
        
        # Validate each post data
        results = json_data["results"]
        for post in posts:
            post_index = post.id - 1
            result = list(filter(lambda result: result["id"] == post.id, results))[0]
            
            self.assertEqual(post.id, result["id"])
            self.assertEqual(post.title, result["title"])
            self.assertEqual(result["post_type"], post_types[post_index])
        
        
class RandomPostViewSetTestCase(BlogTestCase):

    def setUp(self):
        # Set endpoint
        super().setUp(endpoint="/api/random-post/")
        
        # Create posts
        self.post_1 = self.create_post(
            title="Post 1",
            text="Post 1 text",
            image_name="sample.webp",
            audio_name="sample.mp3",
            video_name="sample.mp4",
        )
        self.post_2 = self.create_post(
            title="Post 2",
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
        self.assertEqual(json_data["count"], 1)
        self.assertIsNone(json_data["next"])
        self.assertIsNone(json_data["previous"])
        self.assertEqual(len(json_data["results"]), 1)
        
        # Loop through posts
        result = json_data["results"][0]
        result_id = result["id"]
        post = models.Post.objects.get(id=result_id)
        
        # Validate data text
        self.assertEqual(post.title, result["title"])
        self.assertEqual(post.duration.value, result["duration"])
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
        self.endpoint = f"{self.endpoint}1/"
        self.validate_invalid_method("put")
        
    def test_authenticated_user_patch(self):
        
        # add id to endpoint
        self.endpoint = f"{self.endpoint}1/"
        self.validate_invalid_method("patch")