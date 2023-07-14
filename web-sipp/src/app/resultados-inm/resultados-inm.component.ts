import { Component, ViewChild, OnInit } from '@angular/core';
import { ResultadosService } from '../services/resultadosf.service';
import { DateFormatService } from '../services/date-format.service';
import { ToolbarItems, EditSettingsModel, IEditCell, GridComponent} from '@syncfusion/ej2-angular-grids';
import { L10n } from '@syncfusion/ej2-base';

L10n.load({
  'en-US': {
    grid: {
      'SaveButton': 'Guardar',
      'CancelButton': 'Cancelar',
      'Add': 'Agregar',
      'Edit': 'Editar',
      'Delete': 'Eliminar'
    }
  }
});

interface Resultado {
  spoares_id: number;
  spoares_dependede: number;
}

@Component({
  selector: 'app-resultados-inm',
  templateUrl: './resultados-inm.component.html',
  styleUrls: ['./resultados-inm.component.css']
})
export class ResultadosInmComponent implements OnInit {

  public iddependiente: IEditCell = { params: { readonly: true } };
  public id: IEditCell = { params: { readonly: true } };
  public descripcion?: IEditCell;
  public vigencia: IEditCell = { params: { format: '###.##', value: 2023 } };
  public finalizacion: IEditCell = { params: { format: '###.##', value: 2023 } };
  public showError: boolean = false;
  private hideSpoaresIdColumn: boolean = false;
  nombreUsuario: string = '';
  years: number[] = [];
  public resultados: any[] = [];
  selectedYear1: number = 0;
  selectedYear2: number = 0;
  public toolbar: ToolbarItems[] = ['Add', 'Edit', 'Delete'];
  public editSettings?: EditSettingsModel;
  public showDialog: boolean = false;
  @ViewChild('grid') grid?: GridComponent;
  @ViewChild('childGrid') childGrid?: GridComponent;
  @ViewChild('childChildGrid') childChildGrid?: GridComponent;
  public newId: string = '';
  public newDescripcion: string = '';
  public newAnioVigencia: number = 0;
  public newFinalizacionVigencia: number = 0;
  public currentLevel: number | undefined;
  public selectedRow: Resultado | undefined;
  public validDescripcion: any = { required: true };
  public validVigencia: any = { required: true };
  public validFinalizacion: any = { required: true };
  public validFecha: boolean = false;

  constructor(
    private resultadosService: ResultadosService,
    private dateFormatService: DateFormatService
    ) 
    {
    this.editSettings = { allowEditing: true, allowAdding: true, allowDeleting: true, mode: 'Dialog' };
  }

  ngOnInit() {
    this.id = { params: { readonly: true } };
    this.iddependiente = { params: { readonly: true } };
    this.descripcion = { params: { value: '' } };
    this.vigencia = { params: { format: '###.##', value: 2023 } };
    this.finalizacion = { params: { format: '###.##', value: 2023 } };
    this.populateYears();
    this.selectedYear1 = this.years[0];
    this.selectedYear2 = this.years[0];
    this.actualizarResultados();
    this.validDescripcion = {required: [true, 'Descripción no puede estar vacio']}; 
  }

  populateYears(): void {
    const startYear = 2023;
    const endYear = 2040;
    for (let year = startYear; year <= endYear; year++) {
      this.years.push(year);
    }
  }

  actualizarResultados() {
    this.resultadosService.obtenerResultados(this.selectedYear1.toString(), this.selectedYear2.toString(), "3")
      .subscribe((resultados: any) => {
        this.resultados = resultados;
      });
  }

  onActionComplete(args: any, level: number): void {
    if (args.requestType === 'beginEdit' || args.requestType === 'add') {
      const dialog = (args as any).dialog;
      dialog.header = (args as any).requestType === 'add' ? 'Agregar resultado' : 'Editar resultado'; 
    }
  }

  onActionBegin(args: any, level: number): void {
    let spoaresDependede = this.selectedRow?.spoares_id;
    if (args.requestType === 'beginEdit' || args.requestType === 'add') {
    this.hideSpoaresIdColumn = true;
    this.setIDColumnVisibility(level, !this.hideSpoaresIdColumn);
  } else {
    this.hideSpoaresIdColumn = false;
    this.setIDColumnVisibility(level, !this.hideSpoaresIdColumn);
  }
    
    if (args.requestType === 'save') {
      if(args.action === 'add'){
        this.saveData(args, level, spoaresDependede);
      }else if (args.action === 'edit'){
        this.editData(args, level, spoaresDependede);
      }         
    } else if (args.requestType === 'cancel') {
      this.cancelDialog();
    }
    if (args.requestType === 'delete'){
      this.deleteData(args);
    }
  }

  saveData(args: any, level: number, iddepend: any): void {
    const data = args.data;
    data['spoares_nivel'] = level;
    data['spoares_dependede'] = iddepend;
    // const username = this.authService.getUsername();
    const now = this.dateFormatService.formatDate(new Date(), 'yyyy-MM-dd HH:mm:ss');
    // data['spoares_update'] = `Update: ${now}, Usuario: ${username}`;
    data['spoares_insert'] = `INSERT: ${now}, Usuario: `;
    if(data.spoares_finalizacion >= data.spoares_vigencia_inicio){
      this.resultadosService.guardarResultados(data).subscribe(
      response => {
        this.actualizarResultados();
      },
      error => {
        this.actualizarResultados();
      }
    );
    this.showDialog = false;
    }else {
      args.cancel = true; // Cancelar la operación de guardado
      alert('El año de inicio de vigencia no puede ser mayor que el de finalización.');
    }
  }

  editData(args: any, level: number, iddepend: any): void {
    const data = args.data;
    delete data.resultados_int;
    data['spoares_nivel'] = level;
    data['spoares_dependede'] = iddepend;
    for (let clave in data) {
      if (data[clave] === "") {
        delete data[clave];
      }
    }
    // const username = this.authService.getUsername();
    const now = this.dateFormatService.formatDate(new Date(), 'yyyy-MM-dd HH:mm:ss');
    // data['spoares_update'] = `Update: ${now}, Usuario: ${username}`;
    data['spoares_update'] = `UPDATE: ${now}, Usuario: `;
    if(data.spoares_finalizacion >= data.spoares_vigencia_inicio) {
      this.resultadosService.actualizarResultados(data.spoares_id,data)
        .subscribe(
          response => {
            this.actualizarResultados();
          },
          error => {
            console.error('Error al actualizar los datos', error);
            this.actualizarResultados();
          }
        );
      this.showDialog = false;
    } else {
      args.cancel = true; // Cancelar la operación de edición
      alert('El año de inicio de vigencia no puede ser mayor que el de finalización.');
    }
  }
  deleteData(args: any){
    let data2, data3;
    const data = args.data;
    const now = this.dateFormatService.formatDate(new Date(), 'yyyy-MM-dd HH:mm:ss');
    if ('resultados_int' in data[0] && Array.isArray(data[0].resultados_int) && data[0].resultados_int.length > 0) {
      data2 = data[0].resultados_int[0];
      if ('resultados_int' in data2 && Array.isArray(data2.resultados_int) && data2.resultados_int.length > 0) {
        data3 = data2.resultados_int[0];
      }
    }
    
    // data['spoares_update'] = `Update: ${now}, Usuario: ${username}`;  
    if(data[0].spoares_id != undefined) {
      data[0].spoares_delete = `DELETE: ${now}, Usuario: `;
      data[0].spoares_restrictiva = 'S'
      delete data.resultados_int;
      if(data2!= undefined){
        data2['spoares_restrictiva'] = 'S'
        data2['spoares_delete'] = `DELETE: ${now}, Usuario: `;
        delete data2.resultados_int;
        this.resultadosService.actualizarResultados(data2.spoares_id, data2) // Usar data2 en lugar de data
        .subscribe(
            response => {
            },
            error => {
                console.error('Error al actualizar los datos', error);
            }
        );
        if(data3 != undefined){
            data3['spoares_restrictiva'] = 'S'
            data3['spoares_delete'] = `DELETE: ${now}, Usuario: `;
            delete data3.resultados_int;
            this.resultadosService.actualizarResultados(data3.spoares_id, data3) // Usar data3 en lugar de data
            .subscribe(
                response => {
                },
                error => {
                    console.error('Error al actualizar los datos', error);
                }
            );                        
        }
    }
      this.resultadosService.actualizarResultados(data[0].spoares_id,data[0])
        .subscribe(
          response => {
          },
          error => {
            console.error('Error al actualizar los datos', error);
          }
        );
    }
  }

  cancelDialog(): void {
    this.newId = '';
    this.newDescripcion = '';
    this.newAnioVigencia = 2023;
    this.newFinalizacionVigencia = 2023;
    this.currentLevel = undefined;
    this.showDialog = false;
  }

  setIDColumnVisibility(level: number, visibility: boolean): void {
    let grid;
    if (this.childGrid && level === 2) {
      grid = this.childGrid;
    } else if (this.childChildGrid && level === 3) {
      grid = this.childChildGrid;
    } else {
      grid = this.grid;
    } 
    for (const col of (grid as any).columns) {
      if (col.field === 'spoares_id') {
        col.visible = visibility;
        break;
      }
    }
  }
}
