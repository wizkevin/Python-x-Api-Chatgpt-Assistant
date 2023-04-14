import requests
import json
from db import get_session
from repositories.answer_repository import ChatGptAnswersRepository

session = get_session()

class api_request:
    def __init__(self, args):
        self.headers = {
            'Authorization': f'Bearer {args.api_key}',
            'Content-Type': 'application/json'
        }
        
        if args.path_file_to_debug:
            self.content_file = self.extract_information(args=args)
            self.data = {
                "model": 'text-davinci-003',
                "prompt": f'{args.user_request} \n {self.content_file}',
                "max_tokens": 1000,
                "temperature": 0
            }
        else:
            self.data = {
                "model": 'text-davinci-003',
                "prompt": f'{args.user_request}',
                "max_tokens": 1000,
                "temperature": 0
            }
        
    def get_response(self):
        response = requests.request('POST', 'https://api.openai.com/v1/completions', headers=self.headers, data=json.dumps(self.data))
        print(response.status_code)
        self.result = response.json()
        self.result = self.result['choices'][0]['text'].strip()
        return self.result
    
    def save_response_in_file(self, args):
        with open(f'{args.path}\{args.user_request}.txt', 'w+') as file:
            file.write(f"{self.result}")
            
    def print_response(self):
        print(self.result)
    
    def save_response_in_db(self, args):
        answer_object = ChatGptAnswersRepository(db_session=session)
        answer_object.create_answer(input=args.user_request, answer=self.result)
        
    def generate_other_responses(self, args):
        self.data['prompt'] = f'Ecris trois(3) différents codes en Python pour {args.user_request}'
        response = requests.request('POST', 'https://api.openai.com/v1/completions', headers=self.headers, data=json.dumps(self.data))
        print(response.status_code)
        self.result = response.json()
        self.result = self.result['choices'][0]['text'].strip()
        return self.result
    
    def extract_information(self, args):
        with open(f"{args.path_file_to_debug}", 'r') as file:
            content = file.read()
        return content
    
    def input_verification(self, args):
        answer_object = ChatGptAnswersRepository(db_session=session)
        all_input = answer_object.get_all_input()
        bool_input = False
        
        for input in all_input:
            if args.user_request in input:
                bool_input = True
                
        return bool_input