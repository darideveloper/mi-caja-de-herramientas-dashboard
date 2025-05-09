from time import sleep

from django.test import LiveServerTestCase
from django.core.management import call_command
from django.conf import settings
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class TestAdminBase(LiveServerTestCase):
    """ Base class to test admin (login and setup) """
    
    def setUp(self, endpont="/admin/"):
        """ Load data, setup and login in each test """
        
        # Load data
        call_command("apps_loaddata")
        
        # Create admin user
        self.admin_user, self.admin_pass, _ = self.create_admin_user()
        
        # Setup selenium
        self.endpoint = endpont
        self.__setup_selenium__()
        self.__login__()

    def tearDown(self):
        """ Close selenium """
        try:
            self.driver.quit()
        except Exception:
            pass

    def __setup_selenium__(self):
        """ Setup and open selenium browser """
        
        chrome_options = Options()
        if settings.TEST_HEADLESS:
            chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(5)
    
    def __login__(self):
        
        # Load login page and get fields
        self.driver.get(f"{self.live_server_url}/admin/")
        sleep(2)
        selectors_login = {
            "username": "input[name='username']",
            "password": "input[name='password']",
            "submit": "button[type='submit']",
        }
        fields_login = self.get_selenium_elems(selectors_login)

        fields_login["username"].send_keys(self.admin_user)
        fields_login["password"].send_keys(self.admin_pass)
        fields_login["submit"].click()

        # Wait after login
        sleep(3)
        
        # Open page
        self.driver.get(f"{self.live_server_url}{self.endpoint}")
        sleep(2)
        
    def set_page(self, endpoint):
        """ Set page """
        self.driver.get(f"{self.live_server_url}{endpoint}")
        sleep(2)
        
    def get_selenium_elems(self, selectors: dict) -> dict[str, WebElement]:
        """ Get selenium elements from selectors

        Args:
            selectors (dict): css selectors to find: name, value

        Returns:
            dict[str, WebElement]: selenium elements: name, value
        """
        fields = {}
        for key, value in selectors.items():
            try:
                fields[key] = self.driver.find_element(By.CSS_SELECTOR, value)
            except Exception:
                fields[key] = None
        return fields
    
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
    
    
class TestMediaAdminBase(TestAdminBase):
    """ Base class to test media in admin models """
    
    def setUp(self, base_endpoint: str):
        """ Start setup
        
        Args:
            base_endpoint (str): base endpoint for the tests
        """
        
        # Run base setup
        super().setUp()
        
        # Replace with 'set_base_endpoint' method
        self.base_endpoint = base_endpoint
        
    def set_list_view(self):
        """ Set list view """
        
        # Load group list view
        self.set_page(self.base_endpoint)
        
    def set_change_view(self):
        """ Set change view """
        
        # Load group change view
        self.set_page(f"{self.base_endpoint}/1/change/")
        
    def rendered_icons_test_base(self):
        """ Validate icons are rendered as img tag """
        
        # css selectors
        selectors = {
            "icon": ".field-icon img",
            "icon_link": ".field-icon a",
        }
        
        # Validate icon is rendered as img tag
        fields = self.get_selenium_elems(selectors)
        self.assertTrue(fields["icon"].get_attribute("src"))
        self.assertTrue(fields["icon_link"].get_attribute("href"))
        self.assertEqual(fields["icon_link"].get_attribute("target"), "_blank")
        
    def rendered_url_test_base(self):
        """ Validate url is rendered as a tag """
        
        # css selectors
        selectors = {
            "url": 'a.url-link',
        }
        
        # Validate url is rendered as a tag
        fields = self.get_selenium_elems(selectors)
        self.assertTrue(fields["url"].get_attribute("href"))
        self.assertEqual(fields["url"].get_attribute("target"), "_blank")
        
    def rendered_image_test_base(self):
        """ Validate image is rendered as img tag """
        
        # css selectors
        selectors = {
            "image": ".field-image img",
            "image_link": ".field-image a",
        }
        
        # Validate image is rendered as img tag
        fields = self.get_selenium_elems(selectors)
        self.assertTrue(fields["image"].get_attribute("src"))
        self.assertTrue(fields["image_link"].get_attribute("href"))
        self.assertEqual(fields["image_link"].get_attribute("target"), "_blank")