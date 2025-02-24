import { Component } from '@angular/core';
import { WeatherService } from '../weather.service';

@Component({
  selector: 'app-weather',
  templateUrl: './weather.component.html',
  styleUrls: ['./weather.component.css']
})
export class WeatherComponent {
  city: string;
  weather: any;

  constructor(private weatherService: WeatherService) { }

  getWeather() {
    this.weatherService.getWeather(this.city).subscribe(data => {
      this.weather = data;
    });
  }
}
