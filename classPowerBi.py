import openai


class ConectionOnOpenAiExtractInformation():

    def __init__(self, token, data, ask):
        self.token = token
        self.data = data
        self.ask = ask
        openai.api_key= token


    def useOpenAi(self,texto):


        response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {'role':'user', 'content':texto}
        ]
    )
    
        # response = openai.completions.create(

        #         model= model_engine,
        #         prompt = texto,
        #         max_tokens = 2900,
        #         temperature = 0.4,
        #         n = 1,
        #         top_p = 0.2,
        #         presence_penalty = 1.0,
        #         frequency_penalty = 0.4

        #     )

        resposta = response.choices[0].message.content
        if resposta == '':
            resposta = 'Erro'
        else:
            a = 1

        return resposta
    
    def userAsk(self, ask):
        
        data = self.data
        ask = self.ask
        
        textoPadrao = f"""

            Aqui a tabela com dados:\n\n '{data}'\n\n{ask}"""
        
        resp = self.useOpenAi(textoPadrao)

        return resp
    
    