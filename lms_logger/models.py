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
    id: int
    service_id: str
    level: str
    message: str
    timestamp: datetime
    extra: dict[str, Any] | None = None


# ── Batch App Log ─────────────────────────────────────────────────────────────

class BatchAppLogRequest(BaseModel):
    logs: list[AppLogRequest]


class BatchLogResult(BaseModel):
    index: int
    success: bool
    id: int | None = None
    error: str | None = None


class BatchAppLogResponse(BaseModel):
    results: list[BatchLogResult]


# ── Audit Log ─────────────────────────────────────────────────────────────────

class AuditLogRequest(BaseModel):
    service_id: str = Field(..., description="Registered service UUID (no dashes)")
    actor_id: str | None = None
    action: str
    resource: str | None = None
    resource_id: str | None = None
    timestamp: datetime | None = None
    meta: dict[str, Any] | None = None

    model_config = {"use_enum_values": True}


class AuditLogResponse(BaseModel):
    id: int
    service_id: str
    actor_id: str | None = None
    action: str
    resource: str | None = None
    resource_id: str | None = None
    timestamp: datetime
    meta: dict[str, Any] | None = None