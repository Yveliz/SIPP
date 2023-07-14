from django.db import models
from datetime import datetime
from planificacion.choices import gender_choices
from django.db import models
from treebeard.mp_tree import MP_Node
import uuid




class CentroCosto(models.Model):
    spocco_id = models.IntegerField(primary_key=True)
    spocco_descripcion = models.CharField(max_length=200, null=True)
    spocco_estado = models.CharField(max_length=3, null=True)
    spocco_restrictiva = models.CharField(max_length=3, default='N')

    class Meta:
        db_table = '"SCHE$POANTE". "spoatbl_centro_costo"'
        managed = False


class Correlativo(models.Model):
    adscgdp_id = models.IntegerField(primary_key=True)
    spocor_correlativo = models.IntegerField()
    spocor_restrictiva = models.CharField(max_length=3, default='N')
    spocor_anio = models.IntegerField()

    class Meta:
        db_table = '"SCHE$POANTE"."spoatbl_correlativo"'
        managed = False


class Direccion(models.Model):
    spodir_id = models.IntegerField(primary_key=True)
    spodir_descripcion = models.CharField(max_length=200)
    spodir_estado = models.CharField(max_length=3)
    spodir_restrictiva = models.CharField(max_length=3, default='N')
    spocco_id = models.IntegerField()
    adscgdp_id = models.IntegerField()
    
    class Meta:
        db_table = '"SCHE$POANTE". "spoatbl_direccion"'
        managed = False
        

class FuenteFinanciamiento(models.Model):
    spoffi_id = models.CharField(primary_key=True, max_length=50)
    spoffi_descripcion = models.CharField(max_length=200)
    spoffi_estado = models.CharField(max_length=3)
    spoffi_restrictiva = models.CharField(max_length=3, default='N')
    spoffi_insert = models.CharField(max_length=100)
    spoffi_update = models.CharField(max_length=100)
    spoffi_delete = models.CharField(max_length=100)
    spoffi_propietario = models.CharField(max_length=45)

    class Meta:
        db_table = '"SCHE$POANTE"."spoatbl_fuente_financiamiento"'
        managed = False


class Insumo(models.Model):
    spoins_id = models.CharField(primary_key=True, max_length=30)
    spoins_descripcion = models.CharField(max_length=400)
    spoins_codigo = models.CharField(max_length=30)
    spoins_restrictiva = models.CharField(max_length=3, default='N')

    class Meta:
        db_table = '"SCHE$POANTE"."spoatbl_insumo"'
        managed = False
        

class InsumoProgramacion(models.Model):
    spoins_id = models.CharField(max_length=30, primary_key=True)
    spoprm_id = models.IntegerField()
    spoinsp_cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    spoinsp_precio_unit = models.DecimalField(max_digits=18, decimal_places=5, null=True)
    spoinsp_estado = models.CharField(max_length=3)
    spoinsp_restrictiva = models.CharField(max_length=3, default='N')
    spoudm_id = models.IntegerField(null=True)
    spoinsp_mes = models.IntegerField()
    spoinsp_insert = models.CharField(max_length=100)
    spoinsp_update = models.CharField(max_length=100)
    spoinsp_delete = models.CharField(max_length=100)
    spoinsp_propietario = models.CharField(max_length=100)

    class Meta:
        db_table = '"SCHE$POANTE". "spoatbl_insumo_programacion"'
        managed = False
        unique_together = [['spoins_id', 'spoprm_id']]







class MetaFisica(models.Model):
    spomf_id = models.CharField(primary_key=True, max_length=30)
    spomf_mes = models.IntegerField()
    spomf_anio = models.IntegerField()
    spomf_estado = models.CharField(max_length=3)
    spomf_nivel = models.IntegerField()
    spomf_restrictiva = models.CharField(max_length=3, default='N')
    spomf_metafisica = models.IntegerField(default=0)
    spomf_iddir = models.IntegerField()
    spomf_corr = models.IntegerField()
    spomf_insert = models.CharField(max_length=150)
    spomf_delete = models.CharField(max_length=150)
    spomf_update = models.CharField(max_length=150)
    spomf_propietario = models.CharField(max_length=45)
    spomf_periodo = models.IntegerField(default=0)
    spomf_tipo = models.IntegerField(default=0)
    spomf_suma = models.CharField(max_length=35)
    spoacn_corr = models.CharField(max_length=35)

    class Meta:
        db_table = '"SCHE$POANTE"."spoatbl_metafisica"'
        managed = False
        

class Periodo(models.Model):
    spoap_id = models.IntegerField(primary_key=True)
    spoap_inicio = models.IntegerField()
    spoap_final = models.IntegerField()
    spoap_restrictiva = models.CharField(max_length=2, default='N')
    spoap_orden = models.IntegerField()
    spoap_vigente = models.IntegerField(default=0)

    class Meta:
        db_table = '"SCHE$POANTE"."spoatbl_periodo"'
        managed = False



        



class Programa(models.Model):
    programa = models.CharField(max_length=20)
    subprograma = models.CharField(max_length=2)
    proyecto = models.CharField(max_length=20)
    actividad = models.CharField(max_length=20)
    obra = models.CharField(max_length=20)
    siges = models.CharField(max_length=20, primary_key=True)
    codigo_snip = models.CharField(max_length=20)

    class Meta:
        db_table = '"SCHE$POANTE"."spoatbl_programa"'
        managed = False


class ProgramacionAnual(models.Model):
    spoprm_id = models.IntegerField(primary_key=True)
    spoffi_id = models.CharField(max_length=50)
    sporng_id = models.CharField(max_length=50)
    spodir_id = models.IntegerField()
    spoacn_id = models.CharField(max_length=30)
    spoprm_estado = models.CharField(max_length=3)
    spopra_mes = models.IntegerField(null=True)
    spopra_restrictiva = models.CharField(max_length=3, default='N')
    spopra_anio = models.IntegerField()
    spopra_insumo = models.IntegerField(null=True)
    spopra_presentacion = models.IntegerField(null=True)
    spoacn_corr = models.IntegerField(null=True)
    spoprm_insdesc = models.CharField(max_length=200)
    spoprm_udmins = models.IntegerField()
    spoprm_insert = models.CharField(max_length=100)
    spoprm_update = models.CharField(max_length=100)
    spoprm_delete = models.CharField(max_length=100)
    spoprm_propietario = models.CharField(max_length=45)
    spoprm_preciounitario = models.IntegerField()
    spoprm_cantidad = models.IntegerField()

    class Meta:
        db_table = '"SCHE$POANTE"."spoatbl_programacion_anual"'
        managed = False


class Renglon(models.Model):
    sporng_id = models.CharField(max_length=50, primary_key=True)
    sporng_descripcion = models.CharField(max_length=250)
    sporng_estado = models.CharField(max_length=3)
    sporng_restricitva = models.CharField(max_length=3, default='N')

    class Meta:
        db_table = '"SCHE$POANTE"."spoatbl_renglon"'
        managed = False


class Resultados(models.Model):
    spoares_id = models.AutoField(primary_key=True)
    spoares_descripcion = models.CharField(max_length=500)
    spoares_nivel = models.IntegerField()
    spoares_restrictiva = models.CharField(max_length=2, default='N')
    spoares_vigencia_inicio = models.IntegerField()
    spoares_finalizacion = models.IntegerField()
    spoares_dependede = models.IntegerField(null=True)
    spoares_insert = models.CharField(max_length=100)
    spoares_update = models.CharField(max_length=100)
    spoares_delete = models.CharField(max_length=100)
    spoares_propietario = models.CharField(max_length=45)

    class Meta:
        db_table = '"SCHE$POANTE"."spoatbl_resultados"'
        managed = False






class UnidadMedida(models.Model):
    spoudm_id = models.IntegerField(primary_key=True)
    spoudm_descripcion = models.CharField(max_length=200)
    spoudm_restrictiva = models.CharField(max_length=3, default='N')
    spoudm_sinip = models.IntegerField()
    spoudm_siglas = models.CharField(max_length=200)
    spoudm_insert = models.CharField(max_length=100)
    spoudm_update = models.CharField(max_length=100)
    spoudm_delete = models.CharField(max_length=100)
    spoudm_propietario = models.CharField(max_length=45)

    class Meta:
        db_table = '"SCHE$POANTE"."spoatbl_unidad_medida"'
        managed = False


class Producto(models.Model):
    #spopro_id = models.CharField(max_length=30, primary_key=True)
    spopro_id = models.CharField(max_length=30, primary_key=True)
    spopro_descripcion = models.CharField(max_length=500, null=True)
    spoudm_id = models.IntegerField()
    spopro_codigo = models.CharField(max_length=50)
    #spopro_descripcion = models.CharField(max_length=500, null=True)
    spopro_estado = models.CharField(max_length=3)
    spopro_restrictiva = models.CharField(max_length=3, default='N')
    spopro_anio = models.IntegerField()
    spopro_corr = models.DecimalField(max_digits=10, decimal_places=0)
    spopro_insert = models.CharField(max_length=100)
    spopro_update = models.CharField(max_length=100)
    spopro_delete = models.CharField(max_length=100)
    spopro_propietario = models.CharField(max_length=45)
    spopro_periodo = models.IntegerField(default=0)
    spopro_tipo = models.IntegerField(default=0)
    spopro_orden = models.IntegerField(null=True)

    class Meta:
        managed = False
        db_table = '"SCHE$POANTE". "spoatbl_producto"'



class ProductoDireccion(models.Model):
    spodir_id = models.IntegerField()
    spospro_id = models.CharField(max_length=30)
    spospro_codigo = models.CharField(max_length=50)
    spospro_corr = models.IntegerField()
    spospro_anio = models.IntegerField()
    spopd_restrictiva = models.CharField(max_length=3, default='N')
    spopd_insert = models.CharField(max_length=100)
    spopd_update = models.CharField(max_length=100)
    spopd_delete = models.CharField(max_length=100)
    spopd_propietario = models.CharField(max_length=45)
    spopd_id = models.CharField(max_length=30, primary_key=True)

    class Meta:
        db_table = '"SCHE$POANTE"."spoatbl_productodireccion"'
        managed = False
        unique_together = [("spodir_id", "spospro_id", "spospro_codigo", "spospro_corr", "spospro_anio")]


class SubProducto(models.Model):
    spospro_id = models.CharField(max_length=30, primary_key=True)
    spopro_id = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='spopro_id', related_name='subproductos')
    spoudm_id = models.IntegerField()
    spospr_codigo = models.CharField(max_length=50)
    spospr_descripcion = models.CharField(max_length=500, null=True)
    spospr_estado = models.CharField(max_length=3)
    spospr_restriciva = models.CharField(max_length=3, default='N')
    spopro_codigo = models.CharField(max_length=50)
    spopro_anio = models.IntegerField()
    spospro_corr = models.IntegerField()
    spopro_corr = models.IntegerField()
    spopro_orden = models.IntegerField(null=True)
    spospro_insert = models.CharField(max_length=100)
    spospro_update = models.CharField(max_length=100)
    spospro_delete = models.CharField(max_length=100)
    spospro_propietario = models.CharField(max_length=45)

    class Meta:
        db_table = '"SCHE$POANTE"."spoatbl_subproducto"'
        managed = False





class Meta(models.Model):
    spomta_id = models.CharField(max_length=30, primary_key=True)
    spospro_id = models.ForeignKey(SubProducto, on_delete=models.CASCADE, db_column='spospro_id', related_name='metas')
    spoudm_id = models.IntegerField()
    spomta_codigo = models.CharField(max_length=50, null=True)
    spomta_descripcion = models.CharField(max_length=500, null=True)
    spomta_estado = models.CharField(max_length=3, null=True)
    spomta_restrictiva = models.CharField(max_length=3, default='N')
    spomta_iddir = models.IntegerField()
    spospr_codigo = models.CharField(max_length=50)
    spomta_anio = models.IntegerField(null=True)
    spomta_corr = models.IntegerField()
    spospro_corr = models.IntegerField(null=True)
    spomta_orden = models.IntegerField(null=True)
    spomta_insert = models.CharField(max_length=100, null=True)
    spomta_update = models.CharField(max_length=100, null=True)
    spomta_delete = models.CharField(max_length=100, null=True)
    spomta_propietario = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = '"SCHE$POANTE"."spoatbl_meta"'
        
        
class Accion(models.Model):
    spoacn_id = models.CharField(max_length=30, primary_key=True)
    spomta_id = models.ForeignKey(Meta, on_delete=models.CASCADE, db_column='spomta_id', related_name='acciones')
    spoudm_id = models.IntegerField()
    spoacn_codigo = models.CharField(max_length=50, null=True)
    spoacn_descripcion = models.CharField(max_length=500, null=True)
    spoacn_estado = models.CharField(max_length=3, null=True)
    spoacn_restrictiva = models.CharField(max_length=3, default='N')
    spoacn_anio = models.BigIntegerField(null=True)
    spospr_codigo = models.CharField(max_length=50)
    spoacn_corr = models.IntegerField()
    spomta_corr = models.IntegerField(null=True)
    spoacn_orden = models.IntegerField(null=True)
    spoacn_insert = models.CharField(max_length=100, null=True)
    spoacn_update = models.CharField(max_length=100, null=True)
    spoacn_delete = models.CharField(max_length=100, null=True)
    spoacn_propietario = models.CharField(max_length=45, null=True)

    class Meta:
        managed = False
        db_table = '"SCHE$POANTE". "spoatbl_accion"'