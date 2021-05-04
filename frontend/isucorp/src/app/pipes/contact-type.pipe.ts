import { Pipe, PipeTransform } from '@angular/core';
import { ContactType } from '../contact/contact.service';

@Pipe({
  name: 'contact_type'
})
export class ContactTypePipe implements PipeTransform {

  transform(value: string): string {
    switch (value) {
      case "1":
        return 'Contact type 1'
      case "2":
        return 'Contact type 2'
      case "3":
        return 'Contact type 3'
      default:
        return 'Not Defined'
    }
  }

}
