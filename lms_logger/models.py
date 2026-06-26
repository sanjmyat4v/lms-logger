from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


# ── App Log ──────────────────────────────────────────────────────────────────

class AppLogRequest(BaseModel):
    service_id: str = Field(..., description="Registered service UUID (no dashes)")
    level: LogLevel
    message: str
    source_service: str
    environment: str
    created_at: datetime
    timestamp: datetime | None = Field(default=None, description="Defaults to now() if omitted")
    extra: dict[str, Any] | None = None

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
    service_id: str
    source_service: str
    environment: str
    actor_id: str | None = None
    actor_type: str
    action: str
    target_resource: str
    outcome: str
    event_time: datetime
    resource_id: str | None = None
    meta: dict[str, Any] | None = None

    model_config = {"use_enum_values": True}


class AuditLogResponse(BaseModel):
    log_id: int
    ingested_at: datetime