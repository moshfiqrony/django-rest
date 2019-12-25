from django.shortcuts import render, get_object_or_404
from rest_framework import generics, mixins
from .models import MyChannel
from .serializers import MyChannelSerializer


class MyChannelViews(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = MyChannelSerializer

    def get_queryset(self):
        print('all')
        return MyChannel.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        print('single')
        passed_id = self.request.GET.get('id')
        obj = get_object_or_404(queryset, id=passed_id)
        return obj

    def get(self, request, *args, **kwargs):
        passed_id = self.request.GET.get('id')
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)
