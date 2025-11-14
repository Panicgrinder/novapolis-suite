import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="MCP OpenAI Eval Bridge", version="0.1.0")


class HealthResponse(BaseModel):
    status: str


@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(status="ok")


def main() -> None:
    uvicorn.run("mcp_openai_eval.server:app", host="0.0.0.0", port=4000, reload=False)


if __name__ == "__main__":
    main()
