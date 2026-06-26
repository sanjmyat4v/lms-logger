from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"


# ── App Log ──────────────────────────────────────────────────────────────────

class AppLogRequest(BaseModel):
    context_json: dict[str, Any] | None = None
    created_at: datetime
    environment: str
    level: LogLevel
    message: str
    source_service: str
    trace_id: str

    model_config = {"use_enum_values": True}


class AppLogResponse(BaseModel):
    log_id: int
    ingested_at: datetime


# ── Batch App Log ─────────────────────────────────────────────────────────────

class BatchAppLogRequest(BaseModel):
    logs: list[AppLogRequest]


class BatchLogResult(BaseModel):
    index: int
    success: bool
    log_id: int | None = None
    error_code: str | None = None
    message: str | None = None


class BatchAppLogResponse(BaseModel):
    results: list[BatchLogResult]
    total: int
    succeeded: int
    failed: int


# ── Audit Log ─────────────────────────────────────────────────────────────────

class AuditLogRequest(BaseModel):
    action: str
    actor_id: str | None = None
    actor_type: str
    detail_json: dict[str, Any] | None = None
    environment: str
    event_time: datetime
    ip_address: str
    outcome: str
    source_service: str
    target_resource: str
    
    model_config = {"use_enum_values": True}


class AuditLogResponse(BaseModel):
    log_id: int
    ingested_at: datetime