import pytest
import allure

@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.smoke
def test_sub0():
    assert 2 - 2 == 0


@pytest.mark.smoke
def test_sub1():
    assert 3 + 3 == 0


@pytest.mark.smoke
def test_sub2():
    assert 1 - 1 == 0


@pytest.mark.reg
def test_sub3():
    assert 0 - 0 != 0


@pytest.mark.skip(reason="Not completed, Skip it")
def test_sub3():
    assert 0 - 0 != 0
