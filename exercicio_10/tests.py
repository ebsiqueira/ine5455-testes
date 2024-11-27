import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TesteCalculadora(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.driver = webdriver.Chrome()
        self.driver.get('https://duckduckgo.com')
        barra_de_busca = self.driver.find_element(By.ID, 'searchbox_input')
        barra_de_busca.send_keys('calculadora')
        botao_de_pesquisa = self.driver.find_element(By.CSS_SELECTOR, '.searchbox_searchButton__F5Bwq')
        botao_de_pesquisa.click()
    
    def soma_calculadora(self, numero_1, numero_2):
        for digito in str(numero_1):
            self.driver.find_element(By.XPATH, f"//button[text() = '{digito}']").click()
        self.driver.find_element(By.XPATH, f"//button[text() = '{'+'}']").click()
        for digito in str(numero_2):
            self.driver.find_element(By.XPATH, f"//button[text() = '{digito}']").click()
        self.driver.find_element(By.XPATH, f"//button[text() = '{'='}']").click()
        return int(self.driver.find_element(By.ID, 'display').text)
         
    def multiplicacao_calculadora(self, numero_1, numero_2):
        for digito in str(numero_1):
            self.driver.find_element(By.XPATH, f"//button[text() = '{digito}']").click()
        self.driver.find_element(By.XPATH, f"//button[text() = '{'×'}']").click()
        for digito in str(numero_2):
            self.driver.find_element(By.XPATH, f"//button[text() = '{digito}']").click()
        self.driver.find_element(By.XPATH, f"//button[text() = '{'='}']").click()
        return int(self.driver.find_element(By.ID, 'display').text)   
        
    def divisao_calculadora(self, numero_1, numero_2):
        for digito in str(numero_1):
            self.driver.find_element(By.XPATH, f"//button[text() = '{digito}']").click()
        self.driver.find_element(By.XPATH, f"//button[text() = '{'÷'}']").click()
        for digito in str(numero_2):
            self.driver.find_element(By.XPATH, f"//button[text() = '{digito}']").click()
        for digito in str(numero_1):
            self.driver.find_element(By.XPATH, f"//button[text() = '{'='}']").click()
        return int(self.driver.find_element(By.ID, 'display').text)  
    
    def get_historico_calculadora(self):
        resultados = self.driver.find_elements(By.CSS_SELECTOR, '.tile__past-result')
        historico = []
        for item in resultados:
            historico.append(int(item.text))
            
        historico.reverse()
        return historico
        
    def test_soma_dois_numeros(self):
        numero_dez = 10
        numero_trinta = 30
        self.assertEqual(numero_dez+numero_trinta, self.soma_calculadora(numero_dez, numero_trinta))
        
    def test_soma_dois_numeros_e_divide_por_dez(self):
        numero_dez = 10
        numero_trinta = 30
        self.assertEqual((numero_dez+numero_trinta)/10, self.divisao_calculadora(self.soma_calculadora(numero_dez, numero_trinta), 10))
        
    def test_duas_operacoes_e_verifica_o_resultado_da_ultima(self):
        self.multiplicacao_calculadora(10, 30)
        numero_dez = 10
        numero_trinta = 30
        self.assertEqual(numero_dez+numero_trinta, self.soma_calculadora(numero_dez, numero_trinta))
    
    def test_tres_operacoes_e_verifica_o_historico(self):
        operacoes = [self.soma_calculadora(10, 130), self.divisao_calculadora(30, 10), self.multiplicacao_calculadora(10, 30)]
        self.assertEqual(operacoes, self.get_historico_calculadora())
        
    def tearDown(self) -> None:
        super().tearDown()
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()