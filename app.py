import json

from flask import Flask, Response

import nccp_lib
import routes

app = Flask(__name__)


@app.route(routes.get_dnd_status)
def get_dnd_status(phone):
    result = nccp_lib.get_dnd_status(phone)
    return Response(status=result[0], response=json.dumps(result[1]))


if __name__ == '__main__':
    app.run()
