import { enableProdMode } from '@angular/core';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppModule } from './app/app.module';
import { environment } from './enviroments/enviroment';
import { registerLicense } from '@syncfusion/ej2-base';

// Registering Syncfusion license key
registerLicense('Mgo+DSMBaFt+QHJqVEZrXVNbdV5dVGpAd0N3RGlcdlR1fUUmHVdTRHRcQlthS39Xc0JhXXlXcXc=;Mgo+DSMBPh8sVXJ1S0R+XVFPd11dXmJWd1p/THNYflR1fV9DaUwxOX1dQl9gSXhRdERnXHhcdHNVQ2M=;ORg4AjUWIQA/Gnt2VFhiQlBEfV5AQmBIYVp/TGpJfl96cVxMZVVBJAtUQF1hSn5VdEdiXXpZcnBSRGRf;MjQ5NzI3M0AzMjMxMmUzMDJlMzBuT1h1WG5GQkYvQXdCVS9VaWozMk0xdWtPS2ZEMFVmQVYweHRpWGVaRHBNPQ==;MjQ5NzI3NEAzMjMxMmUzMDJlMzBVU0plUXpMUHRUMm9RVXV6bTZJREtCejVraDNyZW8wTzNEVFptTXg3MDBvPQ==;NRAiBiAaIQQuGjN/V0d+Xk9FdlRDX3xKf0x/TGpQb19xflBPallYVBYiSV9jS31TcEdhWHtbd3ZRTmVUUg==;MjQ5NzI3NkAzMjMxMmUzMDJlMzBmWWIzRHpzZGRrQUVuYjNJcCtkU2x3aG9NTDY0b05NQVFRdS9XdXpBaXJzPQ==;MjQ5NzI3N0AzMjMxMmUzMDJlMzBCR2xLVi81a0JER2wvanBLZnllU0ZWZmErR1Z3MExRL2I3MDBjbFY2dzBJPQ==;Mgo+DSMBMAY9C3t2VFhiQlBEfV5AQmBIYVp/TGpJfl96cVxMZVVBJAtUQF1hSn5VdEdiXXpZcnBcQ2ZU;MjQ5NzI3OUAzMjMxMmUzMDJlMzBuVE1scVVDVGoyMmt2YWtKTTVuelBrVDFBaU82UG1CQkpLeGJMMjJsc1BBPQ==;MjQ5NzI4MEAzMjMxMmUzMDJlMzBsWE5QcU9wMkRBUXV3T0ZPSXNISDhZMHJ1UEtFbDZMcHZkRy8vZDg0eGFjPQ==;MjQ5NzI4MUAzMjMxMmUzMDJlMzBmWWIzRHpzZGRrQUVuYjNJcCtkU2x3aG9NTDY0b05NQVFRdS9XdXpBaXJzPQ==');

if (environment.production) {
  enableProdMode();
}

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));
