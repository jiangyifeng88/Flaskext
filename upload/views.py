from flask import Blueprint, request

upload_blue = Blueprint('upload'.__name__)


@upload_blue.route('img', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        images.save(request.files['img'])
        return ''
    elif request.method == 'GET':
        return render_templates('upload.html')



    request.files
