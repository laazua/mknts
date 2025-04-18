from app import router


@router.get('/openserver')
async def open_server():
    return {
        'message': 'open server'
    }
