import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AqiService {
  private apiUrl = `${environment.airPollutionApiUrl}?appid=${environment.apiKey}`;

  constructor(private http: HttpClient) { }

  getAqi(lat: number, lon: number): Observable<any> {
    return this.http.get(`${this.apiUrl}&lat=${lat}&lon=${lon}`);
  }
}
