import openai


class ConectionOnOpenAiExtractInformation():

    def __init__(self, token, data, ask):
        self.token = token
        self.data = data
        self.ask = ask
        openai.api_key= token


    def useOpenAi(self,texto):

        model_engine = 'gpt-3.5-turbo-instruct'
    
        response = openai.completions.create(

                model= model_engine,
                prompt = texto,
                max_tokens = 2900,
                temperature = 0.4,
                n = 1,
                top_p = 0.2,
                presence_penalty = 1.0,
                frequency_penalty = 0.4

            )

        resposta = response.choices[0].text

        if resposta == '':
            resposta = 'Erro'
        else:
            a = 1

        return resposta
    
    def userAsk(self, ask):
        
        data = self.data
        ask = self.ask
        
        textoPadrao = f"""

            com base no data frame:

            '{data}'

            responda: {ask}"""
        
        resp = self.useOpenAi(textoPadrao)

        return resp
    
    