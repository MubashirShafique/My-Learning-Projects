

import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';
import 'package:weather_app/models/weather_model.dart';

class WeatherCard extends StatelessWidget {
  final Weather weather;
  const WeatherCard({super.key, required this.weather});

  @override
  Widget build(BuildContext context) {
    return ClipRRect(
      borderRadius: BorderRadius.circular(30),
      child: BackdropFilter(
        filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10), // Glass effect
        child: Container(
          width: double.infinity,
          padding: const EdgeInsets.all(25),
          decoration: BoxDecoration(
            color: Colors.white.withOpacity(0.15),
            borderRadius: BorderRadius.circular(30),
            border: Border.all(color: Colors.white.withOpacity(0.2)),
          ),
          child: Column(
            children: [
              Lottie.asset(
                weather.description.toLowerCase().contains('rain')
                    ? 'assets/rain.json'
                    : weather.description.toLowerCase().contains('clear')
                    ? 'assets/w.json'
                    : 'assets/wind.json',
                height: 150,
              ),
              Text(
                weather.cityName,
                style: const TextStyle(fontSize: 32, fontWeight: FontWeight.w300, color: Colors.white),
              ),
              const SizedBox(height: 10),
              Text(
                "${weather.temperature.toStringAsFixed(1)}°",
                style: const TextStyle(fontSize: 70, fontWeight: FontWeight.bold, color: Colors.white),
              ),
              Text(
                weather.description.toUpperCase(),
                style: const TextStyle(fontSize: 16, color: Colors.white70, letterSpacing: 2),
              ),
              const Divider(height: 40, color: Colors.white24),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  _weatherDetail(Icons.water_drop, "Humidity", "${weather.humidity}%"),
                  _weatherDetail(Icons.air, "Wind", "${weather.windSpeed} km/h"),
                ],
              )
            ],
          ),
        ),
      ),
    );
  }

  Widget _weatherDetail(IconData icon, String label, String value) {
    return Column(
      children: [
        Icon(icon, color: Colors.white70, size: 20),
        const SizedBox(height: 5),
        Text(label, style: const TextStyle(color: Colors.white60, fontSize: 12)),
        Text(value, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
      ],
    );
  }
}