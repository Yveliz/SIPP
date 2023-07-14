import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ResultadosIntComponent } from './resultados-int.component';

describe('ResultadosIntComponent', () => {
  let component: ResultadosIntComponent;
  let fixture: ComponentFixture<ResultadosIntComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ResultadosIntComponent]
    });
    fixture = TestBed.createComponent(ResultadosIntComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
