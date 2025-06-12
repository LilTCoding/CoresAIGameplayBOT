@echo off
echo Creating icon...
python create_icon.py

echo Installing PyInstaller...
pip install pyinstaller

echo Building executable...
pyinstaller CoresModTrainer.spec

echo Build complete! The executable is in the dist folder.
pause 