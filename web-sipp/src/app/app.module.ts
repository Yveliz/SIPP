import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormulacionComponent } from './formulacion/formulacion.component';
import { SidebarComponent } from './sidebar/sidebar.component';

import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';

import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { ProductoService } from './services/producto.service'; // Importa el ProductoService
import { ResultadosService } from './services/resultadosf.service'; // Importa el ProductoService

import { MatExpansionModule } from '@angular/material/expansion';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ReactiveFormsModule } from '@angular/forms';
import { DialogModule } from '@syncfusion/ej2-angular-popups';

import { MatTableModule } from '@angular/material/table';

import { GridModule,GridAllModule, EditService, ToolbarService } from '@syncfusion/ej2-angular-grids';
import { PageService, SortService, FilterService, GroupService, DetailRowService } from '@syncfusion/ej2-angular-grids';
import { ToolbarModule } from '@syncfusion/ej2-angular-navigations';

import { ResultadosFinalesComponent } from './resultados-finales/resultados-finales.component';
import { ResultadosIntComponent } from './resultados-int/resultados-int.component';
import { ResultadosInmComponent } from './resultados-inm/resultados-inm.component';
import { SidebarsuperiorComponent } from './sidebarsuperior/sidebarsuperior.component';


library.add(fas);

@NgModule({
  declarations: [
    AppComponent,
    FormulacionComponent,
    SidebarComponent,
    ResultadosFinalesComponent,
    ResultadosIntComponent,
    ResultadosInmComponent,
    SidebarsuperiorComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FontAwesomeModule,
    ReactiveFormsModule,
    ToolbarModule,
    DialogModule,
    
    GridModule,
    GridAllModule,

    MatTableModule,

    MatExpansionModule,
    BrowserAnimationsModule,

    FormsModule
    
  ],
  providers: [
    SortService,
    FilterService,
    GroupService,
    PageService,
    DetailRowService,
    EditService, 
    ToolbarService,
    ProductoService, // Agrega el ProductoService como proveedor
    ResultadosService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
