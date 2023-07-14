import { Component, OnInit } from '@angular/core';
import { ResultadosService} from '../services/resultadosf.service';

@Component({
  selector: 'app-resultados-finales',
  templateUrl: './resultados-finales.component.html',
  styleUrls: ['./resultados-finales.component.css']
})
export class ResultadosFinalesComponent implements OnInit {
  nombreUsuario: string = '';
  years: number[] = [];
  public resultados: any[] = [];
  selectedYear1: number = 0;
  selectedYear2: number = 0;

 

  populateYears(): void {
    const startYear = 2022;
    const endYear = 2040;

    for (let year = startYear; year <= endYear; year++) {
      this.years.push(year);
    }
  }

  constructor(private resultadosService: ResultadosService) { }

  ngOnInit() {
    this.populateYears();
    this.selectedYear1 = this.years[0];
    this.selectedYear2 = this.years[0];
    this.actualizarResultados();
  }

  actualizarResultados() {
    this.resultadosService.obtenerResultados(this.selectedYear1.toString(), this.selectedYear2.toString(), "1").subscribe((resultados: any) => {
      this.resultados = resultados;
      console.log(resultados)
    });
  }

}
