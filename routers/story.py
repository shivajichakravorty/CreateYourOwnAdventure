import uuid
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends, Cookie, Response, BackgroundTasks
from sqlalchemy.orm import Session

from backend.db.database import get_db, SessionLocal
from backend.models.story import Story, StoryNode, StoryOption
from backend.models.job import StoryJob
from backed.schemas.story import CreateStoryRequest, CompleteStoryResponse, CompleteStoryNodeResponse
from backend.schemas.job import StoryJobCreateRequest, StoryJobResponse


