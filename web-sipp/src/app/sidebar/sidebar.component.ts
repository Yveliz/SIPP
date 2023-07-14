import { Component, OnInit } from '@angular/core';
import { faList, faFile, faRightFromBracket,faAngleDown,faAngleRight } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {
  faList = faList;
  faFile = faFile;
  faRightBracket = faRightFromBracket;
  faAngleDown= faAngleDown;
  faAngleRight = faAngleRight;
  
  collapsed: boolean = false;
  subMenuStates: { [key: string]: boolean } = {};

  ngOnInit() {
    this.sidebarCollapse();
    this.initializeSubMenuStates();
  }

  sidebarCollapse() {
    this.collapsed = !this.collapsed;
  
    // Si la barra lateral se colapsa, contraer todos los submenús
    if (this.collapsed) {
      for (let key in this.subMenuStates) {
        this.subMenuStates[key] = false;
      }
    }
  }
  

  toggleSubMenu(subMenuId: string) {
    if (this.collapsed) {
      this.collapsed = false;
    }
    this.subMenuStates[subMenuId] = !this.subMenuStates[subMenuId];
    console.log(subMenuId)
    console.log(this.subMenuStates['submenu1'])
  }
  

  isSubMenuOpen(subMenuId: string): boolean {
    return this.subMenuStates[subMenuId];
  }

  private initializeSubMenuStates() {
    this.subMenuStates['submenu1'] = false;
    this.subMenuStates['submenu2'] = false;
  }
}
