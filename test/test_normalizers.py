import asyncio
import pytest
import pytest_asyncio.plugin
from app import api_fetch


# pytestmark = pytest.mark.asycnio

@pytest.fixture
def github_sample():
    with open('test/github_sample.txt') as file:
        contents = file.read()
    return contents

@pytest.mark.asycnio
async def test_normalize_github(github_sample):
    expected = {
        'source': 'github',
        'category': 'popular',
        'data':[{
            "title":"system-design-primer",
            "link": "https://github.com/donnemartin",
            "desc": "Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.",
            "stars": 72711
        }]
    }

    actual = await api_fetch.normalize_github(github_sample)
    assert actual == expected