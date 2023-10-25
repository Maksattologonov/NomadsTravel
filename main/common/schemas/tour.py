import coreapi
import coreschema
from rest_framework.schemas.coreapi import AutoSchema


class AccommodationSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == 'GET':
            api_fields = [
                coreapi.Field(name='id', required=False, location='path',
                              schema=coreschema.String(description='int (id)'), ),
                coreapi.Field(name='name', required=False, location='path',
                              schema=coreschema.String(description='str (name)')),
            ]
        return self._manual_fields + api_fields


class CitySchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == 'GET':
            api_fields = [
                coreapi.Field(name='id', required=False, location='path',
                              schema=coreschema.String(description='int (id)'), ),
                coreapi.Field(name='name', required=False, location='path',
                              schema=coreschema.String(description='str (name)')),
            ]
        return self._manual_fields + api_fields
