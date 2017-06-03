class ReduceFieldsMixin:
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        query_params = getattr(self.context.get('request', {}), 'query_params', {})
        requested_fields = query_params.get('fields', None)

        if requested_fields:
            requested_fields = requested_fields.split(',')
            fields = {key: value for key, value in fields.items() if key in requested_fields}
        return fields
