import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FormulacionComponent } from './formulacion/formulacion.component';
import { ResultadosFinalesComponent } from './resultados-finales/resultados-finales.component';
import { ResultadosIntComponent} from './resultados-int/resultados-int.component';
import {ResultadosInmComponent} from './resultados-inm/resultados-inm.component'
const routes: Routes = [
  { path: 'formulacion', component: FormulacionComponent },
  { path: 'resultadosf', component: ResultadosFinalesComponent},
  { path: 'resultadosi', component: ResultadosIntComponent},
  { path: 'resultadosinm', component: ResultadosInmComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
