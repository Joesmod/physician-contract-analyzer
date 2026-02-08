from pydantic import BaseModel, Field

class KeyTerm(BaseModel):
    category: str
    extracted_text: str
    plain_english: str
    risk_level: str

class RedFlag(BaseModel):
    title: str
    description: str
    severity: str
    recommendation: str

class AnalysisResponse(BaseModel):
    summary: str
    key_terms: list[KeyTerm] = Field(default_factory=list)
    red_flags: list[RedFlag] = Field(default_factory=list)
    overall_risk_score: int = Field(ge=1, le=10)

class HealthResponse(BaseModel):
    status: str = "ok"
    service: str = "physician-contract-analyzer"
