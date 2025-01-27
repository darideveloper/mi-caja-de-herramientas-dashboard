import os

from django.contrib.auth.models import User
from django.core.management import call_command
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import status


from blog import models


class BlogTestCase(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        """ Load data only once """
        
        # Load fixtures
        call_command("apps_loaddata")
    
    def setUp(self, endpont="/api/"):
        
        # Create admin user and login to client
        self.admin_user, self.admin_pass, self.user = self.create_admin_user()
        self.token = str(AccessToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        
        # Update endpoint
        self.endpoint = endpont
        
        # File paths
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.project_path = os.path.dirname(os.path.dirname(self.current_path))
        self.media_path = os.path.join(self.project_path, "media")
        self.audios_path = os.path.join(self.media_path, "audios")
        self.images_path = os.path.join(self.media_path, "images")
        self.videos_path = os.path.join(self.media_path, "videos")
        self.icons_path = os.path.join(self.media_path, "icons")
    
    def create_admin_user(self) -> tuple[str, str]:
        """ Create a new admin user and return it
        
        Returns:
            tuple:
                str: Username of the user created
                str: Password of the user created
                User: User created
        """
        
        # Create admin user
        password = "admin"
        user = User.objects.create_superuser(
            username="admin",
            email="test@gmail.com",
            password=password,
        )
        
        return user.username, password, user

    def create_post(
        self,
        title: str,
        duration: int,
        text: str,
        image_name: str,
        audio_name: str,
        video_name: str,
        group: models.Group = None,
        category: models.Category = None,
        links: list[models.Link] = None
    ) -> models.Post:
        """Create a post with the given title, content, group and category.

        Args:
            title (str): The title of the post.
            duration (int): The duration of the post in minutes.
            text (str): The text of the post.
            image_name (str): The path to the image of the post.
            audio_name (str): The path to the audio of the post.
            video_name (str): The path to the video of the
            group (models.Group): The group of the post.
            category (models.Category): The category of the post.
            links (list[models.Link]): The links of the post.

        Returns:
            models.Post: The created post model.
        """
        
        # Create related data
        if not group:
            group = models.Group.objects.first()
        
        if not category:
            category = models.Category.objects.first()
            
        if not links:
            links = models.Link.objects.all()
            
        # Create media
        image_path = os.path.join(self.images_path, image_name)
        video_path = os.path.join(self.videos_path, video_name)
        audio_path = os.path.join(self.audios_path, audio_name)
        
        image_file = SimpleUploadedFile(
            name=image_name,
            content=open(image_path, "rb").read(),
            content_type="image/webp"
        )
        video_file = SimpleUploadedFile(
            name=video_name,
            content=open(video_path, "rb").read(),
            content_type="video/mp4"
        )
        audio_file = SimpleUploadedFile(
            name=audio_name,
            content=open(audio_path, "rb").read(),
            content_type="audio/mp3"
        )

        # Create post
        post = models.Post.objects.create(
            title=title,
            group=group,
            category=category,
            duration=duration,
            text=text,
            image=image_path,
            audio=audio_path,
            video=video_path,
        )
        
        # Add links
        post.links.set(links)
        post.save()
        
        # Add media
        post.image = image_file
        post.audio = audio_file
        post.video = video_file
        post.save()
        
        return post
    
    def validate_invalid_method(self, method: str):
        """ Validate that the given method is not allowed on the endpoint """
        
        response = getattr(self.client, method)(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
