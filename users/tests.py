from django.test import TestCase

# Create your tests here.

class UsuarioTestCase(TestCase):

    def setUp(self):
        self.usuario1 = 'João Pedro'
        self.usuario2 = 'João Arthur'
        


    def test_usuarios_nomes_iguais(self):
        self.assertEqual(self.usuario1, self.usuario2) #Testa se dois valores são iguais
