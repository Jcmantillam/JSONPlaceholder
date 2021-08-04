import json
import requests
from typing import List, Set, Dict, Tuple, Optional


def API_requests(url: str, method:str, headers: Dict, data: Dict):
    response = requests.request(
        method,
        url,
        headers=headers,
        data=data
    )
    return response


def identify_object(data: Dict):
    keys = list(data.keys())
    
    if 'userId' in keys:
        if 'body' in keys:
            return 'post'
        elif 'completed' in keys:
            return 'todo'
        else:
            return 'album'
    elif 'postId' in keys:
        return 'comment'
    elif 'albumId' in keys:
        return 'photo'
    elif 'username' in keys:
        return 'user'
    else:
        return 'not_type'