from fastapi import APIRouter, Request, Body, UploadFile, File

from database.photoservice import add_photo_db

photo_router = APIRouter(prefix="/photo",
                         tags=["Управление фотографиями"])

@photo_router.post("/add_photo")
async def add_photo(post_id: int,
                    photo_file: UploadFile = File(...)):
    if photo_file:
        with open(f"database/photos/photo_{post_id}.jpg", "wb") as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)
            add_photo_db(post_id, f"database/photos/photo_{post_id}.jpg")
        return {"status":1, "message": "Фото успешно загружено"}
    return {"status": 0, "message": "Фото не загружено"}

