from flask import request
from flask_login import login_required

from redash.handlers.base import routes
from redash.utils import gen_query_hash


@routes.route('/api/utils/hashify', methods=['POST'])
@login_required
def hashify_query():
    arguments = request.get_json(force=True)
    sql = arguments.get("query_text", "")

    return gen_query_hash(sql)
