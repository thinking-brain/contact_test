import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';
import * as ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import { Contact, ContactService, ContactType } from '../contact.service';

@Component({
  selector: 'app-new-contact',
  templateUrl: './new-contact.component.html',
  styleUrls: ['./new-contact.component.scss']
})
export class NewContactComponent implements OnInit {
  public Editor = ClassicEditor;
  contact: Contact
  maxDate = new Date()
  nameFC = new FormControl('', [Validators.required]);
  birthdateFC = new FormControl('', [Validators.required]);
  phoneFC = new FormControl('', [Validators.pattern('[- +()0-9]+')]);
  constructor(private contactServ: ContactService, private router: Router,
    private snackBar: MatSnackBar) {
      this.contact = {
        contact_type: ContactType.ContactType1
      } as Contact;
  }

  ngOnInit() {
  }

  save(){
    if (this.nameFC.valid && this.birthdateFC.valid && this.phoneFC.valid) {
      this.contact.name = this.nameFC.value;
      this.contact.phone = this.phoneFC.value;
      this.contact.birthdate = this.birthdateFC.value;
      this.contactServ.Create(this.contact).subscribe(r => {
        if (r) {
          this.snackBar.open('Contact created successfully.', 'Close', { duration: 3000 });
        }else{
          this.snackBar.open('Error creating Contact.', 'Close', { duration: 3000 });
        }
      },err => {}, () => {
        this.contactServ.current = null;
        this.router.navigate(['contacts'])
      });
    }
  }
}
