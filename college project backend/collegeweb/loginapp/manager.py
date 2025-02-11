from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.models import User

class usermanager(BaseUserManager):
    use_in_migrations=True
    def create_user(self,email, password=None,**extra):
        if not email:
            raise ValueError("Email is require")
       
        email=self.normalize_email(email)
        user =self.model(email=email,password=password,**extra)
        user.set_password(password)
        user.save(using=self._db)
        
        return user 
        
            

    def create_superuser(self,email,password=None, **extra):
        extra.setdefault('is_staff',True)
        extra.setdefault('is_superuser',True)
        extra.setdefault('is_active',True)
        return self.create_user(email,password,**extra)