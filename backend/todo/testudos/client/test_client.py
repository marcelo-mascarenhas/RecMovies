import numpy as np
import pytest

from todo.models import Movies, Client
from todo.client_integration.client import ClientManipulator



class TestClientManipulator():

    @pytest.fixture
    def setUp(self, mocker):
        self.client_id = 57; self.movie_id = 12;
        
        self.client_manipulator = ClientManipulator()


    def test_fail_buy_movie_when_is_available_but_client_does_not_have_money(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = [Client(client_id=self.client_id, name='Jack Tequila', money=25.55)];

        mock_first_movies = mocker.patch("todo.models.Movies.objects.filter")
        mock_first_movies.return_value =  [Movies(id=self.movie_id, title="Chihiro", language='jp',
                                                                        genres='Anime',     
                                                                        available_copies=100,
                                                                        price=39.99)]

        result = self.client_manipulator.buy_movie(self.client_id, self.movie_id)

        assert result == -1
    
    
    def test_fail_to_buy_movie_because_it_is_not_available(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = [Client(client_id=self.client_id, name='Jack Tequila', money=40.00)];

        mock_first_movies = mocker.patch("todo.models.Movies.objects.filter")
        mock_first_movies.return_value =  [Movies(id=self.movie_id, title="Chihiro", language='jp',
                                                                        genres='Anime',     
                                                                        available_copies=0,
                                                                        price=39.99)]

        result = self.client_manipulator.buy_movie(self.client_id, self.movie_id)

        assert result == -2


    def test_success_buy_from_client(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = [Client(client_id=self.client_id, name='Jack Tequila', money=40.00)];

        mock_first_movies = mocker.patch("todo.models.Movies.objects.filter")
        mock_first_movies.return_value =  [Movies(id=self.movie_id, title="Chihiro", language='jp',
                                                                        genres='Anime',     
                                                                        available_copies=10,
                                                                        price=39.99)]
        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)
                                                
        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.create_movie_client_interaction",
                                                return_value=0)

        result = self.client_manipulator.buy_movie(self.client_id, self.movie_id)

        assert result == 0
    
    
    def test_when_client_does_not_have_money_neither_the_movie_is_available(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = [Client(client_id=self.client_id, name='Prado Magalhães', money=15.00)];

        mock_first_movies = mocker.patch("todo.models.Movies.objects.filter")
        mock_first_movies.return_value =  [Movies(id=self.movie_id, title="Chihiro", language='jp',
                                                                        genres='Anime',     
                                                                        available_copies=0,
                                                                        price=39.99)]
    

        result = self.client_manipulator.buy_movie(self.client_id, self.movie_id)

        assert result == -2


    def test_fail_buy_movie_because_movie_id_does_not_exist(self, setUp, mocker):
        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = [Client(client_id=self.client_id, name='Jack Tequila', money=40.00)];
        
        mock_first_movies = mocker.patch("todo.models.Movies.objects.filter")
        mock_first_movies.return_value =  []

        result = self.client_manipulator.buy_movie(self.client_id, self.movie_id)

        assert result == -3


    def test_fail_buy_movie_because_client_id_does_not_exist(self, setUp, mocker):
        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = [];

        mock_first_movies = mocker.patch("todo.models.Movies.objects.filter")
        mock_first_movies.return_value =  [Movies(id=self.movie_id, title="Chihiro", language='jp',
                                                                        genres='Anime',     
                                                                        available_copies=0,
                                                                        price=39.99)]

        result = self.client_manipulator.buy_movie(self.client_id, self.movie_id)

        assert result == -4
    

    def test_client_add_money_to_wallet(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = [Client(client_id=self.client_id, name='Jack Tequila', money=10.00)]

        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.add_money(self.client_id, 10.00)

        assert result == 20.00


    def test_client_try_to_add_string_as_money_to_wallet(self, setUp, mocker):
        
        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = [Client(client_id=self.client_id, name='Jaqueline Margarita', money=10.00)]
        
        result = self.client_manipulator.add_money(self.client_id, "Dez Reais")
        
        assert result == -1

    def test_set_new_address_success(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = [Client(client_id=self.client_id, name='Jaqueline Margarita', money=10.00)]
        
        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.set_new_address(self.client_id, 'Endereço da casa')

        assert result == 0
    

    def test_fail_set_new_address_argument_not_string(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = [Client(client_id=self.client_id, name='Jaqueline Margarita', money=10.00)]
        
        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.set_new_address(self.client_id, None)

        assert result == -1

    def test_fail_set_new_address_client_not_found(self, setUp, mocker):

        mock_client = mocker.patch("todo.models.Client.objects.filter")
        mock_client.return_value = []
        
        mock_saving_in_database = mocker.patch("todo.client_integration.client.ClientManipulator.save_object_in_database",
                                                return_value=0)

        result = self.client_manipulator.set_new_address(self.client_id, 'Endereçudo')

        assert result == -1


    # def test_client_passing_none_address(self):
    #     pass


    # def test_client_passing_null_email(self):
    #     pass


    # def test_client_insert_wrong_password_exception(self):
    #     pass






 
    

