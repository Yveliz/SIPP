from rest_framework import viewsets, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework import serializers
from .models import Resultados

class ResultadosSerializer(serializers.ModelSerializer):
    resultados_int = serializers.SerializerMethodField()

    class Meta:
        model = Resultados
        exclude = []
        read_only_fields = ['spoares_id']
        extra_kwargs = {
            'spoares_dependede': {'required': False},
            'spoares_insert': {'required': False},
            'spoares_update': {'required': False},
            'spoares_delete': {'required': False},
            'spoares_propietario': {'required': False},
            # Agrega aquí los campos que deseas que no sean obligatorios y sus opciones
        }

    def get_resultados_int(self, obj):
        context = self.context.copy()
        context['lvl'] = '2' if context['lvl'] == '3' else '3'

        lower_level_objects = Resultados.objects.filter(
            spoares_dependede=obj.spoares_id,
            spoares_vigencia_inicio=context['request'].GET.get('anioi', None),
            spoares_finalizacion=context['request'].GET.get('aniof', None),
            spoares_restrictiva='N',
            spoares_nivel=context['lvl']
        )

        return ResultadosSerializer(lower_level_objects, many=True, context=context).data


class ResultadosAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ResultadosSerializer
    queryset = Resultados.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lvl'] = self.request.GET.get('lvl')
        return context

    def get_queryset(self):
        anio_inicio = self.request.GET.get('anioi')
        anio_final = self.request.GET.get('aniof')
        lvl = self.request.GET.get('lvl')
        product_data = []
        
        resultados = Resultados.objects.all()
        queryset = super().get_queryset()

        if anio_inicio:
            queryset = queryset.filter(spoares_vigencia_inicio=anio_inicio,spoares_finalizacion=anio_final , spoares_restrictiva='N')

        if lvl == '1':
            queryset = Resultados.objects.filter(spoares_nivel=lvl, spoares_vigencia_inicio=anio_inicio,spoares_finalizacion=anio_final,spoares_restrictiva='N')

        elif lvl == '2':      
            queryset = Resultados.objects.filter(
                Q(spoares_nivel='1') & Q(spoares_restrictiva='N') & Q(spoares_finalizacion__gte=anio_final) & Q(spoares_vigencia_inicio__lte=anio_inicio)
            )
        elif lvl == '3':
            #queryset = Resultados.objects.filter(spoares_nivel='1', spoares_restrictiva='N')
            queryset = Resultados.objects.filter(
                Q(spoares_nivel='1') & Q(spoares_restrictiva='N') & Q(spoares_finalizacion__gte=anio_final) & Q(spoares_vigencia_inicio__lte=anio_inicio)
            )
        return queryset



    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data.pop('spoares_id', None)  # Asignar None al campo 'spoares_id' para que se genere automáticamente en la base de datos
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    @action(detail=False, methods=['post'])
    def custom_action(self, request):
        # Aquí va tu lógica personalizada para el método POST
        return Response({"message": "Custom POST action"})
    
    def destroy(self, request, *args, **kwargs):
        # Puedes implementar tu lógica personalizada aquí
        # Por ejemplo, obtén el objeto que se va a eliminar:
        instance = self.get_object()

        # Puedes hacer algo con el objeto antes de eliminarlo, si lo deseas
        # ...

        # Ahora procede a eliminar el objeto
        self.perform_destroy(instance)
        
        # Y puedes retornar una respuesta personalizada si quieres
        return Response({"message": "Objeto eliminado"}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        # Aquí es donde realmente se elimina el objeto
        instance.delete()
        
    def update(self, request, *args, **kwargs):
        # Puedes implementar tu lógica personalizada aquí
        # Por ejemplo, obtén el objeto que se va a actualizar:
        instance = self.get_object()

        # Usamos el serializer para validar los datos de la request
        serializer = self.get_serializer(instance, data=request.data, partial=False)  # 'partial=False' indica que es un PUT, no un PATCH

        if serializer.is_valid():
            # Si los datos son válidos, procedemos a guardarlos
            self.perform_update(serializer)
            
            # Y puedes retornar una respuesta personalizada si quieres
            return Response({"message": "Objeto actualizado", "resultados": serializer.data}, status=status.HTTP_200_OK)
        else:
            # En caso contrario, retornamos un error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        # Aquí es donde realmente se guarda el objeto
        serializer.save()
