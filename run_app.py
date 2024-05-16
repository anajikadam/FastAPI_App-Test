import uvicorn
from config import UVI_APP_PORT, UVI_APP_HOST


# if __name__ == '__main__':
#     uvicorn.run("app:app", port=8787, host='0.0.0.0',
#     reload = True, 
#     )


# if __name__ == '__main__':
#     uvicorn.run("app:app", port=5500, host='0.0.0.0',
#     reload = True, ssl_keyfile="SSL/key2.key", ssl_certfile="SSL/cert2.crt"
#     )



if __name__ == '__main__':
    print("App Started...!!!!!")
    uvicorn.run("app:app",  
                host=UVI_APP_HOST,
                port=UVI_APP_PORT, 
                # debug = True,
                reload = True,
    )
                # limit_concurrency=3)