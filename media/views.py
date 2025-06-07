from rest_framework.response import Response
from rest_framework.views import APIView
import os.path

from media.models import ImageHash
import hashlib


def get_file_extension(filename):
    return '.' + filename.split('.')[-1]


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
        base_path = '/Users/tyjanik/devel/media_server/backed_up_files'

        counts = {
            'created': 0,
            'existing': 0
        }

        print(f"Request data is {request.data}")

        for paramName in request.data:
            print('\n--- Processing new file ---\n')
            img = request.data.get(paramName)

            print(f'img has type {type(img)}')

            file_bytes = img.file.read()
            filename = img.name

            print(f'Got {len(file_bytes)} {type(file_bytes)} from the file')

            dig = hash_image_from_bytes(file_bytes)

            # Cannot specify filename here, since we only want to query on img_hash field
            img_hash, created = ImageHash.objects.get_or_create(
                img_hash=dig
            )  # Save occurs automatically with 'get_or_create"

            base_filename = os.path.basename(filename)  # TODO: switch to using ID as filename now

            print(f'paramName is "{paramName}" and filename is "{filename}"')

            file_extension = get_file_extension(filename)
            print(f'file extension is "{file_extension}"')

            if created:
                # Update filename field on newly created object and save again

                # Skipping this since we prob don't care about keeping a randomly generated filename around
                # img_hash.filename = base_filename
                # img_hash.save()

                counts['created'] += 1

                # would need to write it with file extension as well

                abs_file_path = os.path.join(base_path, dig + file_extension)

                print(f'absolute dest file path is {abs_file_path}')

                with open(abs_file_path, 'wb') as f:
                    f.write(file_bytes)

            else:
                counts['existing'] += 1

            print()

        resp_str = f'{counts["created"]} written; {counts["existing"]} existing files ignored'
        print(resp_str)

        return Response(
            resp_str
        )