import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered")

st.title("Unit Converter")

# Category definitions
definitions = {
    "Length": "Length measures the distance between two points. It is commonly measured in meters, feet, and miles.",
    "Mass": "Mass represents the amount of matter in an object. It is measured in kilograms, grams, and pounds.",
    "Temperature": "Temperature quantifies the degree of heat or cold in a substance. It is measured in Celsius, Fahrenheit, and Kelvin.",
    "Area": "Area defines the extent of a two-dimensional surface. Common units include square meters, acres, and hectares.",
    "Speed": "Speed is the rate of motion of an object. It is measured in meters per second, kilometers per hour, and miles per hour.",
    "Time": "Time measures the duration of an event or interval. It is commonly measured in seconds, minutes, and hours.",
    "Volume": "Volume determines the three-dimensional space occupied by a substance. It is measured in liters, gallons, and cubic meters.",
    "Pressure": "Pressure is the force exerted per unit area. It is measured in pascals, bars, and PSI.",
    "Energy": "Energy is the capacity to perform work. It is measured in joules, calories, and watt-hours.",
    "Frequency": "Frequency measures the number of occurrences of a repeating event per unit time. It is measured in hertz, kilohertz, and megahertz.",
    "Fuel Economy": "Fuel economy indicates how efficiently a vehicle uses fuel. It is measured in kilometers per liter and miles per gallon.",
    "Plane Angle": "Plane angles measure rotation between two intersecting lines. It is measured in degrees and radians."
}

# Sidebar: Select Conversion Category
conversion_category = st.sidebar.selectbox("Select Conversion Category", list(definitions.keys()))

# Display category definition
st.sidebar.markdown(f"**{definitions[conversion_category]}**")

# Conversion functions for each category
# (Same as before, keeping all conversion functions here)

def convert_length(value, from_unit, to_unit):
    factors = {"Meters": 1, "Kilometers": 1000, "Miles": 1609.34, "Feet": 0.3048, "Inches": 0.0254}
    return value * factors[from_unit] / factors[to_unit]

def convert_mass(value, from_unit, to_unit):
    factors = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495}
    return value * factors[from_unit] / factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return None
    
def convert_area(value, from_unit, to_unit):
    factors = {
        "Square Meters": 1,
        "Square Kilometers": 1000000,
        "Square Miles": 2589988.11,
        "Hectares": 10000,
        "Acres": 4046.86
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_speed(value, from_unit, to_unit):
    factors = {
        "Meters per second": 1,
        "Kilometers per hour": 0.277778,
        "Miles per hour": 0.44704,
        "Knots": 0.514444
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_time(value, from_unit, to_unit):
    factors = {"Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400}
    return value * factors[from_unit] / factors[to_unit]

def convert_volume(value, from_unit, to_unit):
  factors = {
        "Liters": 1,
        "Milliliters": 0.001,
        "Cubic meters": 1000,
        "Cubic feet": 28.3168,
        "Gallons": 3.78541
    }
  return value * factors[from_unit] / factors[to_unit]

def convert_pressure(value, from_unit, to_unit):
    factors = {
        "Pascals": 1,
        "Bars": 100000,
        "PSI": 6894.76
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_energy(value, from_unit, to_unit):
    factors = {
        "Joules": 1,
        "Kilojoules": 1000,
        "Calories": 4.184,
        "Kilocalories": 4184,
        "Watt-hours": 3600
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_frequency(value, from_unit, to_unit):
    factors = {
        "Hertz": 1,
        "Kilohertz": 1000,
        "Megahertz": 1000000,
        "Gigahertz": 1000000000
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_fuel_economy(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Kilometers per liter" and to_unit == "Miles per gallon":
      return value * 2.35215
    elif from_unit == "Miles per gallon" and to_unit == "Kilometers per liter":
      return value / 2.35215
    return None

def convert_plane_angle(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Degrees" and to_unit == "Radians":
      return value * 3.141592653589793 / 180
    elif from_unit == "Radians" and to_unit == "Degrees":
      return value * 180 / 3.141592653589793
    return None
    
# Define available units based on category
unit_options = {
    "Length": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
    "Mass": ["Kilograms", "Grams", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Area": ["Square Meters", "Square Kilometers", "Square Miles", "Hectares", "Acres"],
    "Speed": ["Meters per second", "Kilometers per hour", "Miles per hour", "Knots"],
    "Time": ["Seconds", "Minutes", "Hours", "Days"],
    "Volume": ["Liters", "Milliliters", "Cubic meters", "Cubic feet", "Gallons"],
    "Pressure": ["Pascals", "Bars", "PSI"],
    "Energy": ["Joules", "Kilojoules", "Calories", "Kilocalories", "Watt-hours"],
    "Frequency": ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"],
    "Fuel Economy": ["Kilometers per liter", "Miles per gallon"],
    "Plane Angle": ["Degrees", "Radians"]
}

units = unit_options.get(conversion_category, [])
value = st.number_input("Enter value to convert", value=1.0)
from_unit = st.selectbox("From", units, key="from_unit")
to_unit = st.selectbox("To", units, key="to_unit")

conversion_functions = {
    "Length": convert_length,
    "Mass": convert_mass,
    "Temperature": convert_temperature,
    "Area": convert_area,
    "Speed": convert_speed,
    "Time": convert_time,
    "Volume": convert_volume,
    "Pressure": convert_pressure,
    "Energy": convert_energy,
    "Frequency": convert_frequency,
    "Fuel Economy": convert_fuel_economy,
    "Plane Angle": convert_plane_angle
}

result = conversion_functions[conversion_category](value, from_unit, to_unit) if conversion_category in conversion_functions else "Conversion logic not implemented yet."

st.markdown(f"### {value} {from_unit} = {result} {to_unit}")

# Voice Input Button
st.markdown(
    """
    <button onclick="record()">🎤 Speak Now</button>
    <input type="hidden" id="spoken-text" value="">
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            function record() {
                const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
                recognition.lang = 'en-US';
                recognition.start();
                
                recognition.onresult = function(event) {
                    const spokenText = event.results[0][0].transcript;
                    document.getElementById('spoken-text').value = spokenText;
                    const numberInput = document.querySelector('div.stNumberInput input');
                    if (numberInput) {
                       numberInput.value = spokenText;
                        // Trigger input event for Streamlit to recognize the change
                        numberInput.dispatchEvent(new Event('input', { bubbles: true }));
                        recognition.stop();
                    } else {
                        console.error("Number input element not found.");
                    }
                }
                
                recognition.onerror = function(event) {
                    console.error("Speech recognition error:", event.error);
                };

                recognition.onend = function() {
                    console.log("Speech recognition ended.");
                };
            }
            
            // Attach the record function to the window object so it can be called from onclick
            window.record = record;
        });
    </script>
    """, unsafe_allow_html=True
)

st.markdown("---")
st.markdown("Made with ❤️ by Syed Zeeshan Iqbal")
