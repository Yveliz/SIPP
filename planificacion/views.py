from planificacion.models import Producto, Accion

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer
from .serializers import DireccionSerializer, PeriodoSerializer
from rest_framework import viewsets
from .models import Accion, CentroCosto, Correlativo, Direccion, FuenteFinanciamiento, Insumo, InsumoProgramacion
from .serializers import AccionSerializer, CentroCostoSerializer, CorrelativoSerializer, DireccionSerializer, FuenteFinanciamientoSerializer, InsumoSerializer, InsumoProgramacionSerializer
from .models import Accion, CentroCosto, Correlativo, Direccion, FuenteFinanciamiento, Insumo, InsumoProgramacion, Meta, MetaFisica, Periodo, Producto, ProductoDireccion
from .serializers import AccionSerializer, CentroCostoSerializer, CorrelativoSerializer, DireccionSerializer, FuenteFinanciamientoSerializer, InsumoSerializer, InsumoProgramacionSerializer, MetaSerializer, MetaFisicaSerializer, PeriodoSerializer, ProductoSerializer, ProductoDireccionSerializer
from .models import Programa, ProgramacionAnual, Renglon, Resultados, SubProducto, UnidadMedida
from .serializers import ProgramaSerializer, ProgramacionAnualSerializer, RenglonSerializer, ResultadosSerializer, SubProductoSerializer, UnidadMedidaSerializer
from .serializers import ResultadosSerializer, ResultadosNivel2Serializer
from django.shortcuts import render


class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer


class ProgramacionAnualViewSet(viewsets.ModelViewSet):
    queryset = ProgramacionAnual.objects.all()
    serializer_class = ProgramacionAnualSerializer


class RenglonViewSet(viewsets.ModelViewSet):
    queryset = Renglon.objects.all()
    serializer_class = RenglonSerializer


class ResultadosViewSet(viewsets.ModelViewSet):
    queryset = Resultados.objects.all()
    serializer_class = ResultadosSerializer


class SubProductoViewSet(viewsets.ModelViewSet):
    queryset = SubProducto.objects.all()
    serializer_class = SubProductoSerializer


class UnidadMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadMedida.objects.all()
    serializer_class = UnidadMedidaSerializer
    
class AccionViewSet(viewsets.ModelViewSet):
    queryset = Accion.objects.all()
    serializer_class = AccionSerializer


class CentroCostoViewSet(viewsets.ModelViewSet):
    queryset = CentroCosto.objects.all()
    serializer_class = CentroCostoSerializer


class CorrelativoViewSet(viewsets.ModelViewSet):
    queryset = Correlativo.objects.all()
    serializer_class = CorrelativoSerializer


class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer


class FuenteFinanciamientoViewSet(viewsets.ModelViewSet):
    queryset = FuenteFinanciamiento.objects.all()
    serializer_class = FuenteFinanciamientoSerializer


class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer


class InsumoProgramacionViewSet(viewsets.ModelViewSet):
    queryset = InsumoProgramacion.objects.all()
    serializer_class = InsumoProgramacionSerializer


class MetaViewSet(viewsets.ModelViewSet):
    queryset = Meta.objects.all()
    serializer_class = MetaSerializer


class MetaFisicaViewSet(viewsets.ModelViewSet):
    queryset = MetaFisica.objects.all()
    serializer_class = MetaFisicaSerializer


class PeriodoViewSet(viewsets.ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoDireccionViewSet(viewsets.ModelViewSet):
    queryset = ProductoDireccion.objects.all()
    serializer_class = ProductoDireccionSerializer

class AccionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Accion.objects.all()
    serializer_class = AccionSerializer


class CentroCostoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CentroCosto.objects.all()
    serializer_class = CentroCostoSerializer


class CorrelativoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Correlativo.objects.all()
    serializer_class = CorrelativoSerializer


class DireccionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer


class FuenteFinanciamientoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FuenteFinanciamiento.objects.all()
    serializer_class = FuenteFinanciamientoSerializer


class InsumoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer


class InsumoProgramacionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InsumoProgramacion.objects.all()
    serializer_class = InsumoProgramacionSerializer


class ProductoList(APIView):
    def get(self, request, format=None):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

class DireccionListAPIView(ListAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class PeriodoListAPIView(ListAPIView):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer
    


from django.shortcuts import render
from .models import Producto, ProductoDireccion, Resultados
from .serializers import ProductoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class ProductoPorDireccionList(APIView):
    def get(self, request):
        dir = request.GET.get('spodir_id', None) #direccion de los parámetros
        anio = request.GET.get('spopro_anio', None) # anio de los parámetros
        etapa = request.GET.get('spopro_tipo', None) # etapa de los parámetros
        
        
        if dir: # Si spodir_id está presente
            producto_direcciones = ProductoDireccion.objects.filter(spodir_id=dir)
            ids = [pd.spospro_id for pd in producto_direcciones]
            spospro_ids = [int(str(pd.spospro_id).split(".")[0]) for pd in producto_direcciones]
            
            # Todos los productos que no son restrictivos
            todos_los_productos = Producto.objects.filter(spopro_restrictiva='N', spopro_anio = anio, spopro_tipo = etapa) 
            
            
            # Filtrar los productos en Python en lugar de hacerlo en la base de datos
            productos = [producto for producto in todos_los_productos if int(str(producto.spopro_id).split(".")[0]) in spospro_ids]
            
            # Lista para guardar la información del producto junto con sus subproductos
            product_data = []
            
            for producto in productos:
                # Filtrar los subproductos en base al id del producto
                subproductos = producto.subproductos.filter(spospro_id__in=ids, spospr_restriciva='N')

                # Serializar el producto, luego se añade a la lista
                serializer = ProductoSerializer(producto)
                product_dict = serializer.data
                product_dict['subproductos'] = []

                for subproducto in subproductos:
                    # Obtener las metas correspondientes a los subproductos
                    metas = subproducto.metas.filter(spospro_id=subproducto.spospro_id, spomta_restrictiva='N', spomta_iddir=dir)  

                    # Serializar el subproducto y metas, luego se añade a la lista
                    subproduct_serializer = SubProductoSerializer(subproducto)
                    subproduct_dict = subproduct_serializer.data
                    subproduct_dict['metas'] = []

                    for meta in metas:
                        # Obtener las acciones correspondientes a las metas
                        acciones = meta.acciones.filter(spomta_id=meta.spomta_id, spoacn_restrictiva='N', spomta_corr=meta.spomta_corr)

                        # Serializar la meta y acciones, luego se añade a la lista
                        meta_serializer = MetaSerializer(meta)
                        meta_dict = meta_serializer.data
                        meta_dict['acciones'] = AccionSerializer(acciones, many=True).data
                        subproduct_dict['metas'].append(meta_dict)

                    product_dict['subproductos'].append(subproduct_dict)
                
                product_data.append(product_dict) 
            
            print("producto query: ",product_data) 
        else: # Si spodir_id no está presente
            productos = Producto.objects.filter(spopro_restrictiva='N') # Obtiene todos los productos que no son restrictivos
            serializer = ProductoSerializer(productos, many=True)
            product_data = serializer.data
        serializer = ProductoSerializer(productos, many=True)
        return Response(product_data)
    
    def post(self, request):
        # Lógica para crear un nuevo producto por dirección
        # ...
        return Response(status=201)
    
    