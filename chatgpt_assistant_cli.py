import argparse
from chatgpt_api_interaction import api_request

parser = argparse.ArgumentParser(description='CLI tool to exploit ChatGPT API')
parser.add_argument('api_key', help='your ChatGPT API key')
parser.add_argument('user_request', help='The user\'s request')
parser.add_argument('--path', '-f', help='Path to save chatgpt\'s response')
parser.add_argument('--path_file_to_debug', '-file', help='Path containing the file to debug')
parser.add_argument('--other_code', '-o', choices=['Yes', 'No'], help='To generate another code')
args = parser.parse_args()

maker = api_request(args=args)

if(maker.input_verification(args=args)):
    print("Your request already exists in the DataBase, please change it !")
else:
    if args.other_code:
        if args.other_code == 'Yes':
            maker.generate_other_responses(args=args)
            maker.print_response()
            maker.save_response_in_file(args=args)
            maker.save_response_in_db(args=args)
            
        elif args.other_code == 'No':
            maker.get_response()
            maker.print_response()
            maker.save_response_in_file(args=args)
            maker.save_response_in_db(args=args)
    else:
        maker.get_response()
        maker.print_response()
        maker.save_response_in_file(args=args)
        maker.save_response_in_db(args=args)