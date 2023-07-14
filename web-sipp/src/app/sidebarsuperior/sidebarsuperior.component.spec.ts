import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SidebarsuperiorComponent } from './sidebarsuperior.component';

describe('SidebarsuperiorComponent', () => {
  let component: SidebarsuperiorComponent;
  let fixture: ComponentFixture<SidebarsuperiorComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SidebarsuperiorComponent]
    });
    fixture = TestBed.createComponent(SidebarsuperiorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
