import numpy as np
import pytest

from todo.models import Movies, Client, MovieClient
from todo.client_integration.client import ClientManipulator


@pytest.mark.unit
class TestClientManipulator():

    @pytest.fixture
    def setUp(self, mocker):
        self.client_id = 57; self.movie_id = 12;
        
        self.client_manipulator = ClientManipulator()

    def test_fail_buy_movie_when_is_available_but_client_does_not_have_money(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter",
        return_value = [Client(client_id=self.client_id, name='Jack Tequila', money=25.55)]);

        mock_first_movies = mocker.patch("todo.models.Movies.objects.filter",
        return_value =  [Movies(id=self.movie_id, title="Chihiro", language='jp',
                                                                        genres='Anime',     
                                                                        available_copies=100,
                                                                        price=39.99)])

        result = self.client_manipulator.buy_movie(self.client_id, self.movie_id)

        assert result == -1
    
    
    def test_fail_to_buy_movie_because_it_is_not_available(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter",
        return_value = [Client(client_id=self.client_id, name='Jack Tequila', money=40.00)]);

        mock_first_movies = mocker.patch("todo.models.Movies.objects.filter",
        return_value =  [Movies(id=self.movie_id, title="Chihiro", language='jp',
                                                                        genres='Anime',     
                                                                        available_copies=0,
                                                                        price=39.99)])

        result = self.client_manipulator.buy_movie(self.client_id, self.movie_id)

        assert result == -2


    def test_success_buy_from_client(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter",
        return_value = [Client(client_id=self.client_id, name='Jack Tequila', money=40.00)]);

        mock_first_movies = mocker.patch("todo.models.Movies.objects.filter",
        return_value =  [Movies(id=self.movie_id, title="Chihiro", language='jp',
                                                                        genres='Anime',     
                                                                        available_copies=10,
                                                                        price=39.99)])
        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)
                                                
        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.create_movie_client_interaction",
                                                return_value=0)

        result = self.client_manipulator.buy_movie(self.client_id, self.movie_id)

        assert result == 0
    

    def test_client_wallet_after_purchase(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter",
        return_value = [Client(client_id=self.client_id, name='Jack Tequila', money=40.00)]);

        mock_first_movies = mocker.patch("todo.models.Movies.objects.filter",
        return_value =  [Movies(id=self.movie_id, title="Chihiro", language='jp',
                                                                        genres='Anime',     
                                                                        available_copies=10,
                                                                        price=39.99)])

        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)
                                                
        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.create_movie_client_interaction",
                                                return_value=0)

        result = self.client_manipulator.buy_movie(self.client_id, self.movie_id)

        assert pytest.approx(mock_client.return_value[0].money, rel=1e-3)  == 0.01
    
    def test_buy_movie_when_client_does_not_have_money_neither_the_movie_is_available(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter",
        return_value = [Client(client_id=self.client_id, name='Prado Magalhães', money=15.00)]);

        mock_first_movies = mocker.patch("todo.models.Movies.objects.filter",
        return_value =  [Movies(id=self.movie_id, title="Chihiro", language='jp',
                                                                        genres='Anime',     
                                                                        available_copies=0,
                                                                        price=39.99)])
    

        result = self.client_manipulator.buy_movie(self.client_id, self.movie_id)

        assert result == -2


    def test_fail_buy_movie_because_movie_id_does_not_exist(self, setUp, mocker):
        mock_client = mocker.patch("todo.models.Client.objects.filter",
        return_value = [Client(client_id=self.client_id, name='Jack Tequila', money=40.00)]);
        
        mock_first_movies = mocker.patch("todo.models.Movies.objects.filter",
        return_value =  [])

        result = self.client_manipulator.buy_movie(self.client_id, self.movie_id)

        assert result == -3


    def test_fail_buy_movie_because_client_id_does_not_exist(self, setUp, mocker):
        mock_client = mocker.patch("todo.models.Client.objects.filter", return_value = [])

        mock_first_movies = mocker.patch("todo.models.Movies.objects.filter",
        return_value =  [Movies(id=self.movie_id, title="Chihiro", language='jp',
                                                                        genres='Anime',     
                                                                        available_copies=0,
                                                                        price=39.99)])

        result = self.client_manipulator.buy_movie(self.client_id, self.movie_id)

        assert result == -4
    

    def test_client_add_money_to_wallet(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = [Client(client_id=self.client_id, name='Jack Tequila', money=10.00)]

        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.add_money(self.client_id, 10.00)

        assert result == 20.00
    

    def test_client_try_to_add_negative_money_to_wallet(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = [Client(client_id=self.client_id, name='Jack Tequila', money=10.00)]

        result = self.client_manipulator.add_money(self.client_id, -10.00)

        assert result == -1


    def test_client_try_to_add_string_as_money_to_wallet(self, setUp, mocker):
        
        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = [Client(client_id=self.client_id, name='Jaqueline Margarita', money=10.00)]
        
        result = self.client_manipulator.add_money(self.client_id, "Dez Reais")
        
        assert result == -1


    def test_adjust_new_address_success(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = [Client(client_id=self.client_id, name='Jaqueline Margarita', money=10.00)]
        
        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.adjust_new_address(self.client_id, 'Endereço da casa')

        assert result == 0
    

    def test_fail_adjust_new_address_argument_not_string(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = [Client(client_id=self.client_id, name='Jaqueline Margarita', money=10.00)]
        
        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.adjust_new_address(self.client_id, None)

        assert result == -1


    def test_fail_adjust_new_address_client_not_found(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter", return_value = [])
        
        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.adjust_new_address(self.client_id, 'Endereçudo')

        assert result == -1


    def test_establishing_client_telephone_sucess(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = [Client(client_id=self.client_id, name='Jaqueline Margarita', money=10.00)]
        
        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.establish_telephone(self.client_id, '9937-1235')

        assert result == 0

    def test_fail_to_establish_telephone_client_not_found(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter", return_value = [])
        
        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.establish_telephone(self.client_id, '9957-6535')

        assert result == -1
        
    
    def test_fail_to_establish_telephone_float_type(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter",
        return_value = [Client(client_id=self.client_id, name='Jaqueline Margarita', money=10.00)])
        
        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.establish_telephone(self.client_id, 9.9937-12.35)

        assert result == -1

    def test_fail_to_establish_telephone_none_type(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter",
        return_value = [Client(client_id=self.client_id, name='Jaqueline Margarita', money=10.00)])
        
        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.establish_telephone(self.client_id, None)

        assert result == -1
    
    def test_authenticate_user_with_the_right_password(self, setUp, mocker):
        email = "jackmarga@gmail.com"
        password = "AX852nana5#3#%z"
        
        mock_client = mocker.patch("todo.models.Client.objects.filter", 
        return_value = [Client(client_id=self.client_id, email=email, money=10.00, password='AX852nana5#3#%z')])

        result = self.client_manipulator.authenticate_user_with_password(self.client_id, password, email)

        assert result == True
        
        
    def test_authenticate_user_with_the_wrong_password(self, setUp, mocker):
        email = "rocambolemole@gmail.com"
        password = "AX852nana5#3#%z"
        
        mock_client = mocker.patch("todo.models.Client.objects.filter", 
        return_value = [Client(client_id=self.client_id, email='rocambolemole@gmail.com', money=10.00, password='AX852nana5#3#%z')])

        result = self.client_manipulator.authenticate_user_with_password(self.client_id, "AX852nana5#3#%Z", email)

        assert result == False

    def test_login_with_not_registered_email(self, setUp, mocker):
        email = "rocambolemole@gmail.com"
        password = "AX852nana5#3#%z"
        
        mock_client = mocker.patch("todo.models.Client.objects.filter", 
        return_value = [Client(client_id=self.client_id, email='rocambolemole@gmail.com', money=10.00, password='AX852nana5#3#%z')])

        result = self.client_manipulator.authenticate_user_with_password(self.client_id, "AX852nana5#3#%Z", "rocamboleduro@gmail.com")

        assert result == False
    
    def test_user_change_password_sucess(self, setUp, mocker):
        new_password = "@ztestedesenha1#2345"

        mock_client = mocker.patch("todo.models.Client.objects.filter", 
        return_value = [Client(client_id=self.client_id, money=10.00, password="testudodesenha1#345")])

        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.change_user_password(self.client_id, new_password)

        assert result == "Senha salva com sucesso"
        assert mock_client.return_value[0].password == new_password

    def test_user_change_password_without_special_character(self, setUp, mocker):
        new_password = "testedesenha12345"

        mock_client = mocker.patch("todo.models.Client.objects.filter",
        return_value = [Client(client_id=self.client_id, money=10.00, password="testudodesenha1#345")])

        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.change_user_password(self.client_id, new_password)

        assert result == "A nova senha deve conter caracteres especiais"
    

    def test_user_change_password_without_numbers(self, setUp, mocker):
        new_password = "testedesenha"

        mock_client = mocker.patch("todo.models.Client.objects.filter",
        return_value = [Client(client_id=self.client_id, money=10.00, password="testudodesenha1#345")])

        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.change_user_password(self.client_id, new_password)

        assert result == "A nova senha deve conter numeros"


    def test_user_change_password_without_letters(self, setUp, mocker):
        new_password = "2849083290#29@948"

        mock_client = mocker.patch("todo.models.Client.objects.filter",
        return_value = [Client(client_id=self.client_id, money=10.00, password="testudodesenha1#345")])

        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.change_user_password(self.client_id, new_password)

        assert result == "A nova senha deve conter letras"

    def test_password_without_the_adequate_length(self, setUp, mocker):
        new_password = "1ab#@"

        mock_client = mocker.patch("todo.models.Client.objects.filter",
        return_value = [Client(client_id=self.client_id, money=10.00, password="testudodesenha1#345")])

        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.change_user_password(self.client_id, new_password)

        assert result == "A nova senha deve conter mais de 8 caracteres"

    def test_user_change_password_with_the_same_password(self, setUp, mocker):
        new_password = "testudodesenha1#345"

        mock_client = mocker.patch("todo.models.Client.objects.filter", 
        return_value = [Client(client_id=self.client_id, money=10.00, password="testudodesenha1#345")])

        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.change_user_password(self.client_id, new_password)

        assert result == "A nova senha deve ser diferente da senha antiga"

    def test_set_new_password_for_client(self, setUp, mocker):
        new_password = "#senhaClichezona123#"

        mock_client = mocker.patch("todo.models.Client.objects.filter", 
        return_value = [Client(client_id=self.client_id, money=10.00)])

        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.change_user_password(self.client_id, new_password)

        assert result == "Senha salva com sucesso"
        assert mock_client.return_value[0].password == new_password

    # def test_give_movie_to_client(self, setUp, mocker):

    #     client = Client(client_id=self.client_id, name='Jack Tequila', money=40.00)

    #     movie = Movies(id=self.movie_id, title="Chihiro", language='jp', genres='Anime', available_copies=10, price=39.99)

    #     mock_client_movie = mocker.patch("todo.models.MovieClient.objects", 
    #                                 return_value = [MovieClient(client_id=self.client_id, movie_id=self.movie_id,)])
        

    #     result = self.client_manipulator.create_movie_client_interaction(self.client_id, self.movie_id)

    #     assert result.movie_id == self.movie_id
    #     assert result.client_id == self.client_id
    