import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ContactModule } from './contact/contact.module';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './material.module';
import { NavMenuComponent } from './nav-menu/nav-menu.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    NavMenuComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ContactModule,
    BrowserAnimationsModule,
    MaterialModule,
  ],
  exports: [ MaterialModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
