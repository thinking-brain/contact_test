import { Component, Inject, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSnackBar } from '@angular/material/snack-bar';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';
import { Contact, ContactService } from '../contact.service';


@Component({
  selector: 'confirm-delete-dialog',
  templateUrl: 'confirm-delete-dialog.html',
  styleUrls: ['confirm-delete-dialog.css'],
})
export class ConfirmDeleteDialog {

  constructor(
    public dialogRef: MatDialogRef<ConfirmDeleteDialog>,
    @Inject(MAT_DIALOG_DATA) public data: Contact) { }

  onNoClick(): void {
    this.dialogRef.close();
  }
  confirm(): void {
    this.dialogRef.close(true);
  }
}

@Component({
  selector: 'app-contact-list',
  templateUrl: './contact-list.component.html',
  styleUrls: ['./contact-list.component.scss']
})
export class ContactListComponent implements OnInit, AfterViewInit {
  @ViewChild(MatPaginator, { static: false }) paginator: MatPaginator;
  @ViewChild(MatSort, { static: false }) sort: MatSort;
  dataSource: MatTableDataSource<Contact>;

  displayedColumns: string[] = ['name','birthdate', 'phone','contact_type', 'actions'];

  constructor(private contactServ: ContactService,
    private router: Router, private snackBar: MatSnackBar, public dialog: MatDialog) {
    contactServ.List().subscribe(r => {
      this.dataSource = new MatTableDataSource<Contact>(r);
      this.dataSource.paginator = this.paginator;
    });
  }

  ngOnInit() {
  }

  ngAfterViewInit() {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }

  edit(contact: Contact) {
    this.contactServ.current = contact;
    this.router.navigate(['/contact/edit'])
  }

  delete(contact: Contact) {
    const dialogRef = this.dialog.open(ConfirmDeleteDialog, {
      width: '40%',
      data: contact
    });

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        this.contactServ.Delete(contact).subscribe(r => {
          if (r) {
            this.contactServ.List().subscribe(r => {
              this.dataSource = new MatTableDataSource<Contact>(r);
              this.dataSource.paginator = this.paginator;
            });
            this.snackBar.open('Contact DELETED.', 'Cerrar', { duration: 3000 });
          } else {
            this.snackBar.open('Error Deleting Contact.', 'Cerrar', { duration: 3000 });
          }
        });
      }
    });
  }
}
