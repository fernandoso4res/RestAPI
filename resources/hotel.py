from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    {
        "hotel_id": "alpha",
        "nome": "Alpha Hotel",
        "cidade": "Nova Petropolis",
        "estrelas": "4.5",
        "diaria": "400"
    },
    {
        "hotel_id": "bravo",
        "nome": "Bravo Hotel",
        "cidade": "Nova Petropolis",
        "estrelas": "3",
        "diaria": "280"
    },
    {
        "hotel_id": "charlie",
        "nome": "Charlie Hotel",
        "cidade": "Rio de Janeiro",
        "estrelas": "5",
        "diaria": "700"
    }
]

class Hoteis(Resource):
    def get(self):
        return{'hoteis': hoteis
        }

class HotelModel:
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade    
        }

class Hotel(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('cidade')
    argumentos.add_argument('diaria')



    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

       
        
    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return{'message': 'Hotel not Found'}, 404

    def post(self, hotel_id):
        
        dados = Hotel.argumentos.parse_args() 
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hoteis.append(novo_hotel)

        return novo_hotel, 200

    def put(self, hotel_id):

        hotel = Hotel.find_hotel(hotel_id)
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200 # OK

        hoteis.append(novo_hotel)
        return novo_hotel, 201 #created = criado
        
    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel Deleted.'}