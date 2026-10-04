@echo off
echo Lancement de l API FastAPI...
uvicorn app.main:app --reload
pause