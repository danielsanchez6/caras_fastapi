# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['appcarasrealistas.py'],
             pathex=[],
             binaries=[],
             datas=[('templates', 'templates'), ('static', 'static'), ('database', 'database'), ('C:\\Anaconda3\\envs\\flask\\Lib\\site-packages\\plotly\\', 'plotly'), ('C:\\Anaconda3\\envs\\flask\\Lib\\site-packages\\kaleido\\', 'kaleido'), ('C:\\Anaconda3\\envs\\flask\\Lib\\site-packages\\PIL\\', 'PIL'), ('C:\\Anaconda3\\envs\\flask\\Lib\\site-packages\\pandas\\', 'pandas'), ('C:\\Anaconda3\\envs\\flask\\Lib\\site-packages\\fpdf\\', 'fpdf'), ('C:\\Anaconda3\\envs\\flask\\Lib\\site-packages\\sqlalchemy\\', 'sqlalchemy'), ('C:\\Anaconda3\\envs\\flask\\Lib\\site-packages\\flask_sqlalchemy\\', 'flask_sqlalchemy'), ('C:\\Anaconda3\\envs\\flask\\Lib\\site-packages\\numpy\\', 'numpy'), ('C:\\Anaconda3\\envs\\flask\\Lib\\site-packages\\pytz\\', 'pytz')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
             
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='AppCarasHiperrealistas',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='AppCarasHiperrealistas')
