# The-Cross-Road-Kitchen-Streamlit-Restaurant-App
a simple and interactive restaurant ordering system built using Streamlit. Customers can browse menu items with images, place orders, and pay using a responsive UPI QR Code. A clean bill summary including GST calculation is also generated automatically.


Features : Interactive Menu

Beautiful 2-column layout

High-quality images for each menu item

15+ multi-cuisine dishes displayed

Order System

Customers select multiple dishes

Auto-calculated order total

UPI Payment

Generates a proper UPI Payment URL

Fully responsive QR code

QR is centered and easy to scan

Bill Summary

Auto GST calculation (5%)

Final amount shown clearly

Simple and clean layout

Tech Stack :
Technology	Purpose
Streamlit	Web App UI
Python	Backend logic
Pillow (PIL)	Image handling
qrcode	Generate payment QR
ReportLab (optional)	For PDF bills (future upgrade)

Project Structure
├── images/
│   ├── Pizza.png
│   ├── Pasta.png
│   ├── Noodles.png
│   ├── Coffee.png
│   └── ... (other menu images)
├── app.py    # Main Streamlit application
└── README.md # Project documentation

all the images are genrated using gemini 

How to Run the App
Install required packages
pip install streamlit qrcode pillow reportlab

Run the Streamlit app
streamlit run app.py

 Your app opens at
http://localhost:8501

 UPI QR Code Logic

The app auto-generates a UPI payment link:

upi://pay?pa=<upi_id>&pn=<name>&am=<amount>&cu=INR


This link is encoded into a QR code and displayed in the center of the screen for easy scanning.

Billing Calculation
Subtotal = Sum of selected dish prices
GST (5%) = Subtotal × 0.05
Final Amount = Subtotal + GST



Devesh Sharma
Python Developer | Data Science Enthusiast
📧 sharmadevesh1611@gmail.com
