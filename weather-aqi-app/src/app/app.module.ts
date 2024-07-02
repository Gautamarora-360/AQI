import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatInputModule, MatButtonModule, MatCardModule, MatToolbarModule } from '@angular/material';

import { AppComponent } from './app.component';
import { WeatherComponent } from './weather/weather.component';
import { AqiComponent } from './aqi/aqi.component';
import { WeatherService } from './weather.service';
import { AqiService } from './aqi.service';

@NgModule({
  declarations: [
    AppComponent,
    WeatherComponent,
    AqiComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatInputModule,
    MatButtonModule,
    MatCardModule,
    MatToolbarModule
  ],
  providers: [WeatherService, AqiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
