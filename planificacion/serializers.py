from rest_framework import serializers
from .models import Producto
from .models import Direccion, Periodo
from .models import Accion, CentroCosto, Correlativo, Direccion, FuenteFinanciamiento, Insumo, InsumoProgramacion
from .models import Accion, CentroCosto, Correlativo, Direccion, FuenteFinanciamiento, Insumo, InsumoProgramacion, Meta, MetaFisica, Periodo, Producto, ProductoDireccion
from .models import Programa, ProgramacionAnual, Renglon, Resultados, SubProducto, UnidadMedida

class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = '__all__'


class ProgramacionAnualSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramacionAnual
        fields = '__all__'


class RenglonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renglon
        fields = '__all__'


class SubProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProducto
        fields = '__all__'


class UnidadMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadMedida
        fields = '__all__'
        
class AccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accion
        fields = '__all__'


class CentroCostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroCosto
        fields = '__all__'


class CorrelativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correlativo
        fields = '__all__'


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'


class FuenteFinanciamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuenteFinanciamiento
        fields = '__all__'


class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = '__all__'


class InsumoProgramacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsumoProgramacion
        fields = '__all__'


class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meta
        fields = '__all__'


class MetaFisicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaFisica
        fields = '__all__'


class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class ProductoDireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoDireccion
        fields = '__all__'

class AccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accion
        fields = '__all__'


class CentroCostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroCosto
        fields = '__all__'


class CorrelativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correlativo
        fields = '__all__'


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'


class FuenteFinanciamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuenteFinanciamiento
        fields = '__all__'


class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = '__all__'


class InsumoProgramacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsumoProgramacion
        fields = '__all__'
 
 
class SubProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProducto
        fields = '__all__'
 
 
 
        
class ProductoSerializer(serializers.ModelSerializer):
    filtered_subproductos = SubProductoSerializer(many=True, read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'  # lista los campos que deseas exponer en la API


class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'
        
class ResultadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultados
        fields = '__all__'
        exclude = []
        read_only_fields = ['spoares_id']
        extra_kwargs = {
            'spoares_dependede': {'required': False, 'allow_blank': True},
            'spoares_insert': {'required': False, 'allow_blank': True},
            'spoares_update': {'required': False, 'allow_blank': True},
            'spoares_delete': {'required': False, 'allow_blank': True},
            'spoares_propietario': {'required': False, 'allow_blank': True},
            # Agrega aquí los campos que deseas que no sean obligatorios y sus opciones
        }
        
class ResultadosNivel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Resultados
        fields = '__all__'