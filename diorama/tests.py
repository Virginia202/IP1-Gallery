from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class ImageTestClass(TestCase):

    #setup method
     '''
    Set up method to run before each test cases.
    '''
    def setUp(self):
        nairobi = Location(name='nairobi')
        nairobi.save()
        cat = Category(name='cats')
        cat.save()
        
        self.kittens= Image(image = 'jpg', image_name= 'kittens', image_description= 'beautiful', image_location= nairobi,image_category=cat)
        self.kittens.save()

    #test instance
    def test_instance(self):
    '''
    This test tests if an object is initialized properly.
    '''
        self.assertTrue(isinstance(self.kittens,Image))

    #save method
    def test_save_method(self):
    '''
    This is to to test if images are saved.
    '''    
        self.kittens.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    
    #delete method
    def delete_image_method(self):
    '''
    This is to test if an image can be deleted.
    '''    
        self.kittens.save_image()
        self.kittens.delete_image()
        images = Image.objects.all()   
        self.assertTrue(len(images) == 0) 

    # retrieve all images
    def test_can_retrieve_all_images(self):
    '''
    This is to test if one can retrieve all images.
    '''    
        self.kittens.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 1) 

    # test update method
    def test_can_update_images(self):
    '''
    This is to test if one can update images.
    '''    
        self.kittens.save_image()
        cat = Image.objects.filter(image_name='Amber').update(image_name= 'AMBER')
        fetch_cat = Image.objects.get(image_name='Amber')
        self.assertEqual(fetch_cat.image_name,'AMBER')
       

class LocationTestClass(TestCase):
    def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
        self.nairobi = Location(name = 'Nairobi')
       
    def test_save_method(self):
    '''
    Save method to save locations.
    '''    
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    #delete method
    def delete_location_method(self):
    '''
    Delete method to delete locations.
    '''    
        self.nairobi.save_location()
        self.nairobi.delete_location()
        locations = Location.objects.all()   
        self.assertTrue(len(locations) == 0)     

class CategoryTestClass(TestCase):
    def setUp(self):
    '''
    Set up method to run before each test cases.
    '''    
       self.cats = Category(name='cats')

    #save method
    def test_save_method(self):
    '''
    Save method to save all categories.
    '''    
        self.flowers.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)

    #delete method
    def test_delete_method(self):
    '''
    Delete method to delete categories.
    '''    
        self.cats.save_category()
        self.cats.delete_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) == 0)     

    