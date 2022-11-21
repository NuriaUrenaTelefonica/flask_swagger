#!/usr/bin/env python3

import connexion

from swagger_client import encoder



def main():
    app = connexion.App(__name__, specification_dir='./swagger_client/swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'EDEM BlackJack Casino - Client'}, pythonic_params=True)
    app.run(port=8081,debug=True)


if __name__ == '__main__':
    main()