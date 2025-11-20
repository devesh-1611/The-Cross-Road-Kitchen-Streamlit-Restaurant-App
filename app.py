import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image


# Page setup
st.set_page_config(page_title="The_Cross_Road_Kitchen", page_icon="🍽️", layout="wide")

# Sidebar
st.sidebar.markdown("Your favorite multi-cuisine destination!")
st.sidebar.image(
    r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Coffe.png",
    use_container_width=True
)

st.sidebar.markdown(
    """
    <h3 style='text-align: center; font-family: Georgia, serif; margin-bottom: 4px;'>
        ☕ <i>Coffee Before Anything</i>
    </h3>
    <p style='text-align: center; color: #888888; font-size: 14px; margin-top: 0;'>
        Your daily dose of warmth & aroma.
    </p>
    """,
    unsafe_allow_html=True
)

# Main Title
st.title("🍽️ The_Cross_Road_Kitchen")
st.markdown("Welcome to Devesh's Restro! Explore our menu and place your order.")

# 📋 Menu

menu = {
    "Margherita Pizza": 150, "Pasta Alfredo": 180, "Lasagna": 200, "Tiramisu": 120,
    "Garlic Bread": 90, "Spring Rolls": 100, "Kung Pao Chicken": 220, "Hakka Noodles": 150,
    "Manchurian": 140, "Dumplings": 130, "Butter Chicken": 250, "Paneer Tikka": 200,
    "Biryani": 180, "Masala Dosa": 120, "Gulab Jamun": 90, "Burrito": 180,
    "Quesadilla": 170, "Chai": 10
}

menu_images = {
    "Margherita Pizza": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Pizza.png",
    "Dosa": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Dosa.png",
    "Pasta Alfredo": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Pasta.png",
    "Lasagna": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Lasagna.png",
    "Tiramisu": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Tiramisu.png",
    "Garlic Bread": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Garlic Bread.png",
    "Spring Rolls": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Spring rolls.png",
    "Kung Pao Chicken": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Kung Pao Chicken.png",
    "Hakka Noodles": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Noodles.png",
    "Manchurian": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Manchurian.png",
    "Dumplings": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Dumpling.png",
    "Butter Chicken": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Butter Chicken.png",
    "Paneer Tikka": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Paneer Ticka.png",
    "Biryani": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Biryani.png",
    "Masala Dosa": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Paneer Ticka.png",
    "Gulab Jamun": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\GulabJamun.png",
    "Burrito": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Burrito.png",
    "Quesadilla": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Quesadilla.png",
    "Chai": r"C:\Users\DELL\OneDrive\Desktop\Restro\images\Chai.png"
}

cols = st.columns(2)

for idx, (item, price) in enumerate(menu.items()):
    with cols[idx % 2]:
        if item in menu_images:
            st.image(menu_images[item], width=200, caption=item)
        st.markdown("---")


# Order Section

st.subheader("🛍️ Place Your Order")
selected_items = st.multiselect("Select items:", list(menu.keys()))
order_total = sum(menu[item] for item in selected_items)

# Payment Section

if selected_items:

    with st.expander("Your Cart", expanded=True):
        for item in selected_items:
            st.write(f"- {item}: ₹{menu[item]}")

        st.markdown(f"### **Total: ₹{order_total}**")

    payment_choice = st.radio("Choose Payment Method:", ["UPI", "Other"])

    
#FIXED — Proper indentation for UPI flow

    if payment_choice == "UPI":

        upi_id = "sharmadevesh1611-1@oksbi"
        upi_url = f"upi://pay?pa={upi_id}&pn=Devesh%20Restro&am={order_total}&cu=INR"

        qr = qrcode.QRCode(version=1, box_size=8, border=2)
        qr.add_data(upi_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white").convert("RGB")


        center = st.columns(3)
        with center[1]:
            st.image(img, caption="Scan to Pay via UPI", width=240)

        st.caption(f"UPI ID: {upi_id} — Amount: ₹{order_total}")

    else:
        st.info("Please pay at the counter using cash or card.")

    #Bill Calculation
    
    gst = round(order_total * 0.05, 2)
    final_amount = round(order_total + gst, 2)

    st.subheader("Bill Summary")
    st.write(f"Subtotal: ₹{order_total}")
    st.write(f"GST (5%): ₹{gst}")
    st.write(f"**Total Amount: ₹{final_amount}**")

else:
    st.info("🛒 Your cart is empty. Please select items to continue.")
