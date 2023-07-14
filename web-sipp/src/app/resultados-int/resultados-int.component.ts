import { Component } from '@angular/core';
import { ResultadosService } from '../services/resultadosf.service';
import { PageSettingsModel } from '@syncfusion/ej2-angular-grids';

@Component({
  selector: 'app-metas-int',
  templateUrl: './resultados-int.component.html',
  styleUrls: ['./resultados-int.component.css']
})
export class ResultadosIntComponent {
  nombreUsuario: string = '';
  years: number[] = [];
  public resultados: any[] = [];
  selectedYear1: number = 0;
  selectedYear2: number = 0;

  public pageSettings: PageSettingsModel;

  populateYears(): void {
    const startYear = 2023;
    const endYear = 2040;

    for (let year = startYear; year <= endYear; year++) {
      this.years.push(year);
    }
  }

  constructor(private resultadosService: ResultadosService) {
    this.pageSettings = { pageSize: 6 };  // Personaliza el tamaño de página aquí
  }

  ngOnInit() {
    this.populateYears();
    this.selectedYear1 = this.years[0];
    this.selectedYear2 = this.years[0];
    this.actualizarResultados();
  }

  actualizarResultados() {
    this.resultadosService.obtenerResultados(this.selectedYear1.toString(), this.selectedYear2.toString(), "2").subscribe((resultados: any) => {
      this.resultados = resultados;
    });
  }
}
