from typing import List
from sqlalchemy.orm import Session

from models.chatgtp_answers import ChatGptAnswer


class ChatGptAnswersRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_answer_by_input(self, input: str) -> ChatGptAnswer:
        return self.db_session.query(ChatGptAnswer).filter(ChatGptAnswer.input == input).first()

    def get_all_answers(self) -> List[ChatGptAnswer]:
        return self.db_session.query(ChatGptAnswer).all()
    
    def get_all_input(self) -> List[ChatGptAnswer]:
        return self.db_session.query(ChatGptAnswer.input).all()

    def create_answer(self, input: str, answer: str) -> ChatGptAnswer:
        answer = ChatGptAnswer(input=input, answer=answer)
        self.db_session.add(answer)
        self.db_session.commit()
        return answer
