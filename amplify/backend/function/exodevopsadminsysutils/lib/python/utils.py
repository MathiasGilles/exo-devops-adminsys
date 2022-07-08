import re

def get_user_id (event):
    user_id = None
    cognitoAuthenticationProvider = event['requestContext']['identity']['cognitoAuthenticationProvider']
    parts = cognitoAuthenticationProvider.split(':')
    if parts[-2] == 'CognitoSignIn':
        regex = re.compile(r'\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b')
    if regex.match(parts[-1]):
        user_id = parts[-1]

    if user_id is None or len(user_id) <= 0:
        raise ValueError('Input error: user_id')

    return user_id