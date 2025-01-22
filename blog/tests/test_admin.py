import os

from django.core.files.uploadedfile import SimpleUploadedFile

from core.tests.base import TestMediaAdminBase
from blog import models


class GroupRenderedDataTestCase(TestMediaAdminBase):
    """ Test rendered data in group admin (icons) """
    
    def setUp(self):
        
        # Run base setup
        super().setUp("/admin/blog/group")
        
    def test_rendered_icons_list_view(self):
        """ Validate icons are rendered as img tag """
        
        # Load group list view
        self.set_list_view()
        self.rendered_icons_test_base()
        
    def test_rendered_icons_change_view(self):
        """ Validate icons are rendered as img tag """
        
        # Load group change view
        self.set_change_view()
        self.rendered_icons_test_base()
    
    
class CategoryRenderedDataTestCase(TestMediaAdminBase):
    """ Test rendered data in category admin (icons) """
    
    def setUp(self):
        
        # Run base setup
        super().setUp("/admin/blog/category")
        
    def test_rendered_icons_list_view(self):
        """ Validate icons are rendered as img tag """
        
        # Load group list view
        self.set_list_view()
        self.rendered_icons_test_base()
        
    def test_rendered_icons_change_view(self):
        """ Validate icons are rendered as img tag """
        
        # Load group change view
        self.set_change_view()
        self.rendered_icons_test_base()
        
        
class LinkRenderedDataTestCase(TestMediaAdminBase):
    """ Test rendered data in category admin (icons and urls) """
    
    def setUp(self):
        
        # Run base setup
        super().setUp("/admin/blog/link")
        
    def test_rendered_list_view(self):
        """ Validate icons are rendered as img tag """
        
        # Load group list view
        self.set_list_view()
        
        # Validate icons
        self.rendered_icons_test_base()
        
        # Validate urls
        self.rendered_url_test_base()
        
    def test_rendered_change_view(self):
        """ Validate icons are rendered as img tag """
        
        # Load group change view
        self.set_change_view()
        
        # Validate icons
        self.rendered_icons_test_base()
        
        # Validate urls
        self.rendered_url_test_base()
        

class PostRenderedDataTestCase(TestMediaAdminBase):
    """ Test rendered data in post admin (images, videos and audios) """
    
    def setUp(self):
        
        # Run base setup
        super().setUp("/admin/blog/post")
        
        # Create post
        self.post = models.Post.objects.create(
            title="Test post",
            group=models.Group.objects.create(name="Para dejar de compararte"),
            category=models.Category.objects.create(name="Meditación"),
            duration=10,
            text="#this is a \n **sample text**",
        )
        
        # Add links to post
        links = models.Link.objects.all()
        self.post.links.set(links)
        
        # Add media to post
        
        # media paths
        app_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        project_path = os.path.dirname(app_path)
        media_path = os.path.join(project_path, 'media')
        image_name = 'sample.webp'
        video_name = 'sample.mp4'
        audio_name = 'sample.mp3'
        image_path = os.path.join(media_path, 'images', image_name)
        video_path = os.path.join(media_path, 'videos', video_name)
        audio_path = os.path.join(media_path, 'audios', audio_name)
        
        # read media
        image_file = SimpleUploadedFile(
            name=image_name,
            content=open(image_path, 'rb').read(),
            content_type='image/webp'
        )
        video_file = SimpleUploadedFile(
            name=audio_name,
            content=open(video_path, 'rb').read(),
            content_type='audio/mp3'
        )
        audio_file = SimpleUploadedFile(
            name=video_name,
            content=open(audio_path, 'rb').read(),
            content_type='video/mp4'
        )
        
        # add media to post
        self.post.image = image_file
        self.post.video = video_file
        self.post.audio = audio_file
        self.post.save()
        
    def test_rendered_list_view(self):
        """ Validate icons are rendered as img tag """
        
        # Load group list view
        self.set_list_view()
        
        # Validate image
        self.rendered_image_test_base()
        
    def test_rendered_change_view(self):
        """ Validate icons are rendered as img tag """
        
        # Load group change view
        self.set_change_view()
        
        # Validate media
        self.rendered_image_test_base()
        self.rendered_video_test_base()
        self.rendered_audio_test_base()