# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ["'C:\\Program Files\\Algoritmika\\algovenv\\Scripts\\python.exe", 'c:/Program Files/Algoritmika/vscode/data/extensions/algoritmika.algopython-20240404.120101.0/data/student/2985430/657891/shooter_game.pyC:\\Program', "Files\\Algoritmika\\vscode\\data\\extensions\\algoritmika.algopython-20240404.120101.0\\data\\student\\2985430\\657891\\shooter_game.py'"],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='python',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
