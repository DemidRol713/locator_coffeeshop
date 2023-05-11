from rest_framework import serializers

from user.models import Profile


class UserRegistrationSerializers(serializers.ModelSerializer):

    password2 = serializers.CharField(label='Repeat password', max_length=20)

    class Meta():
        model = Profile
        fields = ['first_name', 'last_name', 'username', 'password', 'password2', 'email', 'date_of_birth']

    def save(self, **kwargs):
        if Profile.objects.filter(username=self.validated_data.get('username')).exists():
            raise serializers.ValidationError({'username': "Этот логин уже зарегистрирован"})

        if Profile.manager.filter(email=self.validated_data.get('email')).exists():
            raise serializers.ValidationError({'email': "Эта почта уже зарегистрирована"})

        user = Profile(username=self.validated_data['username'], email=self.validated_data['email'])
        # Проверяем на валидность пароль
        password = self.validated_data['password']
        # Проверяем на валидность повторный пароль
        password2 = self.validated_data['password2']
        # Проверяем совпадают ли пароли
        if password != password2:
            # Если нет, то выводим ошибку
            raise serializers.ValidationError({'password': "Пароли не совпадает"})
        # Сохраняем пароль
        user.set_password(password)
        # Сохраняем пользователя
        user.save()
        # Возвращаем нового пользователя
        return user

        
class UserChengeSerializers(serializers.ModelSerializer):

    class Meta():
        model = Profile
        fields = []


class UserLoginSerializers(serializers.ModelSerializer):

    class Meta():
        model = Profile
        fields = ['username', 'password']