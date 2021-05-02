import pytest

from apod import utility

def test_get_thumbs():
    data_no_url = ""
    assert utility._get_thumbs(data_no_url) == ""

    data_no_id = "https://www.youtube.com/"
    assert utility._get_thumbs(data_no_id) == ""

    data_youtube = "https://www.youtube.com/watch?v=yCJWsIpZDkU"
    assert utility._get_thumbs(data_youtube) == "https://img.youtube.com/vi/yCJWsIpZDkU/0.jpg"

    data_vimeo = "https://vimeo.com/542174820"
    assert utility._get_thumbs(data_vimeo) == "https://i.vimeocdn.com/video/1124434005_640.jpg"
