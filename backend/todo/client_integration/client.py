from ..models import Movies
from ..models import Client
from ..models import MovieClient

class ClientManipulator():

    def change_user_password(self, client_id, new_password):
        
        result_query_client = Client.objects.filter(id=client_id)
        if not result_query_client:
            return -1
        
        client_object = result_query_client[0]

        if client_object.password and new_password == client_object.password:
            return "A nova senha deve ser diferente da senha antiga"
        
        if len(new_password) < 8:
            return "A nova senha deve conter mais de 8 caracteres"
        
        if not self.__check_for_number_in_string(new_password):
            return "A nova senha deve conter numeros"

        if not self.__check_letters_in_string(new_password):
            return "A nova senha deve conter letras"
        
        if not self.__detect_special_character_in_string(new_password):
            return "A nova senha deve conter caracteres especiais"

        client_object.password = new_password;  self.save_object_in_database(client_object)
        return "Senha salva com sucesso"



    def add_money(self, client_id, money_to_add):
        #Adiciona dinheiro a carteira do cliente
        result_query_client = Client.objects.filter(id=client_id)

        # if money_to_add not a number
        if not isinstance(money_to_add, int) and not isinstance(money_to_add, float):
                return -1
        
        if money_to_add <= 0:
            return -1
        
        if not result_query_client:
            return -1
        else:
            client_object = result_query_client[0]

            client_object.money = client_object.money + money_to_add
            self.save_object_in_database(client_object)
        
        return client_object.money
    
    def adjust_new_address(self, client_id, new_adress):

        result_query_client = Client.objects.filter(id=client_id)

        if not isinstance(new_adress, str):
            return -1

        if not result_query_client:
            return -1
        else:
            client_object = result_query_client[0]

            client_object.address_line = new_adress
            self.save_object_in_database(client_object)
        
        return 0
    
    def establish_telephone(self, client_id, telephone):
        result_query_client = Client.objects.filter(id=client_id)

        if not isinstance(telephone, str) and not isinstance(telephone, int): 
            return -1

        if not result_query_client:
            return -1
        else:
            client_object = result_query_client[0]

            client_object.telephone = telephone
            self.save_object_in_database(client_object)
        
        return 0

    def buy_movie(self, client_id, movie_id):
        # Checa se o filme tá disponível para compra, se o cliente tem dinheiro
        # tem dinheiro para comprar. Cliente compra com sucesso. Cliente compra sem sucesso.
        ''' 
            return 0 => PERFEITO!
            return -1 => Faltou grana
            return -2 => Filme indisponível
            return -3 => movie_id não existe
            return -4 => client_id não existe
        '''
        
        result_query_movie = Movies.objects.filter(id=movie_id)
        result_query_client = Client.objects.filter(id=client_id)

        if not result_query_movie:
            return -3
        else:
            movie_object = result_query_movie[0]
            # Use the movie_object here
            movie_available = self.__check_movie_available(movie_object)
   
            
        if not result_query_client:
            return -4
        else:
            client_object = result_query_client[0]
        
        if movie_available:
            retorno = self.__charge_movie_value(client_object, movie_object)
            if not retorno:
                return -1
            self.__remove_item_from_stock(movie_object)
            self.create_movie_client_interaction(client_id, movie_id)
        else:
            return -2
        
        return 0
    
    def create_movie_client_interaction(self, client_id, movie_id):
        movie_client_interaction = MovieClient(client_id=client_id, movie_id=movie_id)
        # movie_client_interaction = self.create_movie_client_object(client_id, movie_id)
        self.save_object_in_database(movie_client_interaction)
        return movie_client_interaction

    def authenticate_user_with_password(self, client_id, password, email):
        result_query_client = Client.objects.filter(email=email)
        if not result_query_client:
            return -1
        
        client_object = result_query_client[0]
        return False if client_object.password != password else True        

    def __charge_movie_value(self, client_object, movie_object):
        #Cobra o valor do filme comprado
        movie_price = movie_object.price
        
        if client_object.money < movie_price:
                return False
            
        client_object.money = client_object.money - movie_price

        self.save_object_in_database(client_object)
        return True
    
    def __check_movie_available(self, movie_object):
        return movie_object.available_copies > 0

    def create_movie_client_object(self, client_id, movie_id):
        return MovieClient(client_id=client_id, movie_id=movie_id)



    def save_object_in_database(self, object_to_save):
        object_to_save.save(); return 0;

    def __remove_item_from_stock(self, movie_object):
        movie_object.available_copies = movie_object.available_copies - 1
        self.save_object_in_database(movie_object)
        return movie_object.available_copies

    def __check_for_number_in_string(self, string):
        return any(character.isdigit() for character in string)

    def __check_letters_in_string(self, string):
        return any(character.isalpha() for character in string)




    def __detect_special_character_in_string(self, string):
        character_list = ['@', '_', '!', '#', '$', 
        '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '\\', '|', '}', '{', 
        '~', ':', ']', '[']
        
        dictionary_for_faster_query = {k: None for k in character_list}
        
        return any(character in dictionary_for_faster_query for character in string)


if __name__ == '__main__':
    Client()
    