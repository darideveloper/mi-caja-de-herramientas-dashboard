from django.core.exceptions import ValidationError


def validate_video_extension(value):
    if not value.name.endswith('.mp4'):
        error = 'El archivo no es un video válido. '
        error += 'Por favor, suba un archivo .mp4'
        raise ValidationError(error)
    
    
def validate_audio_extension(value):
    if not value.name.endswith('.mp3'):
        error = 'El archivo no es un audio válido. '
        error += 'Por favor, suba un archivo .mp3'
        raise ValidationError(error)