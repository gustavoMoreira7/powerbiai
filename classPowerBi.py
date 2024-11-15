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
                temperature = 0.2,
                n = 1,
                top_p = 0.7,
                presence_penalty = 0.5,
                frequency_penalty = 0.2

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
        
        prompt = f"""
            Você é um analista de dados. Abaixo está uma tabela representada como texto, seguida de uma pergunta. Analise os dados cuidadosamente e forneça uma resposta clara e objetiva.

            Dados da tabela:
            {data}

            Pergunta: {ask}

            Resposta: 
        """

        
        resp = self.useOpenAi(prompt)

        return resp
    
    