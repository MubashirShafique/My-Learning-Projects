

import 'package:weather_app/models/weather_model.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class WeatherServices {
  final String apikey = '';

  Future<Weather> fetchWeather(String cityname) async {
    final url = Uri.parse(
        'https://api.openweathermap.org/data/2.5/weather?q=$cityname&appid=$apikey');

    final response = await http.get(url);

    if (response.statusCode == 200) {
      return Weather.fromJson(json.decode(response.body));
    } else {
      throw Exception('City not found or API error');
    }
  }
}