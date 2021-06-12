"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from nsfw_dl.bases import BaseSearchXML


class GelbooruRandom:
    """ Gets a random image from gelbooru. """
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """ .... """
        type(args)
        return "https://www.gelbooru.com/index.php?page=post&s=random", {}, {}

    @staticmethod
    def get_image(data):
        """ ... """
        return data.find(id="image").get("src")


class GelbooruSearch(BaseSearchXML):
    """ Gets a random image with a specific tag from gelbooru. """
    data_format = "bs4/xml"

    @staticmethod
    def prepare_url(args):
        """ .... """
        return ("https://www.gelbooru.com/"
                f"index.php?page=dapi&s=post&q=index&{args}", {}, {})
