import json
import logging
import time
from math import degrees

from fastapi import APIRouter

from openai import OpenAI
from sqlalchemy.orm import session
from starlette.responses import JSONResponse

from src.database.database import engine
from src.repository.ClassroomRepository import ClassroomRepository
from src.repository.CourseRepository import CourseRepository
from src.repository.DegreeRepository import DegreeRepository
from src.repository.SubjectRepository import SubjectRepository
from src.repository.TeacherRepository import TeacherRepository
from src.routes.course_route import course
from src.utils.EnvironmentVariableResolver import EnvironmentVariableResolver

logger = logging.getLogger(__name__)
schedule = APIRouter()

client = OpenAI(api_key=EnvironmentVariableResolver().get_openai_key())

def create_thread_id() -> str:
    thread = client.beta.threads.create()
    return str(thread.id)

def conversation(thread_id: str, user_input: str, assistant_id: str) -> str:
    create_threads_message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_input,
    )


    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    while True:
        time.sleep(5)

        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )


        if run_status.status == 'completed':
            messages = client.beta.threads.messages.list(
                thread_id=thread_id,
            )


            return messages.data[0].content[0].text.value

        elif run_status.status == 'requires_action':


            required_actions = run_status.required_action.submit_tool_outputs.model_dump()
            tool_outputs = []

            for action in required_actions["tool_calls"]:
                func_name = action['function']['name']
                #
                # if func_name == "get_delivery_time":
                #     tool_outputs.append({
                #         "tool_call_id": action['id'],
                #         "output": self.get_delivery_time()
                #     })
                #
                # else:
                #     self.logger.error(f"Unknown function called assistant.conversation: {func_name}")
                #
                #     raise ValueError(f"Unknown function: {func_name}")

            if tool_outputs:
                client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread_id,
                    run_id=run.id,
                    tool_outputs=tool_outputs
                )

        else:

            time.sleep(5)




def extract_json(message):
    try:
        start = message.find('{')
        end = message.rfind('}') + 1
        if start != -1 and end != -1:
            extracted_json = message[start:end]
            parsed_json = json.loads(extracted_json)
            return parsed_json
        else:
            raise ValueError("No JSON found in the message.")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in the message.")



@schedule.get("/")
async def get_schedule():
    try:


        user_input = f"Genera un horario usando los siguientes datos del colegio"

        classrooms = ClassroomRepository().find_all()


        for item in classrooms:
            user_input += f"\n {item.to_dict()}"

        courses = CourseRepository().find_all()

        for item in courses:
            user_input += f"\n {item}"

        degrees = DegreeRepository().find_all()

        for item in degrees:
            user_input += f"\n {item}"

        subject = SubjectRepository().find_all()

        for item in subject:
            user_input += f"\n {item}"

        teacher = TeacherRepository().find_all()

        for item in teacher:
            user_input += f"\n {item}"

        thread = create_thread_id()

        response = conversation(
            thread_id=thread,
            user_input=user_input,
            assistant_id="asst_4tUEyaWYMfRoyDscs3WaZxbF"
        )



        print(
            response
        )

        print(
            extract_json(response)
        )

        return JSONResponse(content=extract_json(response))

    except Exception as e:
        logger.error(f"Error fetching schedule: {str(e)}", exc_info=True)
        raise e


