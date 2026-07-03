
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart'; // Font ke liye
import 'package:weather_app/models/weather_model.dart';
import 'package:weather_app/services/weather_services.dart';
import 'package:weather_app/widgets/weather_card.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final WeatherServices _weatherServices = WeatherServices();
  final TextEditingController _controller = TextEditingController();
  bool _isLoading = false;
  Weather? _weather;

  // Mausam ke hisab se background badalne ka logic
  LinearGradient _getDynamicGradient() {
    if (_weather == null) return const LinearGradient(colors: [Color(0xFF4facfe), Color(0xFF00f2fe)]);

    String desc = _weather!.description.toLowerCase();
    if (desc.contains('rain')) {
      return const LinearGradient(begin: Alignment.topCenter, end: Alignment.bottomCenter, colors: [Color(0xFF2c3e50), Color(0xFF000000)]);
    } else if (desc.contains('cloud')) {
      return const LinearGradient(begin: Alignment.topCenter, end: Alignment.bottomCenter, colors: [Color(0xFF757f9a), Color(0xFFd7dde8)]);
    } else if (desc.contains('clear')) {
      return const LinearGradient(begin: Alignment.topCenter, end: Alignment.bottomCenter, colors: [Color(0xFFf6d365), Color(0xFFfda085)]);
    }
    return const LinearGradient(colors: [Color(0xFF4facfe), Color(0xFF00f2fe)]);
  }

  void _getWeather() async {
    if (_controller.text.isEmpty) return;
    setState(() => _isLoading = true);
    try {
      final weather = await _weatherServices.fetchWeather(_controller.text);
      setState(() {
        _weather = weather;
        _isLoading = false;
      });
    } catch (e) {
      setState(() => _isLoading = false);
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('City not found!')));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: double.infinity,
        height: double.infinity,
        decoration: BoxDecoration(gradient: _getDynamicGradient()),
        child: SafeArea(
          child: SingleChildScrollView(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 20),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const SizedBox(height: 20),
                  // Instagram Style Text
                  Text(
                    "Weather App",
                    style: GoogleFonts.grandHotel(fontSize: 40, color: Colors.white),
                  ),
                  const SizedBox(height: 30),
                  // Modern Search Bar
                  Container(
                    decoration: BoxDecoration(
                      boxShadow: [BoxShadow(color: Colors.black12, blurRadius: 10, offset: const Offset(0, 5))],
                    ),
                    child: TextField(
                      controller: _controller,
                      style: const TextStyle(color: Colors.white),
                      decoration: InputDecoration(
                        hintText: "Search City...",
                        hintStyle: const TextStyle(color: Colors.white60),
                        filled: true,
                        fillColor: Colors.white.withOpacity(0.2),
                        prefixIcon: const Icon(Icons.search, color: Colors.white),
                        suffixIcon: IconButton(icon: const Icon(Icons.send, color: Colors.white), onPressed: _getWeather),
                        border: OutlineInputBorder(borderRadius: BorderRadius.circular(20), borderSide: BorderSide.none),
                      ),
                      onSubmitted: (_) => _getWeather(),
                    ),
                  ),
                  const SizedBox(height: 40),
                  if (_isLoading)
                    const Center(child: CircularProgressIndicator(color: Colors.white))
                  else if (_weather != null)
                    Center(child: WeatherCard(weather: _weather!)),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}