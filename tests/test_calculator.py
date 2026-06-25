"""
Test per il modulo calcolatrice
"""

import pytest
from features.calculator import Calculator


class TestCalculator:
    """Test della calcolatrice"""
    
    def setup_method(self):
        """Setup prima di ogni test"""
        self.calculator = Calculator()
    
    def test_simple_addition(self):
        """Test di semplice addizione"""
        result = self.calculator.calculate("2 + 2")
        assert result == 4
    
    def test_simple_subtraction(self):
        """Test di semplice sottrazione"""
        result = self.calculator.calculate("5 - 3")
        assert result == 2
    
    def test_multiplication(self):
        """Test di moltiplicazione"""
        result = self.calculator.calculate("3 * 4")
        assert result == 12
    
    def test_division(self):
        """Test di divisione"""
        result = self.calculator.calculate("10 / 2")
        assert result == 5
    
    def test_complex_expression(self):
        """Test di espressione complessa"""
        result = self.calculator.calculate("2 + 3 * 4")
        assert result == 14
    
    def test_division_by_zero(self):
        """Test di divisione per zero"""
        with pytest.raises(ValueError):
            self.calculator.calculate("5 / 0")
    
    def test_invalid_expression(self):
        """Test di espressione non valida"""
        with pytest.raises(ValueError):
            self.calculator.calculate("2 ++ 2")