from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from app.database import (
    delete_album as delete_album_from_db,
    get_album as get_album_from_db,
    get_user as get_user_from_db,
    list_albums,
    save_album,
    update_album as update_album_in_db,
)
from app.models import AlbumCreate, AlbumResponse, Token
from app.security import (
    create_access_token,
    get_current_user,
    verify_password,
)

router = APIRouter()


@router.get("/")
def home():
    return {"message": "API de médiathèque opérationnelle"}


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_from_db(form_data.username)
    if user is None or not verify_password(form_data.password, user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Identifiant ou mot de passe incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {
        "access_token": create_access_token(user["username"]),
        "token_type": "bearer",
    }


@router.post("/albums", response_model=AlbumResponse, status_code=status.HTTP_201_CREATED)
def create_album(album: AlbumCreate, _user: dict = Depends(get_current_user)):
    album_id = save_album(album)
    return get_album_from_db(album_id)


@router.get("/albums", response_model=list[AlbumResponse])
def read_albums():
    return list_albums()


@router.get("/albums/{album_id}", response_model=AlbumResponse)
def read_album(album_id: int):
    album = get_album_from_db(album_id)
    if album is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album introuvable")
    return album


@router.put("/albums/{album_id}", response_model=AlbumResponse)
def edit_album(
    album_id: int, album: AlbumCreate, _user: dict = Depends(get_current_user)
):
    if not update_album_in_db(album_id, album):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album introuvable")
    return get_album_from_db(album_id)


@router.delete("/albums/{album_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def remove_album(album_id: int, _user: dict = Depends(get_current_user)):
    if not delete_album_from_db(album_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album introuvable")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
