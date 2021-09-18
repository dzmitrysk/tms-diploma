from django.contrib.auth.models import User

superuser = User.objects.create_superuser(username='admin',
                                          password='123123abc')

if superuser:
    print(f"Superuser '{superuser.username}' created")
else:
    print('NOT CREATED superuser')