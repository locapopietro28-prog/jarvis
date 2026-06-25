"""
Test per il modulo utilities
"""

import pytest
from features.utilities import Utilities


class TestUtilities:
    """Test delle funzionalità utili"""
    
    def setup_method(self):
        """Setup prima di ogni test"""
        self.utilities = Utilities()
    
    def test_get_current_datetime(self):
        """Test del recupero della data/ora"""
        result = self.utilities.get_current_datetime()
        assert "Data" in result or "Ora" in result
    
    def test_calculate_calories_valid(self):
        """Test del calcolo calorie con parametri validi"""
        result = self.utilities.calculate_calories("30 70 M")
        assert "Calorie" in result or "BMR" in result
    
    def test_calculate_calories_invalid(self):
        """Test del calcolo calorie con parametri invalidi"""
        result = self.utilities.calculate_calories("invalid")
        assert "❌" in result
    
    def test_convert_units_km_to_miles(self):
        """Test conversione km a miles"""
        result = self.utilities.convert_units("100 km to miles")
        assert "✅" in result or "62" in result
    
    def test_convert_units_celsius_to_fahrenheit(self):
        """Test conversione Celsius a Fahrenheit"""
        result = self.utilities.convert_units("0 celsius to fahrenheit")
        assert "✅" in result or "32" in result
    
    def test_convert_units_invalid(self):
        """Test conversione invalida"""
        result = self.utilities.convert_units("100 km to xyz")
        assert "❌" in result
