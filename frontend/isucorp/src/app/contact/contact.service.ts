import { Inject, Injectable, LOCALE_ID } from '@angular/core';
import { from, Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import {formatDate} from '@angular/common';

export enum ContactType{
  ContactType1 = "1",
  ContactType2 = "2",
  ContactType3 = "3",
}

export interface Contact {
  id: number
  name: string
  birthdate: Date,
  contact_type: ContactType
  phone: string
  description: string
}
@Injectable({
  providedIn: 'root'
})
export class ContactService {
  current : Contact
  url: string = 'http://127.0.0.1:5000/contact/';

  constructor(private http: HttpClient, @Inject(LOCALE_ID) private locale: string) { }

  Get(id: number): Observable<Contact>{
    let url = this.url + id;
    return this.http.get<Contact>(url).pipe(map(result => {
      return result;
    }));
  }

  List(): Observable<Contact[]>{
    return this.http.get<Contact[]>(this.url).pipe(map(result => {
      let contacts : Contact[];
      contacts = [];
      for (const item of result) {
        contacts.push(item)
      }
      return contacts;
    }));
  }

  Create(contact: Contact): Observable<boolean>{
    let data = {
      'name': contact.name,
      'birthdate': formatDate(contact.birthdate,'yyyy-MM-dd',this.locale),
      'contact_type': contact.contact_type
    }
    if (contact.description != null && contact.description != undefined) {
      data['description'] = contact.description;
    }
    if (contact.phone != null && contact.phone != undefined) {
      data['phone'] = contact.phone;
    }
    return this.http.post<any>(this.url, data).pipe(map(result => {
      if (result.status == true) {
        return true;
      }
      return false;
    }));
  }

  Update(contact: Contact): Observable<boolean>{
    if (contact.id != null || contact.id != undefined) {
      let data = {
        'name': contact.name,
        'birthdate': formatDate(contact.birthdate,'yyyy-MM-dd',this.locale),
        'contact_type': contact.contact_type
      }
      if (contact.description != null && contact.description != undefined) {
        data['description'] = contact.description;
      }
      if (contact.phone != null && contact.phone != undefined) {
        data['phone'] = contact.phone;
      }
      let url = this.url + contact.id;
      return this.http.put<any>(url, data).pipe(map(result => {
        if (result.status == true) {
          return true;
        }
        return false;
      }));
    }
    return from([false]);
  }

  Delete(contact: Contact): Observable<boolean>{
    if (contact.id != null || contact.id != undefined) {
      let url = this.url + contact.id;
      return this.http.delete<any>(url).pipe(map(result => {
        if (result.status == true) {
          return true;
        }
        return false;
      }));
    }
    return from([false]);
  }
}
