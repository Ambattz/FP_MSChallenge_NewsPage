from bs4 import BeautifulSoup
import pytest
import pickle
import requests

class TestWebpage:
    @pytest.fixture(autouse=True)
    def get_soup(self):
        index_page = requests.get("http://localhost:8000/index.html")
        soup_index = BeautifulSoup(index_page.content, 'html.parser')
        self._index = soup_index

        crime_page = requests.get("http://localhost:8000/crime.html")
        soup_crime = BeautifulSoup(crime_page.content, 'html.parser')
        self._crime = soup_crime

        recentnews_page = requests.get("http://localhost:8000/recentnews.html")
        soup_recentnews = BeautifulSoup(recentnews_page.content, 'html.parser')
        self._recentnews = soup_recentnews

        weather_page = requests.get("http://localhost:8000/weather.html")
        soup_weather = BeautifulSoup(weather_page.content, 'html.parser')
        self._weather = soup_weather


    # testing index.html
    def test_indexpage(self):
        site=self._index.find('header')
        assert site.find('img', {'src': 'image/mike.png'})
        assert site.find('h1').text == 'The News'
        
        site=self._index.find('div', {'class':'topnav'})
        assert site.find('a', {'class': 'active'}, {'href': 'index.html'})
        assert 4 == len(site.find_all('a'))

        site=self._index.find('footer')
        assert site.find('p').text == 'Copyright 2019 News'

        site=self._index.find('div', {'class': 'row'})
        a=0
        for border in site.find_all('div', {'class': 'border'}):
            assert border.find_all('b')
            category=border.find('div', {'class': 'category'})
            if category.find('a', {'href': 'crime.html'}):
                assert category.find('img', {'src': 'image/criminal.png'})
                a+=1;
            elif category.find('a', {'href': 'recentnews.html'}):
                assert category.find('img', {'src': 'image/news.png'})
                a+=1;
            elif category.find('a', {'href': 'weather.html'}):
                assert category.find('img', {'src': 'image/half_sunny.png'})
                a+=1;
        assert a ==3

# ------------------------------------------------------------------------------------------------------------------------------


    # testing crime.html
    def test_crimepage(self):
        site=self._crime.find('header')
        assert site.find('img', {'src': 'image/mike.png'})
        assert site.find('h1').text == 'The News'
        
        site=self._crime.find('div', {'class':'topnav'})
        assert site.find('a', {'href': 'index.html'})
        assert 4 == len(site.find_all('a'))

        site=self._crime.find('footer')
        assert site.find('p').text == 'Copyright 2019 News'

        site=self._crime.find('div', {'class': 'row'})
        assert site.find('img', {'src': 'image/fight.png'})
        assert 2 == len(site.find_all('ul'))
        for ul in site.find_all('ul'):
            assert 4 == len(ul.find_all('li'))
            for li in ul.find_all('li'):
                assert li.find('b')
                assert li.find('a')
                assert li.find('p', {'class': 'grey'})

# ------------------------------------------------------------------------------------------------------------------------------


    # testing recentnews.html
    def test_recentnewspage(self):
        site=self._recentnews.find('header')
        assert site.find('img', {'src': 'image/mike.png'})
        assert site.find('h1').text == 'The News'
        
        site=self._recentnews.find('div', {'class':'topnav'})
        assert site.find('a', {'href': 'index.html'})
        assert 4 == len(site.find_all('a'))

        site=self._recentnews.find('footer')
        assert site.find('p').text == 'Copyright 2019 News'

        assert 2 == len(self._recentnews.find_all('div', {'class': 'row'}))
        for row in self._recentnews.find_all('div', {'class': 'row'}):
            assert 3 == len(row.find_all('div', {'class': 'card'}))
            for card in row.find_all('div', {'class': 'card'}):
                assert card.find('img')
                assert card.find('b')
                assert card.find('a')
                assert card.find('p', {'class': 'grey'})

# ------------------------------------------------------------------------------------------------------------------------------


    # testing weather.html
    def test_weatherpage(self):
        site=self._weather.find('header')
        assert site.find('img', {'src': 'image/mike.png'})
        assert site.find('h1').text == 'The News'
        
        site=self._weather.find('div', {'class':'topnav'})
        assert site.find('a', {'href': 'index.html'})
        assert 4 == len(site.find_all('a'))

        site=self._weather.find('footer')
        assert site.find('p').text == 'Copyright 2019 News'

        table=self._weather.find('table')
        assert 6 == len(table.find_all('tr'))
        assert 4 == len(table.find_all('th'))
        assert 20 == len(table.find_all('td'))
        assert 5 == len(table.find_all('img'))

