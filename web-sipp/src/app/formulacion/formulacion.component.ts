import { Component, ViewChild, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ProductoService } from '../services/producto.service';
import { PageSettingsModel, EditSettingsModel, ToolbarItems } from '@syncfusion/ej2-angular-grids';
import { FormGroup, FormControl } from '@angular/forms';
import { forkJoin } from 'rxjs';
import { debounceTime, distinctUntilChanged } from 'rxjs/operators';
import { DialogEditEventArgs } from '@syncfusion/ej2-angular-grids';
import { IEditCell, GridComponent} from '@syncfusion/ej2-angular-grids';

interface Accion {
  // Agrega los campos necesarios aquí para la acción
}

interface Meta {
  spomta_id: string;
  spoudm_id: number;
  spomta_descripcion: string;
  spomta_restrictiva: string;
  spomta_insert: string;
  spomta_propietario: string;
  acciones: Accion[]; // Asume que cada meta tiene una lista de acciones
}

interface Subproducto {
  spospro_id: string;
  spoudm_id: number;
  spospr_descripcion: string;
  spospr_insert: string;
  spospr_propietario: string;
  metas: Meta[]; // Asume que cada subproducto tiene una lista de metas
}

interface Producto {
  spopro_id: string;
  spopro_descripcion: string;
  spoudm_id: number;
  spopro_insert: string;
  spopro_propietario: string;
  subproductos: Subproducto[]; // Asume que cada producto tiene una lista de subproductos
}

@Component({
  selector: 'app-formulacion',
  templateUrl: './formulacion.component.html',
  styleUrls: ['./formulacion.component.scss']
})
export class FormulacionComponent implements OnInit {
  public iddependiente: IEditCell = { params: { readonly: true } };
  public id: IEditCell = { params: { readonly: true } };
  public descripcion?: IEditCell;

  public showDialog = false;
  public selectedRow: Producto | undefined;

  
  selectedSubproducto: any;
  nombreUsuario: string;
  periodos: any[];
  anios: any[];
  direcciones: any[] = [];
  periodoSeleccionado: string;
  productos: any[] = [];
  medidas: any[] = [];
  anioSeleccionado: number;
  formulario = new FormGroup({
    direccion: new FormControl(),
    etapa: new FormControl(),
    anio: new FormControl(),
    periodo: new FormControl()  // Esta línea es nueva
  });

  public pageSettings: PageSettingsModel;

  public toolbar: ToolbarItems[] = ['Add', 'Edit', 'Delete'];
  public editSettings?: EditSettingsModel;
  @ViewChild('grid') grid?: GridComponent;
  @ViewChild('childGrid') childGrid?: GridComponent;
  @ViewChild('childChildGrid') childChildGrid?: GridComponent;  
  @ViewChild('childChildChildGrid') childChildChildGrid?: GridComponent;  

  public validIdDependiente: any = { required: true };
  public validDescripcion: any = { required: true };




  constructor(private http: HttpClient, private productoService: ProductoService) {
    this.nombreUsuario = '';
    this.pageSettings = { pageSize: 6 };
    this.periodos = [];
    this.anios = [];
    this.direcciones = [];
    this.medidas = [];
    this.periodoSeleccionado = '';
    this.anioSeleccionado = 2023;

    this.editSettings = { allowEditing: true, allowAdding: true, allowDeleting: true, mode: 'Dialog' };
    
  }

  formatoPeriodo(inicio: number, final: number): string {
    return `${inicio}-${final}`;
  }
  generarListaAnios(periodoSeleccionado: string) {
    const [inicio, final] = periodoSeleccionado.split('-').map(Number);
    this.anios = Array.from({ length: final - inicio + 1 }, (_, index) => inicio + index);
  }

  ngOnInit(): void {
    this.id = { params: { readonly: true } };
    this.iddependiente = { params: { readonly: true } };
    this.descripcion = { params: { value: '' } };





    forkJoin({
      direcciones: this.productoService.obtenerDirecciones(),
      periodos: this.productoService.obtenerPeriodos(),
      medidas: this.productoService.obtenerUnidadMedida()
    }).subscribe((res: any) => {
      this.direcciones = res.direcciones;
      this.periodos = res.periodos;
      this.medidas = res.medidas;

      if (this.periodos.length > 0) {
        this.periodoSeleccionado = this.formatoPeriodo(this.periodos[0].spoap_inicio, this.periodos[0].spoap_final);
        this.generarListaAnios(this.periodoSeleccionado);
        this.formulario.controls['anio'].setValue(this.anios[0]);  // Establecer el primer año de la lista como valor inicial
        this.formulario.controls['periodo'].setValue(this.periodoSeleccionado);  // Establecer el periodo seleccionado como valor inicial
        this.formulario.controls['direccion'].setValue(this.direcciones[0].adscgdp_id);
        this.formulario.controls['etapa'].setValue('0');
        this.obtenerProductos();
      }
      this.formulario.get('periodo')?.valueChanges.subscribe(periodo => {
        this.generarListaAnios(periodo);
      });
    });

    this.formulario.valueChanges
      .pipe(
        debounceTime(5),
        distinctUntilChanged()
      )
      .subscribe(() => {
        this.obtenerProductos();
      });
  }

  obtenerProductos(): void {
    const { direccion, anio, etapa } = this.formulario.value;

    this.productoService.obtenerProductosPorDireccion(direccion, anio, etapa).subscribe((data: any) => {
      this.productos = data;
    });
  }

  obtenerUnidadMedidas(): void {
    this.productoService.obtenerUnidadMedida().subscribe((data: any) => {
      this.medidas = data;
    });
  }

  getUnidadMedida(spoudmId: number): any {
    return this.medidas.find(medida => medida.spoudm_id === spoudmId);
  }

  onActionComplete(args: any, level: number): void {
    if (args.requestType === 'beginEdit' || args.requestType === 'add') {
      const dialog = (args as any).dialog;
      dialog.header = (args as any).requestType === 'add' ? 'Agregar resultado' : 'Editar resultado'; 
    }
  }

  onActionBegin(args: any, level: number) {
    console.log(args)
    
    if (args.requestType === 'beginEdit' || args.requestType === 'add') {
      if (level === 3) {
        console.log(this.selectedSubproducto.spospro_id); // para verificar si tienes el id correcto
        const idSubproducto = this.selectedSubproducto.spospro_id;
        if (args.requestType === 'beginEdit' || args.requestType === 'add') {
          args.rowData['spospro_id'] = idSubproducto;
          console.log(idSubproducto);
        }
      }

      let meta = args.data;
      let idSubproducto = this.selectedSubproducto.spospro_id; // id del subproducto seleccionado

    }
  }


  rowSelectedSubproducto(args: any): void {
    this.selectedSubproducto = args.data;
  }
}
