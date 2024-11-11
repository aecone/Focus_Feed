from flask import Blueprint, Response, request
import requests

proxy_bp = Blueprint('proxy', __name__)

@proxy_bp.route('/proxy-image')
def proxy_image():
    image_url = request.args.get('url')
    if not image_url:
        return {"error": "No URL provided"}, 400
    
    response = requests.get(image_url, stream=True)
    
    # Forward the content if the request is successful
    if response.status_code == 200:
        return Response(response.content, mimetype="image/jpeg")
    else:
        return {"error": "Unable to fetch image"}, 404
