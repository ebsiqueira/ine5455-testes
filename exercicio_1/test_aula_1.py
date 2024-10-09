import unittest
from datetime import datetime, timedelta, date, time

class TesteBibliotecaDatetime(unittest.TestCase):   
 
    def test_criacao_tempo(self):
        # Fixture Setup
        # Exercise SUT
        tempo = time(9, 56, 50)
        # Result Verification
        self.assertEqual(tempo.hour, 9)
        self.assertEqual(tempo.minute, 56)
        self.assertEqual(tempo.second, 50)
        # Fixture Teardown

    def test_criacao_data(self):
        # Fixture Setup
        # Exercise SUT
        data = date(2024, 9, 4)
        # Result Verification
        self.assertEqual(data.year, 2024)
        self.assertEqual(data.month, 9)
        self.assertEqual(data.day, 4)
        # Fixture Teardown

    def test_timedelta_adicao(self):
        # Fixture Setup
        data_inicial = date(2024, 9, 4)
        # Exercise SUT
        adicao = data_inicial + timedelta(days=5)
        # Result Verification
        self.assertEqual(adicao, date(2024, 9, 9))
        # Fixture Teardown

    def test_timedelta_subtracao(self):
        # Fixture Setup
        data_inicial = date(2024, 9, 4)
        # Exercise SUT
        subtracao = data_inicial - timedelta(days=4)
        # Result Verification
        self.assertEqual(subtracao, date(2024, 8, 31))
        # Fixture Teardown

    def test_diferenca_entre_datas(self):
        # Fixture Setup
        data_inicial = date(2024, 8, 31)
        data_final = date(2024, 9, 4)
        # Exercise SUT
        diferenca_entre_datas = (data_final - data_inicial)
        # Result Verification
        self.assertEqual(diferenca_entre_datas.days, 4)
        # Fixture Teardown
        
    def test_tempo_maximo(self):
        # Fixture Setup
        tempo = time(23, 59, 59, 999999)
        # Exercise SUT
        tempo_max = time.max
        # Result Verification
        self.assertEqual(tempo_max, tempo)
        # Fixture Teardown
        
    def test_tempo_minimo(self):
        # Fixture Setup
        tempo = time(0, 0, 0, 0)
        # Exercise SUT
        tempo_min = time.min
        # Result Verification
        self.assertEqual(tempo_min, tempo)
        # Fixture Teardown 
        
    def test_data_maxima(self):
        # Fixture Setup
        data = date(9999, 12, 31)
        # Exercise SUT
        data_max = date.max
        # Result Verification
        self.assertEqual(data_max, data)
        # Fixture Teardown  
        
    def test_data_minima(self):
        # Fixture Setup
        data = date(1, 1, 1)
        # Exercise SUT
        data_min = date.min
        # Result Verification
        self.assertEqual(data_min, data)
        # Fixture Teardown
        
    def test_formata_strftime_data(self):
        # Fixture Setup
        data_string = "2024-09-04"
        data = datetime(2024, 9, 4)
        # Exercise SUT
        strf_data = data.strftime("%Y-%m-%d")
        # Result Verification
        self.assertEqual(strf_data, data_string)
        # Fixture Teardown
    
    def test_formata_strftime_tempo(self):
        # Fixture Setup
        tempo_string = "09:42:59"
        tempo = time(9, 42, 59)
        # Exercise SUT
        strf_tempo = tempo.strftime("%H:%M:%S")
        # Result Verification
        self.assertEqual(strf_tempo, tempo_string)
        # Fixture Teardown
        
    def test_dia_da_semana_quarta(self):
        # Fixture Setup
        data = date(2024, 9, 4)
        quarta_feira = 2
        # Exercise SUT
        dia_da_semana = datetime.weekday(data)
        # Result Verification
        self.assertEqual(dia_da_semana, quarta_feira)
        # Fixture Teardown
        
    def test_ano_bissexto_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            date(2023, 2, 29)
        # Result Verification
        # Fixture Teardown

    def test_comparacao_data(self):
        # Fixture Setup
        # Exercise SUT
        eh_maior = date(2024, 9, 4) > date(2023, 9, 4)
        # Result Verification
        self.assertTrue(eh_maior)
        # Fixture Teardown

    def test_comparacao_tempo(self):
        # Fixture Setup
        # Exercise SUT
        eh_menor = time(10, 00, 1) > time(10, 00, 00)
        # Result Verification
        self.assertTrue(eh_menor)
        # Fixture Teardown
        
    def test_substituicao_data(self):
        # Fixture Setup
        data = date(2024, 9, 4)
        # Exercise SUT
        nova_data = data.replace(year=2025)
        # Result Verification
        self.assertEqual(nova_data, date(2025, 9, 4))
        # Fixture Teardown

    def test_substituicao_tempo(self):
        # Fixture Setup
        tempo = time(10, 00, 45)
        # Exercise SUT
        novo_tempo = tempo.replace(minute=15)
        # Result Verification
        self.assertEqual(novo_tempo, time(10, 15, 45))
        # Fixture Teardown
        
    def test_combinacao(self):
        # Fixture Setup
        data = date(2024, 9, 4)
        hora = time(10, 00)
        # Exercise SUT
        data_hora = datetime.combine(data, hora)
        # Result Verification
        self.assertEqual(data_hora, datetime(2024, 9, 4, 10, 00))
        # Fixture Teardown

    def test_strptime_parse_data_completa(self):
        # Fixture Setup
        # Exercise SUT
        data = datetime.strptime("2024-09-04", "%Y-%m-%d")
        # Result Verification
        self.assertEqual(data, datetime(2024, 9, 4))
        # Fixture Teardown

    def test_strptime_tempo(self):
        # Fixture Setup
        # Exercise SUT
        tempo = datetime.strptime("10:00", "%H:%M").time()
        # Result Verification
        self.assertEqual(tempo, time(10, 00))
        # Fixture Teardown
        
    def test_timestamp_negativo(self):
        # Fixture Setup
        # Exercise SUT
        data = date.fromtimestamp(-1)
        # Result Verification
        self.assertEqual(data, date(1969, 12, 31))
        # Fixture Teardown
        
    def test_timestamp(self):
        # Fixture Setup
        # Exercise SUT
        data = date.fromtimestamp(1725455932)
        # Result Verification
        self.assertEqual(data, date(2024, 9, 4))
        # Fixture Teardown
        
    def test_dia_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            date(2024, 9, -4)
        # Result Verification
        # Fixture Teardown
        
    def test_mes_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            date(2024, -9, 4)
        # Result Verification
        # Fixture Teardown
        
    def test_ano_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            date(-2024, 9, 4)
        # Result Verification
        # Fixture Teardown

if __name__ == '__main__':
    unittest.main()
