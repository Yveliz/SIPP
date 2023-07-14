import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ResultadosInmComponent } from './resultados-inm.component';

describe('ResultadosInmComponent', () => {
  let component: ResultadosInmComponent;
  let fixture: ComponentFixture<ResultadosInmComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ResultadosInmComponent]
    });
    fixture = TestBed.createComponent(ResultadosInmComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
