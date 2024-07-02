import { Component } from '@angular/core';
import { AqiService } from '../aqi.service';

@Component({
  selector: 'app-aqi',
  templateUrl: './aqi.component.html',
  styleUrls: ['./aqi.component.css']
})
export class AqiComponent {
  city: string;
  lat: number;
  lon: number;
  aqi: any;

  constructor(private aqiService: AqiService) { }

  getAqi() {
    this.aqiService.getAqi(this.lat, this.lon).subscribe(data => {
      this.aqi = data;
    });
  }
}
