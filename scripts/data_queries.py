from models import Response
import pandas as pd

def get_responses_by_question(question_id):
    query = (Response
             .select(Response.answer)
             .where(Response.question == question_id))
    return pd.DataFrame(query.dicts())
