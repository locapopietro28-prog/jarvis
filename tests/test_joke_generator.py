"""
Test per il generatore di barzellette
"""

import pytest
from features.joke_generator import JokeGenerator


class TestJokeGenerator:
    """Test del generatore di barzellette"""
    
    def setup_method(self):
        """Setup prima di ogni test"""
        self.joke_generator = JokeGenerator()
    
    def test_get_random_joke_general(self):
        """Test di ottenere una barzelletta generale"""
        joke = self.joke_generator.get_random_joke("general")
        assert joke is not None
        assert isinstance(joke, str)
        assert len(joke) > 0
    
    def test_get_random_joke_geek(self):
        """Test di ottenere una barzelletta informatica"""
        joke = self.joke_generator.get_random_joke("geek")
        assert joke is not None
        assert isinstance(joke, str)
        assert len(joke) > 0
    
    def test_get_random_joke_official(self):
        """Test di ottenere una barzelletta ufficiale"""
        joke = self.joke_generator.get_random_joke("official")
        assert joke is not None
        assert isinstance(joke, str)
        assert len(joke) > 0
    
    def test_get_multiple_jokes(self):
        """Test di ottenere multiple barzellette"""
        jokes = self.joke_generator.get_multiple_jokes(count=2, api_type="general")
        assert jokes is not None
        assert isinstance(jokes, str)
        assert len(jokes) > 0
    
    def test_joke_format_contains_emoji(self):
        """Test che la barzelletta contenga emoji"""
        joke = self.joke_generator.get_random_joke("general")
        assert joke is not None
        assert "😂" in joke or "📝" in joke or "😄" in joke
