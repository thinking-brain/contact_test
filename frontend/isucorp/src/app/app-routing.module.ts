import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ContactListComponent } from './contact/contact-list/contact-list.component';
import { EditContactComponent } from './contact/edit-contact/edit-contact.component';
import { NewContactComponent } from './contact/new-contact/new-contact.component';

const routes: Routes = [
  { path: '', component: ContactListComponent, pathMatch:'full' },
  { path: 'contacts', component: ContactListComponent },
  { path: 'contact/create', component: NewContactComponent },
  { path: 'contact/edit', component: EditContactComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
