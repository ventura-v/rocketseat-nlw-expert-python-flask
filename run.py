from src.main.server.server import app

if __name__ == '__main__':
    # A execução do servidor é feita quando o script é rodado diretamente, e não importado, com a checagem if __name__ == '__main__':.
    # Isso é padrão em aplicações Flask para iniciar o servidor apenas quando o script é o ponto de entrada principal.

    app.run(host='0.0.0.0', port=3000, debug=True)
    # o argumento "debug=True" permite atualizar o servidor sempre que salvar algo
