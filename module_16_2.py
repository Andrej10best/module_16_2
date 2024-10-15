from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/')
async def get_main_page():
    return 'Главная страница'

@app.get('/user/admin')
async def get_admin_page():
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def get_user_info(user_id: int = Path(ge=1, le=100, description='Enter User ID', example='1')):
    return f'Вы вошли как пользователь №{user_id}'

@app.get('/user/{username}/{age}')
async def get_user_number(username: str = Path(ge=5, le=20, description='Enter username', example='UrbanUser'),
                          age: int = Path(ge=18, le=120, description='Enter age', example='24')):
    return {'Имя:': username, 'Возраст:': age}

