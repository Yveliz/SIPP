import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ResultadosService {

  private apiUrl = 'http://127.0.0.1:8000/planificacion/api/resultados-nivel/';
  constructor(private http: HttpClient) {}

  obtenerResultados(anioi: string, aniof: string,nivel:string) {
    const url = `http://127.0.0.1:8000/planificacion/api/resultados-nivel/?anioi=${anioi}&aniof=${aniof}&lvl=${nivel}`; // Agregar spodir_id a la URL
    return this.http.get(url); // Usa el método GET
  }

  guardarResultados(datos: any): Observable<any> {
    // Realiza la llamada HTTP POST al endpoint correspondiente en tu API REST
    return this.http.post<any>(this.apiUrl, datos);
  }

  actualizarResultados(id: number, datos: any): Observable<any> {
    for (let clave in datos) {
      if (datos[clave] === '') {
        delete datos[clave] ;
      }
    }
    
    return this.http.put<any>(`${this.apiUrl}${id}/`, datos);
  }
  
}
