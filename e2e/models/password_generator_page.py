from playwright.sync_api import Page

class PasswordGeneratorPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.password_length_input = self.page.locator("#password-length")
        self.password = self.page.locator("#password")
        self.generate_password_button = self.page.locator(".generate-new-password-box button")
        self.clipboard_button = self.page.locator("#copy-to-clipboard")
        self.uppercase_button = self.page.locator("#character-inclusions-uppercase")
        self.lowercase_button = self.page.locator("#character-inclusions-lowercase")
        self.numbers_button = self.page.locator("#character-inclusions-numbers")
        self.symbols_button = self.page.locator("#character-inclusions-symbols")
        
    def goto(self):
        self.page.goto("http://127.0.0.1:5500/index.html")
    
    def get_password(self):
        return str(self.password.input_value())
    
    
    def activate_character_inclusion(self, button):
        self.change_character_inclusion_status(button, True)
    
    def deactivate_character_inclusion(self, button):
        self.change_character_inclusion_status(button, False)
    
    def change_character_inclusion_status(self, button, desired_status):
        
        button_element = None
        
        if(button == 'uppercase'):
            button_element = self.uppercase_button
            
        elif(button == 'lowercase'):
            button_element = self.lowercase_button
        
        elif(button == 'numbers'):
            button_element = self.numbers_button
            
        elif(button == 'symbols'):
            button_element = self.symbols_button
        else:
            return
        
        if desired_status is True:
            if 'selected' not in button_element.get_attribute('class'):
                button_element.click()
        else:
            if 'selected' in button_element.get_attribute('class'):
                button_element.click()

            
        
        
