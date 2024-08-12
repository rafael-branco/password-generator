from time import sleep
import re
import pytest
import playwright
from playwright.sync_api import Page, expect
from models.password_generator_page import PasswordGeneratorPage


def test_generate_password_button(page: Page):
    
    password_generator = PasswordGeneratorPage(page)
    password_generator.goto()
    password_generator.generate_password_button.click()
    
    assert password_generator.get_password() != ""
    

@pytest.mark.parametrize("length", [10, 16, 24, 28, 50])
def test_password_length(page: Page, length: int):
    password_generator = PasswordGeneratorPage(page)
    password_generator.goto()
    password_generator.password_length_input.fill(str(length))
    
    assert len(password_generator.get_password()) == length


def test_numbers_only_password(page: Page):
    
    password_generator = PasswordGeneratorPage(page)
    password_generator.goto()
    
    password_generator.deactivate_character_inclusion('uppercase')
    password_generator.deactivate_character_inclusion('lowercase')
    
    password = password_generator.get_password()
    
    assert re.fullmatch(r'[0-9]+', password), "Password contains non-digit characters"


def test_uppercase_only_password(page: Page):
    
    password_generator = PasswordGeneratorPage(page)
    password_generator.goto()
    
    password_generator.deactivate_character_inclusion('numbers')
    password_generator.deactivate_character_inclusion('lowercase')
    
    password = password_generator.get_password()
    
    assert re.fullmatch(r'[A-Z]+', password), "Password contains non-uppercase characters"
    

def test_lowercase_only_password(page: Page):
    
    password_generator = PasswordGeneratorPage(page)
    password_generator.goto()
    
    password_generator.deactivate_character_inclusion('numbers')
    password_generator.deactivate_character_inclusion('uppercase')
    
    password = password_generator.get_password()
    
    assert re.fullmatch(r'[a-z]+', password), "Password contains non-lowercase characters"    


def test_symbols_only_password(page: Page):
    
    password_generator = PasswordGeneratorPage(page)
    password_generator.goto()
    
    password_generator.activate_character_inclusion('symbols')
    password_generator.deactivate_character_inclusion('numbers')
    password_generator.deactivate_character_inclusion('uppercase')
    password_generator.deactivate_character_inclusion('lowercase')
    
    password = password_generator.get_password()
    
    assert re.fullmatch(r'[!@#$%^&*()\-_=\+\[\]{}|;:,.<>?/`~]+', password), "Password contains non-symbols characters"
    

@pytest.mark.parametrize("symbols,numbers,uppercase,lowercase,regex", [
    (True, False, False, False, r'[!@#$%^&*()\-_=\+\[\]{}|;:,.<>?/`~]+'),
    (False, True, False, False, r'[0-9]+'),
    (False, False, True, False, r'[A-Z]+'),
    (False, False, False, True, r'[a-z]+'),
    (True, True, False, False, r'[!@#$%^&*()\-_=\+\[\]{}|;:,.<>?/`~0-9]+'),
    (True, False, True, False, r'[!@#$%^&*()\-_=\+\[\]{}|;:,.<>?/`~A-Z]+'),
    (True, False, False, True, r'[!@#$%^&*()\-_=\+\[\]{}|;:,.<>?/`~a-z]+'),
    (False, True, True, False, r'[0-9A-Z]+'),
    (False, True, False, True, r'[0-9a-z]+'), 
    (False, False, True, True, r'[A-Za-z]+'), 
    (True, True, True, False, r'[!@#$%^&*()\-_=\+\[\]{}|;:,.<>?/`~0-9A-Z]+'),
    (True, True, False, True, r'[!@#$%^&*()\-_=\+\[\]{}|;:,.<>?/`~0-9a-z]+'),
    (True, False, True, True, r'[!@#$%^&*()\-_=\+\[\]{}|;:,.<>?/`~A-Za-z]+'),
    (True, True, True, True, r'[!@#$%^&*()\-_=\+\[\]{}|;:,.<>?/`~0-9A-Za-z]+')
])
def test_mixed_character_inclusion(page: Page, symbols, numbers, uppercase, lowercase, regex):
    password_generator = PasswordGeneratorPage(page)
    password_generator.goto()

    if symbols:
        password_generator.activate_character_inclusion('symbols')
    else:
        password_generator.deactivate_character_inclusion('symbols')
    
    if numbers:
        password_generator.activate_character_inclusion('numbers')
    else:
        password_generator.deactivate_character_inclusion('numbers')
    
    if uppercase:
        password_generator.activate_character_inclusion('uppercase')
    else:
        password_generator.deactivate_character_inclusion('uppercase')
    
    if lowercase:
        password_generator.activate_character_inclusion('lowercase')
    else:
        password_generator.deactivate_character_inclusion('lowercase')
    
    password = password_generator.get_password()
    
    assert re.fullmatch(regex, password), f"Password does not match the expected pattern: {regex}"
