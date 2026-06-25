"""
Test per il processore di comandi
"""

import pytest
from core.command_processor import CommandProcessor


class TestCommandProcessor:
    """Test del processore di comandi"""
    
    def setup_method(self):
        """Setup prima di ogni test"""
        self.processor = CommandProcessor()
    
    def test_calculate_command(self):
        """Test del comando calcola"""
        response = self.processor.process("calcola 2 + 2")
        assert "4" in response
        assert "✅" in response
    
    def test_help_command(self):
        """Test del comando aiuto"""
        response = self.processor.process("aiuto")
        assert "aiuto" in response.lower() or "comandi" in response.lower()
    
    def test_unknown_command(self):
        """Test di comando sconosciuto"""
        response = self.processor.process("comandosconosciuto")
        assert "non riconosciuto" in response.lower() or "❌" in response
    
    def test_empty_command(self):
        """Test di comando vuoto"""
        response = self.processor.process("")
        assert response  # Deve restituire qualcosa