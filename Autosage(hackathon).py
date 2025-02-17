# -*- coding: utf-8 -*-
"""ppsp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16m9LBvQiXT18fHTBS1dtf1pTe6AG7EP3
"""

!apt-get update
!apt-get install -y curl unzip xz-utils git
!git clone https://github.com/flutter/flutter.git -b stable
!flutter/bin/flutter doctor

!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
!unzip ngrok-stable-linux-amd64.zip
!./ngrok authtoken YOUR_NGROK_AUTH_TOKEN

# Commented out IPython magic to ensure Python compatibility.
!mkdir auto_saga
# %cd auto_saga
!flutter/bin/flutter create .

!flutter/bin/flutter create .

!flutter/bin/flutter create . # This line should only be executed once to set up the project structure.
# The second execution of `flutter create .` in input-5 is likely the culprit.
# Comment it out or remove it.

flutter_code = """
import 'package:flutter/material.dart';
import 'package:gemini_flash/gemini_flash.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return GeminiFlashApp(
      title: 'AutoSaga',
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  List<Vehicle> _vehicles = [];

  @override
  void initState() {
    super.initState();
    _loadVehicles();
  }

  Future<void> _loadVehicles() async {
    // Load vehicles from API or database
    final vehicles = await VehicleApi.getVehicles();
    setState(() {
      _vehicles = vehicles;
    });
  }

  @override
  Widget build(BuildContext context) {
    return GeminiFlashScaffold(
      appBar: GeminiFlashAppBar(
        title: Text('AutoSaga'),
      ),
      body: ListView.builder(
        itemCount: _vehicles.length,
        itemBuilder: (context, index) {
          final vehicle = _vehicles[index];
          return VehicleCard(vehicle);
        },
      ),
    );
  }
}

class VehicleCard extends StatelessWidget {
  final Vehicle vehicle;

  VehicleCard(this.vehicle);

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Column(
        children: [
          Text(vehicle.make),
          Text(vehicle.model),
          Text(vehicle.year.toString()),
          Text(vehicle.price.toString()),
        ],
      ),
    );
  }
}

class Vehicle {
  final String make;
  final String model;
  final int year;
  final double price;

  Vehicle({this.make, this.model, this.year, this.price});
}

class VehicleApi {
  static Future<List<Vehicle>> getVehicles() async {
    // Simulate API call
    await Future.delayed(Duration(seconds: 2));
    return [
      Vehicle(make: 'Toyota', model: 'Camry', year: 2022, price: 25000.0),
      Vehicle(make: 'Honda', model: 'Civic', year: 2021, price: 20000.0),
      Vehicle(make: 'Ford', model: 'Fusion', year: 2020, price: 18000.0),
    ];
  }
}
"""
with open('lib/main.dart', 'w') as f: # This will now write to the 'main.dart' within the 'lib' directory.
    f.write(flutter_code)

!flutter/bin/flutter run --release --target lib/main.dart &
get_ipython().system_raw('./ngrok http 8080 &')
!sleep 10 && curl -s http://localhost:4040/api/tunnels | grep -Po 'public_url":\K"[^"]*' | sed 's/"//g'