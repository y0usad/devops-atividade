import unittest

from app import app, hello


class TestAplicacaoFlask(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_funcao_hello_retorna_mensagem_esperada(self):
        mensagem = hello()

        self.assertEqual(
            mensagem,
            "Olá! Esta é uma aplicação Dockerizada para a atividade de DevOps.",
        )

    def test_pagina_inicial_retorna_status_200(self):
        resposta = self.client.get("/")

        self.assertEqual(resposta.status_code, 200)

    def test_pagina_inicial_exibe_mensagem_esperada(self):
        resposta = self.client.get("/")

        self.assertIn("aplicação Dockerizada", resposta.get_data(as_text=True))

    def test_pagina_inicial_retorna_conteudo_html(self):
        resposta = self.client.get("/")

        self.assertEqual(resposta.mimetype, "text/html")

    def test_pagina_inicial_rejeita_metodo_post(self):
        resposta = self.client.post("/")

        self.assertEqual(resposta.status_code, 405)

    def test_rota_inexistente_retorna_status_404(self):
        resposta = self.client.get("/rota-inexistente")

        self.assertEqual(resposta.status_code, 404)


if __name__ == "__main__":
    unittest.main()
