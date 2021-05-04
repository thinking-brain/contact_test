import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ContactListComponent, ConfirmDeleteDialog } from './contact-list/contact-list.component';
import { NewContactComponent } from './new-contact/new-contact.component';
import { EditContactComponent } from './edit-contact/edit-contact.component';
import { CKEditorModule } from '@ckeditor/ckeditor5-angular';
import { MaterialModule } from '../material.module';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ContactTypePipe } from "../pipes/contact-type.pipe";


@NgModule({
  declarations: [
    ContactListComponent,
    NewContactComponent,
    EditContactComponent,
    ConfirmDeleteDialog,
    ContactTypePipe
  ],
  imports: [
    CommonModule,
    CKEditorModule,
    MaterialModule,
    RouterModule,
    FormsModule,
    ReactiveFormsModule
  ],
  schemas:  [CUSTOM_ELEMENTS_SCHEMA]
})
export class ContactModule { }
