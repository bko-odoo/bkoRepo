import { Component, OnInit } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit {

   currentUrl: string = '/';

	constructor(private router: Router) {
		this.router.events
		  .subscribe((event) => {
			if (event instanceof NavigationEnd) {
			  this.currentUrl = event.url
			}
		})
	}


  ngOnInit() {
  }

}
