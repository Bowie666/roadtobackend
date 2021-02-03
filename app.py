from common import create_app
from common.config import DefaultConfig

app = create_app(DefaultConfig)


if __name__ == '__main__':
    app.run()
