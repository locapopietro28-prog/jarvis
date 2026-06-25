"""
Test per il modulo mappa del mondo
"""

import pytest
from features.world_map import WorldMap


class TestWorldMap:
    """Test della mappa del mondo"""
    
    def setup_method(self):
        """Setup prima di ogni test"""
        self.world_map = WorldMap()
    
    def test_countries_data_loaded(self):
        """Test che i dati dei paesi siano caricati"""
        countries = self.world_map.get_countries_list()
        assert len(countries) > 0
    
    def test_get_country_info_italia(self):
        """Test di ottenere informazioni sull'Italia"""
        info = self.world_map.get_country_info("Italia")
        assert info is not None
        assert "Roma" in info
        assert "Europa" in info
    
    def test_get_country_info_nonexistent(self):
        """Test di ottenere informazioni per un paese inesistente"""
        info = self.world_map.get_country_info("PaeseFantasma")
        assert info is None
    
    def test_countries_list_not_empty(self):
        """Test che la lista dei paesi non sia vuota"""
        countries = self.world_map.get_countries_list()
        assert len(countries) > 0
        assert "italia" in countries