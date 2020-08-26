from fastapi import APIRouter

#from rest_api.controller import file_upload
from rest_api.controller import query

router = APIRouter()

router.include_router(query.router, tags=["query"])
#router.include_router(feedback.router, tags=["feedback"])
#router.include_router(file_upload.router, tags=["file-upload"])