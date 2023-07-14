// date-format.service.ts

import { Injectable } from '@angular/core';
import { format } from 'date-fns';

@Injectable({
  providedIn: 'root',
})
export class DateFormatService {
  constructor() {}

  formatDate(date: Date, formatString: string): string {
    return format(date, formatString);
  }
}
