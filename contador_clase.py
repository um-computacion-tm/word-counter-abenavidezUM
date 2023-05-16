import unittest

def contador(sentence):
    
    palabras = sentence.split()
    npalabras = len(palabras)
    return npalabras


class TestWordCounter(unittest.TestCase):
    
    def test_0(self):
        result = contador('')
        self.assertEqual(result, 0)
        
    def test_1(self):
        result = contador('test')
        self.assertEqual(result, 1)
        
    def test_2(self):
        result = contador('segundo test')
        self.assertEqual(result, 2)
        
    def test_3(self):
        result = contador('..test..')
        self.assertEqual(result, 1)
        
    def test_4(self):
        result = contador('..test.. cuatro!')
        self.assertEqual(result, 2)
        
    def test_5(self):
        result = contador('Este es mi ultimo test')
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()