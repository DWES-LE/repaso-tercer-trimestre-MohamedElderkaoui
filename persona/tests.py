from django.test import TestCase

# Create your tests here.
"""
class Persona(Page):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=100)
    biografia = RichTextField()
    foto = models.ImageField(upload_to="persona")
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    body = RichTextField(blank=True)
    into = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    
    
    search_fields = Page.search_fields + [
        index.SearchField("nombre"),
        index.SearchField("apellidos"),
        index.SearchField("fecha_nacimiento"),
        index.SearchField("lugar_nacimiento"),
        index.SearchField("biografia"),
        index.SearchField("twitter"),
        index.SearchField("facebook"),
        index.SearchField("instagram"),
        index.SearchField("linkedin"),
    ]
    
    content_panels = Page.content_panels + [
        FieldPanel("nombre"),
        FieldPanel("apellidos"),
        FieldPanel("fecha_nacimiento"),
        FieldPanel("lugar_nacimiento"),
        FieldPanel("biografia"),
        FieldPanel("foto"),
        FieldPanel("twitter"),
        FieldPanel("facebook"),
        FieldPanel("instagram"),
        FieldPanel("linkedin"),
    ]
    
    promote_panels = Page.promote_panels + [
        FieldPanel("body"),
        FieldPanel("into"),
    ]
    """
from django.test import TestCase
from .models import Persona
from django.utils import timezone   

class PersonaModelTest(TestCase):
    
    def test_nombre_apellidos(self):
        persona = Persona()
        persona.nombre = "Rafael"
        persona.apellidos = "López"
        self.assertEqual(persona.nombre + " " + persona.apellidos, str(persona))
        
    def test_fecha_nacimiento(self):
        persona = Persona()
        persona.fecha_nacimiento = timezone.now()
        self.assertEqual(persona.fecha_nacimiento, timezone.now())
        
    def test_lugar_nacimiento(self):
        persona = Persona()
        persona.lugar_nacimiento = "Lorca"
        self.assertEqual(persona.lugar_nacimiento, "Lorca")
        
    def test_biografia(self):
        persona = Persona()
        persona.biografia = "Nacido en Lorca"
        self.assertEqual(persona.biografia, "Nacido en Lorca")
        
    def test_twitter(self):
        persona = Persona()
        persona.twitter = "https://twitter.com/rafael_lopez"
        self.assertEqual(persona.twitter, "https://twitter.com/rafael_lopez")
        
    def test_facebook(self):
        persona = Persona()
        persona.facebook = "https://www.facebook.com/rafael.lopez.735944"
        self.assertEqual(persona.facebook, "https://www.facebook.com/rafael.lopez.735944")
        
    def test_instagram(self):
        persona = Persona()
        persona.instagram = "https://www.instagram.com/rafaellopez_/"
        self.assertEqual(persona.instagram, "https://www.instagram.com/rafaellopez_/")
        
    def test_linkedin(self):
        persona = Persona()
        persona.linkedin = "https://www.linkedin.com/in/rafael-l%C3%B3pez-2b0a8a1b/"
        self.assertEqual(persona.linkedin, "https://www.linkedin.com/in/rafael-l%C3%B3pez-2b0a8a1b/")
        
    def test_body(self):
        persona = Persona()
        persona.body = "Prueba body"
        self.assertEqual(persona.body, "Prueba body")
        
    def test_into(self):
        persona = Persona()
        persona.into = "Prueba into"
        self.assertEqual(persona.into, "Prueba into")
        
    def test_tags(self):
        persona = Persona()
        persona.tags = "Prueba tags"
        self.assertEqual(persona.tags, "Prueba tags")

        """  
class PersonaIndex(Page):
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
    ]
    
    subpage_types = ["Persona"]
    
    def personas(self):
        return Persona.objects.live().descendant_of(self)
    
    class Meta:
        verbose_name = "Página de personas"
        verbose_name_plural = "Páginas de personas"
        
    def __str__(self):
        return self.title
        """
from .models import PersonaIndex
from django.test import TestCase
class PersonaIndexModelTest(TestCase):
    
    def test_intro(self):
        persona_index = PersonaIndex()
        persona_index.intro = "Prueba intro"
        self.assertEqual(persona_index.intro, "Prueba intro")
        
    def test_personas(self):
        persona_index = PersonaIndex()
        persona_index.personas = "Prueba personas"
        self.assertEqual(persona_index.personas, "Prueba personas")
        
    def test_verbose_name(self):
        persona_index = PersonaIndex()
        persona_index.verbose_name = "Prueba verbose_name"
        self.assertEqual(persona_index.verbose_name, "Prueba verbose_name")
        
    def test_verbose_name_plural(self):
        persona_index = PersonaIndex()
        persona_index.verbose_name_plural = "Prueba verbose_name_plural"
        self.assertEqual(persona_index.verbose_name_plural, "Prueba verbose_name_plural")
        
    def test_str(self):
        persona_index = PersonaIndex()
        persona_index.str = "Prueba str"
        self.assertEqual(persona_index.str, "Prueba str")


        """
class PersonaCategoria(Page):
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
    ]
    
    subpage_types = ["Persona"]
    
    def personas(self):
        return Persona.objects.live().descendant_of(self)
    
    class Meta:
        verbose_name = "Página de categorias"
        verbose_name_plural = "Páginas de categorias"
        
    def __str__(self):
        return self.title
        """
from .models import PersonaCategoria
from django.test import TestCase
class PersonaCategoriaModelTest(TestCase):
    
    def test_intro(self):
        persona_categoria = PersonaCategoria()
        persona_categoria.intro = "Prueba intro"
        self.assertEqual(persona_categoria.intro, "Prueba intro")
        
    def test_personas(self):
        persona_categoria = PersonaCategoria()
        persona_categoria.personas = "Prueba personas"
        self.assertEqual(persona_categoria.personas, "Prueba personas")
        
    def test_verbose_name(self):
        persona_categoria = PersonaCategoria()
        persona_categoria.verbose_name = "Prueba verbose_name"
        self.assertEqual(persona_categoria.verbose_name, "Prueba verbose_name")
        
    def test_verbose_name_plural(self):
        persona_categoria = PersonaCategoria()
        persona_categoria.verbose_name_plural = "Prueba verbose_name_plural"
        self.assertEqual(persona_categoria.verbose_name_plural, "Prueba verbose_name_plural")
        
    def test_str(self):
        persona_categoria = PersonaCategoria()
        persona_categoria.str = "Prueba str"
        self.assertEqual(persona_categoria.str, "Prueba str")
        """
class PersonaList(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        
    ]
    subpage_types = ['Persona']
    def personas(self):
        return Persona.objects.live().descendant_of(self)
    class Meta:
        verbose_name = "Lista de personas"
        verbose_name_plural = "Listas de personas"
    def __str__(self):
        return self.title
        """
from .models import PersonaList
from django.test import TestCase
class PersonaListModelTest(TestCase):
    
    def test_intro(self):
        persona_list = PersonaList()
        persona_list.intro = "Prueba intro"
        self.assertEqual(persona_list.intro, "Prueba intro")
        
    def test_personas(self):
        persona_list = PersonaList()
        persona_list.personas = "Prueba personas"
        self.assertEqual(persona_list.personas, "Prueba personas")
        
    def test_verbose_name(self):
        persona_list = PersonaList()
        persona_list.verbose_name = "Prueba verbose_name"
        self.assertEqual(persona_list.verbose_name, "Prueba verbose_name")
        
    def test_verbose_name_plural(self):
        persona_list = PersonaList()
        persona_list.verbose_name_plural = "Prueba verbose_name_plural"
        self.assertEqual(persona_list.verbose_name_plural, "Prueba verbose_name_plural")
        
    def test_str(self):
        persona_list = PersonaList()
        persona_list.str = "Prueba str"
        self.assertEqual(persona_list.str, "Prueba str")
        """