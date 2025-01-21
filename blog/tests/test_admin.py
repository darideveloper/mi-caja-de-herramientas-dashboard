from core.tests.base import TestMediaAdminBase


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