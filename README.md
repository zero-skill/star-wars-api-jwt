# star-wars-api-jwt
## People endpoints:
- `[GET] /people` Listar todos los registros de `people` en la base de datos.
- `[POST] /people` Añadir un registro de  `people` en la base de datos.
    ### Json body must have this data to insert:
        {
            "height": "some height",
            "mass": "some mass",
            "hair_color": "some hair color",
            "eye": "some eye color",
            "birth_year": "some birth year",       
            "gender": "some gender"
        }
- `[GET] /people/<int:people_id>` Listar la información de un solo `people`.
- `[PUT] /people/<int:people_id>` Actualiza la informacion de un solo `people`.
    ### Json body must have this data to modify:
        {
            "height": "some height",
            "mass": "some mass",
            "hair_color": "some hair color",
            "eye": "some eye color",
            "birth_year": "some birth year",       
            "gender": "some gender"
        }
- `[DELETE] /people/<int:people_id>` Elimina un `people` de la base de datos.
## Planet endpoints:
- `[GET] /planets` Listar los registros de `planets` en la base de datos.
- `[POST] /planets` Añadir un registro de  `planets` en la base de datos.
    ### Json body must have this data to insert:
        {
            "model":"some model",
	        "starship":"some starship",
	        "cost_in_credits":"some cost_in_credits",
	        "length":"some length",
	        "crew":"some crew",
	        "passengers":"some passengers",
	        "max_atmosphering_speed":"some max_atmosphering_speed",
	        "hyperdrive_rating":"some hyperdrive_rating",
	        "mGLT":"some mGLT",
	        "cargo_capacity":"some cargo_capacity",
	        "consumables":"some consumables"
        }
- `[GET] /planets/<int:planet_id>` Listar la información de un solo `planet`.
- `[PUT] /planets/<int:people_id>` Actualiza la informacion de un solo `planet`.
    ### Json body must have this data to modify:
        {
            "model":"some model",
	        "starship":"some starship",
	        "cost_in_credits":"some cost_in_credits",
	        "length":"some length",
	        "crew":"some crew",
	        "passengers":"some passengers",
	        "max_atmosphering_speed":"some max_atmosphering_speed",
	        "hyperdrive_rating":"some hyperdrive_rating",
	        "mGLT":"some mGLT",
	        "cargo_capacity":"some cargo_capacity",
	        "consumables":"some consumables"
        }
- `[DELETE] /planets/<int:people_id>` Elimina un `planet` de la base de datos.
## Login endpoint
- `[POST] /login` Inicia sesión con un usuario de la base de datos.
    ### Json body must have this data to login:
        {
            "username": "some username",
            "password": "some password"
        }
    ### The response contain:
        {
            "token": "TOKEN_JWT",
            "user_id": "current user_id"
        }
## Users & Favorites endpoints:
- `[GET] /users` Listar todos los usuarios.
- `[GET] /users/favorites` Listar todos los favoritos que pertenecen al usuario actual.
    > You need to add the `Auth Bearer Token` to header request.

- `[POST] /favorite/planet/<int:planet_id>` Añade un nuevo `planet` favorito al usuario actual con el id = `planet_id`.
    > You need to add the `Auth Bearer Token` to header request.
    ### Json body must be empty:
        {}
- `[POST] /favorite/people/<int:planet_id>` Añade un nueva `people` favorito al usuario actual con el id = `people_id`.
    > You need to add the `Auth Bearer Token` to header request. 
    ### Json body must be empty:
        {}
- `[DELETE] /favorite/planet/<int:planet_id>` Elimina un `planet` favorito con el `id = planet_id`.
    > You need to add the `Auth Bearer Token` to header request. 
- `[DELETE] /favorite/people/<int:people_id>` Elimina un `people` favorito con el `id = people_id`.
    > You need to add the `Auth Bearer Token` to header request. 
