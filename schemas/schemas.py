from pydantic import BaseModel
from typing import Optional


class Diarization_and_transcription(BaseModel):
    uuid: str


class text_to_text_translation_fromJSON(BaseModel):
    uuid: str
    audio_lang: Optional[str] = None
    target_lang: Optional[str] = None
