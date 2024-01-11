# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import copy_metadata
from PyInstaller.utils.hooks import collect_data_files, collect_submodules,collect_dynamic_libs

# Define a function to collect the necessary resources
def collect_all(package):
    data = collect_data_files(package, include_py_files=True)
    hiddenimports = collect_submodules(package)
    binaries = collect_dynamic_libs(package, destdir=package)
    return (data, hiddenimports, binaries)

ultralytics_data, ultralytics_hiddenimports, ultralytics_binaries = collect_all('ultralytics')

datas=[('data/demo.mp4','data')]
datas += ultralytics_data

hiddenimports = []
hiddenimports += ultralytics_hiddenimports

binaries = []
binaries += ultralytics_binaries

a = Analysis(
    ['src\\bbshot_counter_app.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='bbshot_counter_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='bbshot_counter_app',
)
