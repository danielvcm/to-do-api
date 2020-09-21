from cryptography.fernet import Fernet
import os
class EncriptionService:
    fernet = Fernet(bytes(os.getenv('F_KEY').encode('utf8')))
    @staticmethod
    def encrypt_password(user_request, new_user):
        fernet = EncriptionService.fernet
        new_user.password = fernet.encrypt(user_request.password.encode('utf8'))
    
    @staticmethod
    def decrypt_password(user):
        fernet = EncriptionService.fernet
        user.password = EncriptionService.convert_to_string(user.password)
        real_password = fernet.decrypt(bytes(user.password.encode('utf8')))
        real_password = EncriptionService.convert_to_string(real_password)
        return real_password
    
    @staticmethod
    def convert_to_string(bytes_string):
        return str(bytes_string)[2:-1]
