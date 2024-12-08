import os


DATABASE_URL = f"sqlite:///{os.path.join(os.path_dirname(__file__),'users.db')}"
