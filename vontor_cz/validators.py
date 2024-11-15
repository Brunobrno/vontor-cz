from django.core.exceptions import ValidationError

def file_size(value, limit): # add this to some file where you can import it from
    '''
    ---
    do `limit` napiš počet MegaBajtu!
    ---

    '''
    calculated_limit = limit * 1024 * 1024
    
    if value.size > calculated_limit:
        raise ValidationError('File too large. Size should not exceed ' + str(limit) + ' MiB.')

def photo_extension(value):
    '''
    ověření přípon souboru které funguji s html
    '''
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.apng' , '.avif', '.svg', '.webp']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported image file.')