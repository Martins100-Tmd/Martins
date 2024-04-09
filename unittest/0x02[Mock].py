from unittest.mock import Mock, MagicMock, patch
import unittest
import utils


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


mock_object = MagicMock(return_value="Mocked Result")


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

    @patch("utils.func.sum", mock_object)
    def test_seven(self):
        """Test seven"""
        result = utils.func.sum(3, 2)
        self.assertEqual(result, "Mocked Result")

    @patch("utils.func.sum")
    def test_eight(self, mock_object):
        """Test Eight"""
        mock_object.return_value = 10
        result = utils.func.sum(4, 1)
        mock_object.assert_called()
        mock_object.assert_called_with(4, 1)
        self.assertEqual(result, 10)

    def test_Nine(self):
        with patch("utils.func.sum") as mock_func:
            mock_func.return_value = 200
            result = utils.func.sum("My name is ", "Martins")
            assert mock_func.call_count == 1
            mock_func.assert_called()
            mock_func.assert_called_once()
            mock_func.assert_called_once_with("My name is ", "Martins")
            mock_func.assert_called_with("My name is ", "Martins")
            self.assertEqual(result, 200)
            mock_func.reset_mock()
            mock_func.assert_not_called()
        mock_func.reset_mock()


if __name__ == "__main__":
    unittest.main()
