from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework import routers
from .views import AccionViewSet, CentroCostoViewSet, CorrelativoViewSet, DireccionViewSet, FuenteFinanciamientoViewSet, InsumoViewSet, InsumoProgramacionViewSet
from .views import AccionViewSet, CentroCostoViewSet, CorrelativoViewSet, DireccionViewSet, FuenteFinanciamientoViewSet, InsumoViewSet, InsumoProgramacionViewSet, MetaViewSet, MetaFisicaViewSet, PeriodoViewSet, ProductoViewSet, ProductoDireccionViewSet
from .views import ProgramaViewSet, ProgramacionAnualViewSet, RenglonViewSet, ResultadosViewSet, SubProductoViewSet, UnidadMedidaViewSet
from . import views
from . import resultados_views
from rest_framework import viewsets

from .resultados_views import ResultadosAPIView
        
router = routers.DefaultRouter()
router.register('acciones', AccionViewSet)
router.register('centros-costo', CentroCostoViewSet)
router.register('correlativos', CorrelativoViewSet)
router.register('direcciones', DireccionViewSet)
router.register('fuentes-financiamiento', FuenteFinanciamientoViewSet)
router.register('insumos', InsumoViewSet)
router.register('insumos-programacion', InsumoProgramacionViewSet)
router.register('metas', MetaViewSet)
router.register('metas-fisicas', MetaFisicaViewSet)
router.register('periodos', PeriodoViewSet)
router.register('productos', ProductoViewSet)
router.register('productos-direccion', ProductoDireccionViewSet)
router.register('programas', ProgramaViewSet)
router.register('programacion-anual', ProgramacionAnualViewSet)
router.register('renglones', RenglonViewSet)
router.register('resultados', ResultadosViewSet)
router.register('subproductos', SubProductoViewSet)
router.register('unidades-medida', UnidadMedidaViewSet)
router.register('resultados-nivel', resultados_views.ResultadosAPIView, basename='resultados-nivel')

urlpatterns = [
   # path('', prueba, name='prueba'),
    


    #path('api/productos/', ProductoList.as_view(), name='producto-list'),
    #path('api/direcciones/', DireccionListAPIView.as_view(), name='direcciones-list'),
    #path('api/periodos/', PeriodoListAPIView.as_view(), name='periodos-list'),
    path('api/', include(router.urls)),
    path('api/productos_por_direccion/', views.ProductoPorDireccionList.as_view(), name='productos_por_direccion'),
    #path('api/resultados-nivel/', views.ResultadosAPIView.as_view(), name='resultados-finales'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)