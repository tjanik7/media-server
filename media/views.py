from rest_framework.response import Response
from rest_framework.views import APIView
import os.path

from media.models import ImageHash
import hashlib


def hash_image_from_bytes(file_bytes):
    # file_bytes: bytes
    # returns str

    img_hash = hashlib.md5()
    img_hash.update(file_bytes)

    return img_hash.hexdigest()


class TestView(APIView): # media/test-post
    def post(self, request):
        print(request.data)

        testKey = request.data['testKey']
        # keyParam = request.query_params['testKey']

        # print(f'param is {keyParam}')
        print(f'testKey is {testKey}')

        return Response({
            'testKey': 'Appears to be working'
        })


class FirstView(APIView): # media/hi
    def get(self, request):

        print(request)
        # print(request.query_params['sampleKey'])

        return Response({
            'testKey': 'looks like that worked!'
        })


    def post(self, request):
        base_path = '/Users/tyjanik/devel/media_server/script_sandbox/files_written'

        counts = {
            'created': 0,
            'existing': 0
        }

        print(f"Request data is {request.data}")

        for filename in request.data:
            img = request.data.get(filename)

            file_bytes = img.file.read()

            print(f'Got {len(file_bytes)} bytes from the file')

            dig = hash_image_from_bytes(file_bytes)

            # Cannot specify filename here, since we only want to query on img_hash field
            img_hash, created = ImageHash.objects.get_or_create(
                img_hash=dig
            )  # Save occurs automatically with 'get_or_create"

            base_filename = os.path.basename(filename)

            print(f'filename is "{filename}"')

            if created:
                # Update filename field on newly created object and save again
                img_hash.filename = base_filename
                img_hash.save()

                counts['created'] += 1

                # TODO: potentially switch to using hash as name, since it must be unique
                # would need to write it with file extension as well
                with open(os.path.join(base_path, base_filename), 'wb') as f:
                    f.write(file_bytes)

            else:
                counts['existing'] += 1

        resp_str = f'{counts["created"]} written; {counts["existing"]} existing files ignored'
        print(resp_str)

        return Response(
            resp_str
        )