# This is a Unit Test file that checks that oiur functions work as expected.
# It's a good practice to always ensure that the code output the desired output given sample input.
# Should also be incorporated using Continiuous Integration at the root of the Github Repo.

from package.character import palindrome
import numpy as np
def test_palindrome():

    np.testing.assert_equal(palindrome("aa")==True, True)
