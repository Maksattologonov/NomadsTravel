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


class DestinationsSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == 'GET':
            api_fields = [
                coreapi.Field(name='title', required=False, location='path',
                              schema=coreschema.String(description='str (title)'), ),
                coreapi.Field(name='category', required=False, location='path',
                              schema=coreschema.String(description='str (category)')),
            ]
            return self._manual_fields + api_fields


class DestinationSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == 'GET':
            api_fields = [
                coreapi.Field(name='id', required=False, location='query',
                              schema=coreschema.String(description='int (id)')),
            ]
            return self._manual_fields + api_fields


class TourSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == 'GET':
            api_fields = [
                coreapi.Field(name='title', required=False, location='path',
                              schema=coreschema.String(description='str (title)'), ),
                coreapi.Field(name='category', required=False, location='path',
                              schema=coreschema.String(description='str (category)')),
            ]
            return self._manual_fields + api_fields


class DestinationRatingSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == 'POST':
            api_fields = [

                coreapi.Field(name='destination', required=False, location='form',
                              schema=coreschema.String(description='int (id)'), ),
                coreapi.Field(name='value', required=False, location='form',
                              schema=coreschema.String(description='decimal (value)')),
            ]
            return self._manual_fields + api_fields
