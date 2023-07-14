import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class ProductoService {
  private apiUrl = 'http://localhost:3000'; // cambia esto por la URL de tu API

  
  constructor(private http: HttpClient) {}

  obtenerProductosPorDireccion(direccion: string, anio: string,etapa:string) {
    const url = `http://127.0.0.1:8000/planificacion/api/productos_por_direccion/?spodir_id=${direccion}&spopro_anio=${anio}&spopro_tipo=${etapa}`; // Agregar spodir_id a la URL
    return this.http.get(url); // Usa el método GET
  }
  
  obtenerUnidadMedida(){
    const url = `http://127.0.0.1:8000/planificacion/api/unidades-medida/`; // Agregar spodir_id a la URL
    return this.http.get(url); // Usa el método GET
  }
  obtenerDirecciones(){
    const url = `http://127.0.0.1:8000/planificacion/api/direcciones/`; // Agregar spodir_id a la URL
    return this.http.get(url); // Usa el método GET
  }
  obtenerPeriodos(){
    const url = `http://127.0.0.1:8000/planificacion/api/periodos/`; // Agregar spodir_id a la URL
    return this.http.get(url); // Usa el método GET
  }

  addMeta(meta: any) {
    return this.http.post(`${this.apiUrl}/metas`, meta);
  }

  updateMeta(meta: any) {
    return this.http.put(`${this.apiUrl}/metas/${meta.id}`, meta);
  }

  deleteMeta(id: number) {
    return this.http.delete(`${this.apiUrl}/metas/${id}`);
  }
}

