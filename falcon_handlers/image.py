import gevent, json, falcon, uuid, os, mimetypes,io
from gevent.queue import Queue
from handlers.hooks import with_json_payload

class ImageHandler(object):
    _CHUNK_SIZE_BYTES = 4096
    def __init__(self, storage_path):
        self._storage_path = storage_path

    def on_post(self, req, resp):
        print('here')
        ext = mimetypes.guess_extension(req.content_type)
        name = '{uuid}{ext}'.format(uuid=uuid.uuid4(), ext=ext)
        image_path = os.path.join(self._storage_path, name)

        with io.open(image_path, 'wb') as image_file:
            while True:
                chunk = req.stream.read(self._CHUNK_SIZE_BYTES)
                if not chunk:
                    break
                image_file.write(chunk)
        print('here')

        resp.status = falcon.HTTP_201
        resp.location = '/images/' + name
        return resp     
