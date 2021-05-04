import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';
import * as ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import { Contact, ContactService, ContactType } from '../contact.service';

@Component({
  selector: 'app-edit-contact',
  templateUrl: './edit-contact.component.html',
  styleUrls: ['./edit-contact.component.scss']
})
export class EditContactComponent implements OnInit {
  public Editor = ClassicEditor;
  contact: Contact
  maxDate = new Date()
  nameFC = new FormControl('', [Validators.required]);
  birthdateFC = new FormControl('', [Validators.required]);
  phoneFC = new FormControl('', [Validators.pattern('[- +()0-9]+')]);
  constructor(private contactServ: ContactService, private router: Router,
    private snackBar: MatSnackBar) {
      if (contactServ.current == null || contactServ.current == undefined) {
        snackBar.open('You doesn`t selected any Contact.', 'Close', { duration: 3000 });
        this.router.navigate(['/contacts'])
      }
    this.contact = contactServ.current;
    this.nameFC.setValue(this.contact.name);
    this.phoneFC.setValue(this.contact.phone);
    this.birthdateFC.setValue(this.contact.birthdate);
  }

  ngOnInit() {
  }

  save() {
    if (this.nameFC.valid && this.birthdateFC.valid && this.phoneFC.valid) {
      this.contact.name = this.nameFC.value;
      this.contact.phone = this.phoneFC.value;
      this.contact.birthdate = this.birthdateFC.value;
      this.contactServ.Update(this.contact).subscribe(r => {
        if (r) {
          this.snackBar.open('Contact updated successfully.', 'Close', { duration: 3000 });
        } else {
          this.snackBar.open('Error updating Contact.', 'Close', { duration: 3000 });
        }
      }, err => { }, () => {
        this.contactServ.current = null;
        this.router.navigate(['/contacts'])
      });
    }
  }
}
