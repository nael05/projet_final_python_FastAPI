import sqlite3
from contextlib import closing
from pathlib import Path

from app.models import AlbumCreate

DATABASE_PATH = Path(__file__).resolve().parent.parent / "albums.db"


def initialize_database() -> None:
	with closing(sqlite3.connect(DATABASE_PATH)) as connection:
		connection.execute(
			"""
			CREATE TABLE IF NOT EXISTS albums (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				titre TEXT NOT NULL,
				artiste TEXT NOT NULL,
				genre TEXT NOT NULL,
				annee INTEGER NOT NULL,
				note REAL NOT NULL,
				note_interne TEXT NOT NULL DEFAULT ''
			)
			"""
		)
		connection.execute(
			"""
			CREATE TABLE IF NOT EXISTS users (
				username TEXT PRIMARY KEY,
				password_hash TEXT NOT NULL
			)
			"""
		)
		connection.commit()


def save_album(album: AlbumCreate) -> int:
	with closing(sqlite3.connect(DATABASE_PATH)) as connection:
		cursor = connection.execute(
			"""
			INSERT INTO albums (titre, artiste, genre, annee, note)
			VALUES (?, ?, ?, ?, ?)
			""",
			(
				album.titre,
				album.artiste,
				album.genre.value,
				album.annee,
				album.note,
			),
		)
		connection.commit()
		return cursor.lastrowid


def get_album(album_id: int) -> dict | None:
	with closing(sqlite3.connect(DATABASE_PATH)) as connection:
		connection.row_factory = sqlite3.Row
		row = connection.execute(
			"SELECT * FROM albums WHERE id = ?", (album_id,)
		).fetchone()
		return dict(row) if row else None


def list_albums() -> list[dict]:
	with closing(sqlite3.connect(DATABASE_PATH)) as connection:
		connection.row_factory = sqlite3.Row
		rows = connection.execute("SELECT * FROM albums ORDER BY id").fetchall()
		return [dict(row) for row in rows]


def update_album(album_id: int, album: AlbumCreate) -> bool:
	with closing(sqlite3.connect(DATABASE_PATH)) as connection:
		cursor = connection.execute(
			"""
			UPDATE albums
			SET titre = ?, artiste = ?, genre = ?, annee = ?, note = ?
			WHERE id = ?
			""",
			(
				album.titre,
				album.artiste,
				album.genre.value,
				album.annee,
				album.note,
				album_id,
			),
		)
		connection.commit()
		return cursor.rowcount > 0


def delete_album(album_id: int) -> bool:
	with closing(sqlite3.connect(DATABASE_PATH)) as connection:
		cursor = connection.execute("DELETE FROM albums WHERE id = ?", (album_id,))
		connection.commit()
		return cursor.rowcount > 0


def get_user(username: str) -> dict | None:
	with closing(sqlite3.connect(DATABASE_PATH)) as connection:
		connection.row_factory = sqlite3.Row
		row = connection.execute(
			"SELECT username, password_hash FROM users WHERE username = ?",
			(username,),
		).fetchone()
		return dict(row) if row else None


def create_user_if_missing(username: str, password_hash: str) -> None:
	with closing(sqlite3.connect(DATABASE_PATH)) as connection:
		connection.execute(
			"INSERT OR IGNORE INTO users (username, password_hash) VALUES (?, ?)",
			(username, password_hash),
		)
		connection.commit()
