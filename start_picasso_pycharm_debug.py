import os
import sys

os.environ["PICASSO_SETTINGS"] = "/absolute/path/to/config.py"  # Must run before we import (i.e. load) `app`

from picasso import app

# IN FACT, RUNNING WITHOUT THE BELOW WORKED
"""
if not ('pydevd' in sys.modules):
    # To debug in PyCharm, see http://www.adamburvill.com/2015/04/debugging-flask-app-with-pycharm.html
    #  and see http://flask.pocoo.org/docs/0.12/quickstart/
    print("Running flask with PyCharm debug.")
    app_options = {"port":5000}
    app_options["debug"] = True
    app_options["use_debugger"] = False
    app_options["use_reloader"] = False

    app.run(**app_options)
else:
    app.run()
"""
app.run()
