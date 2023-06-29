
para crear el ejecutable y el archivo .spec:

pyinstaller --add-data "templates;templates" --add-data "static;static" --add-data "database;database" appcarasestableinestable.py


pyinstaller --add-data "templates;templates" --add-data "static;static" --add-data "database;database" --add-data "C:\Anaconda3\Lib\site-packages\plotly\;plotly" --add-data "C:\Anaconda3\Lib\site-packages\kaleido\;kaleido" --noconsole appcarasestableinestable.py











pyinstaller --add-data "templates;templates" --add-data "static;static" --add-data "database;database" --add-data "C:\Anaconda3\Lib\site-packages\plotly\;plotly" --add-data "C:\Anaconda3\Lib\site-packages\kaleido\;kaleido" --add-data "C:\Anaconda3\Lib\site-packages\PIL\;PIL" --add-data "C:\Anaconda3\Lib\site-packages\pandas\;pandas" --add-data "C:\Anaconda3\Lib\site-packages\fpdf\;fpdf" --add-data "C:\Anaconda3\Lib\site-packages\psutil\;psutil" --add-data "C:\Anaconda3\Lib\site-packages\sqlalchemy\;sqlalchemy" --add-data "C:\Anaconda3\Lib\site-packages\flask_sqlalchemy\;flask_sqlalchemy" --add-data "C:\Anaconda3\Lib\site-packages\numpy\;numpy" --add-data "C:\Anaconda3\Lib\site-packages\pytz\;pytz" --name AppCarasEstableInestable --noconsole appcarasestableinestable.py




pyinstaller --add-data "templates;templates" --add-data "static;static" --add-data "database;database" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\plotly\;plotly" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\kaleido\;kaleido" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\PIL\;PIL" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\pandas\;pandas" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\fpdf\;fpdf" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\sqlalchemy\;sqlalchemy" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\flask_sqlalchemy\;flask_sqlalchemy" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\numpy\;numpy" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\pytz\;pytz" --name AppCarasEstableInestable --noconsole appcarasestableinestable.py



pyinstaller --add-data "templates;templates" --add-data "static;static" --add-data "database;database" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\plotly\;plotly" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\kaleido\;kaleido" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\PIL\;PIL" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\pandas\;pandas" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\fpdf\;fpdf" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\sqlalchemy\;sqlalchemy" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\flask_sqlalchemy\;flask_sqlalchemy" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\numpy\;numpy" --add-data "C:\Anaconda3\envs\flaskapp\Lib\site-packages\pytz\;pytz" --name AppCarasEstableInestable --noconsole appcarasestableinestable.py








C:\Anaconda3\envs\flaskapp\Lib\site-packages








entorno de acaconda base 


pyinstaller --add-data "templates;templates" --add-data "static;static" --add-data "database;database" --add-data "C:\Anaconda3\Lib\site-packages\plotly\;plotly" --add-data "C:\Anaconda3\Lib\site-packages\kaleido\;kaleido" --add-data "C:\Anaconda3\Lib\site-packages\PIL\;PIL" --add-data "C:\Anaconda3\Lib\site-packages\pandas\;pandas" --add-data "C:\Anaconda3\Lib\site-packages\fpdf\;fpdf" --add-data "C:\Anaconda3\Lib\site-packages\sqlalchemy\;sqlalchemy" --add-data "C:\Anaconda3\Lib\site-packages\flask_sqlalchemy\;flask_sqlalchemy" --add-data "C:\Anaconda3\Lib\site-packages\numpy\;numpy" --add-data "C:\Anaconda3\Lib\site-packages\pytz\;pytz" --name AppCarasEstableInestable --noconsole appcarasestableinestable.py












para añadir cambios de en el archivo .spec: 

cambiar para que no muestre la consola console=True por console=False
para colocar un icono a la aplicación   icon='static/icon.ico' pero comprobar debe colocar la carpeta static
para cambiar el nombre a la aplicacion   name='appcarasestableinestable'name='appcarasestableinestable'


para ejecutar cambios de en el archivo .spec: 
pyinstaller appcarasestableinestable.spec
