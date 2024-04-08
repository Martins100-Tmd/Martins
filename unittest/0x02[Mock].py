from unittest.mock import Mock, MagicMock, patch
import unittest
from utils.func import sum


def fetch_some_url(api):
    """
    Given this is an expensive function, one that fetch data from the internet.
    We really don't want to run this everytime our test runs because of our
    resource fetching rate limit, and our server cost for such operation
    """
    return {"name": "Peace"}


def fetch_some_sideEffect(arg):
    if not isinstance(arg, str):
        raise TypeError("api must be string")


def processApiData(data):
    """
    Take this as the function that process the fetched data and do something with it
    """
    return data["name"]


def side_effect_simulation(arg):
    if arg == "foo":
        return "bar"
    else:
        return "baz"


def test_Two_randomFn(prop):
    return prop * 2


def externalAPI(url):
    return {"msg": "success"}


def externalApiSideEffect(num):
    if num > 10:
        return {"msg": "List capacity exceeded"}
    else:
        return {"msg": "No {} passed".format(num)}


print(fetch_some_url("url"))


class MOONTEST(unittest.TestCase):
    def test_One(self):
        """
        in this, we are using MagicMock to mock the function fetch_some_url
        which in turn, saves us the time, cost, and even unpredictable behaviors
        """
        fetch_some_url = MagicMock(return_value={"name": "Martins"})
        self.assertEqual(processApiData(fetch_some_url("url")), "Martins")

    def test_Two(self):
        """
        Using MagicMock side_effect
        """
        test_Two_randomFn = MagicMock(side_effect=side_effect_simulation)
        self.assertEqual(test_Two_randomFn("Hi"), "baz")

    def test_Three(self):
        """
        Testing for the TypeError
        """
        fetch_some_url = MagicMock(side_effect=fetch_some_sideEffect)
        self.assertRaises(TypeError, fetch_some_url, 10)

    def test_Four(self):
        """
        side_effect can be iterable. I.e it return each element in the iterable
        on each call of the function.
        And it give an error if there are no more element to print
        """
        test_Two_randomFn = MagicMock(side_effect=[1, 2, 3])
        self.assertEqual(test_Two_randomFn(100), 1)
        self.assertEqual(test_Two_randomFn(100), 2)
        self.assertEqual(test_Two_randomFn(100), 3)

    def test_Five(self):
        """ """
        externalAPI = MagicMock(side_effect=externalApiSideEffect)
        self.assertEqual(externalAPI(10), {"msg": "No 10 passed"})
        self.assertEqual(externalAPI(7), {"msg": "No 7 passed"})
        self.assertEqual(externalAPI(12), {"msg": "List capacity exceeded"})

    @patch("utils.func.sum")
    def test_seven(self, mock_obj):
        """Test seven"""
        mock_obj.return_value = "Mocked Result"
        result = sum(2, 3)
        self.assertEqual(result, "Mocked Result")


if __name__ == "__main__":
    unittest.main()
