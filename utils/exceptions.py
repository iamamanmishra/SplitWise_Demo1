class AudioCroppingException(Exception):
    pass


class AudioSegmentationException(Exception):
    pass


class DiarizedSpeakerIdentificationException(Exception):
    pass


class GMMSpeakerIdentificationException(Exception):
    pass


class GMMSpeakerTrainingException(Exception):
    pass


class InsufficientTrainingAudioException(Exception):
    pass


class SpeakerIDSpeakerCreationException(Exception):
    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message, status_code)
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return f"{self.status_code} {self.message}"


class SpeakerIDSpeakerIdentificationException(Exception):
    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message, status_code)
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return f"{self.status_code} {self.message}"


class SpeakerIDSpeakerTrainingException(Exception):
    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message, status_code)
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return f"{self.status_code} {self.message}"


class SpeakerMetadataDatabaseException(Exception):
    def __init__(self, message: str, status_code: int = 502):
        super().__init__(message, status_code)
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return f"{self.status_code} {self.message}"
