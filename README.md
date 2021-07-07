# star-wars-api-jwt
## People endpoints:
- `[GET] /people` Listar todos los registros de `people` en la base de datos
- `[POST] /people` Añadir un registro de  `people` en la base de datos
- `[GET] /people/<int:people_id>` Listar la información de un solo `people`
- `[PUT] /people/<int:people_id>` Actualiza la informacion de un solo `people`
- `[DELETE] /people/<int:people_id>` Elimina un `people` de la base de datos
## Planet endpoints:
- `[GET] /planets` Listar los registros de `planets` en la base de datos
- `[POST] /planets` Añadir un registro de  `planets` en la base de datos
- `[GET] /planets/<int:planet_id>` Listar la información de un solo `planet`
- `[PUT] /planets/<int:people_id>` Actualiza la informacion de un solo `planet`
- `[DELETE] /planets/<int:people_id>` Elimina un `planet` de la base de datos
## Users & Favorites endpoints:
- `[GET] /users` Listar todos los usuarios 
- `[GET] /users/favorites` Listar todos los favoritos que pertenecen al usuario actual.
- `[POST] /favorite/planet/<int:planet_id>` Añade un nuevo `planet` favorito al usuario actual con el id = `planet_id`.
- `[POST] /favorite/people/<int:planet_id>` Añade un nueva `people` favorito al usuario actual con el id = `people_id`.
- `[DELETE] /favorite/planet/<int:planet_id>` Elimina un `planet` favorito con el `id = planet_id`.
- `[DELETE] /favorite/people/<int:people_id>` Elimina un `people` favorito con el `id = people_id`.
