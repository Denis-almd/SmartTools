import streamlit as st
from project.tools.base_tool import BaseTool

class Password_generator(BaseTool):
    
    def get_name(self):
        return "Password Generator"
    
    def get_icon(self):
        return "🔐"
    
    def get_description(self):
        return "Generate strong passwords with customizable options."
    
    def render(self):
        with st.container():
            st.header("Password Generator")
            length = st.slider("Password Length", min_value=8, max_value=64, value=12)
            uppercase = st.checkbox("Include Uppercase Letters")
            lowercase = st.checkbox("Include Lowercase Letters")
            numbers = st.checkbox("Include Numbers")
            symbols = st.checkbox("Include Symbols")
            
            if st.button("Generate Password"):
                password = self._generate_password(length, uppercase, lowercase, numbers, symbols)
                if password:
                    #st.success(f"Generated Password: {password}")
                    st.code(password, language="text")
            
    def _generate_password(self, length, uppercase, lowercase, numbers, symbols):
        import random
        import string
        
        # conservative set of symbols commonly accepted by sites
        accepted_symbols = "!@#$%&*()-_+=[]{}<>?.,;:/^"

        base_password = ""
        if uppercase:
            base_password += random.choice(string.ascii_uppercase)
        if lowercase:
            base_password += random.choice(string.ascii_lowercase)
        if numbers:
            base_password += random.choice(string.digits)
        if symbols:
            base_password += random.choice(accepted_symbols)
        
        char_pool = ""
        if uppercase:
            char_pool += string.ascii_uppercase
        if lowercase:
            char_pool += string.ascii_lowercase
        if numbers:
            char_pool += string.digits
        if symbols:
            char_pool += accepted_symbols
            
        if not char_pool:
            st.error("Please select at least one character type!")
            return ""
        
        password = ''.join(list(base_password) + [random.choice(char_pool) for _ in range(length - len(base_password))])
        password = list(password)
        random.shuffle(password)
        return ''.join(password)
        
        
        