# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files, copy_metadata, collect_submodules

# Include the necessary static files
datas = [
    (r'myenv\\Lib\\site-packages\\streamlit\\runtime', r'myenv\\Lib\\site-packages\\streamlit\\runtime'),
    (r'data\\NETSCOUT.pdf', 'data'),
]

# Collect additional data files and metadata
datas += collect_data_files("streamlit")
datas += collect_data_files("langchain")
datas += copy_metadata("streamlit")
datas += copy_metadata("langchain")

# Collect all submodules
hiddenimports = collect_submodules("streamlit")
hiddenimports += collect_submodules("langchain")

block_cipher = None

a = Analysis(
    ['run.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='wrap',
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
