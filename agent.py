from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
from fastapi.middleware.cors import CORSMiddleware

class CodeRequest(BaseModel):
    request_id: int
    code: str

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def handle_code_request(code_request: CodeRequest):
    with open(f"{code_request.request_id}.py", "w") as f:
        f.write(code_request.code)
    return f"file written {code_request.request_id}.py"

@app.get("/health_check")
def health_check():
    return {"status": "ok"}

@app.post("/execute")
def execute(CodeRequest: CodeRequest):
    handle_code_request(CodeRequest)
    codeRun = subprocess.run(["python", f"{CodeRequest.request_id}.py"], capture_output=True)  # type: ignore
    return {
        "inicial_request": {
        "request_id": CodeRequest.request_id, 
        "code": CodeRequest.code
        },
        "result": codeRun
    }
