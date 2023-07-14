import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ResultadosFinalesComponent } from './resultados-finales.component';

describe('ResultadosFinalesComponent', () => {
  let component: ResultadosFinalesComponent;
  let fixture: ComponentFixture<ResultadosFinalesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ResultadosFinalesComponent]
    });
    fixture = TestBed.createComponent(ResultadosFinalesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
