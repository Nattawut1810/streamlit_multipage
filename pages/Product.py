import streamlit as st

st.title("Product Page")

# Initialize cart in session state if not exists
if 'cart' not in st.session_state:
    st.session_state.cart = 0

# สร้างข้อมูลสินค้า
products = [
    {"name": " Fender Jim Root Telecaster", "price": "42,300.00 THB", "image": "https://media.ctmusicshop.com/wp-content/uploads/2020/02/28213922/Fender-Jim-Root-Telecaster-1-2.jpg"},
    {"name": " Fender Player Stratocaster HSS", "price": "20,000", "image": "https://media.ctmusicshop.com/wp-content/uploads/2020/02/28213421/Fender-Player-Stratocaster-HSS-MN-BK-1.jpg"},
    {"name": "Fender Jaguar", "price": "25,000", "image": "https://cdn.shopify.com/s/files/1/0400/3974/3642/files/5384100374_fen_ins_frt_1_rr_1200x.jpg?v=1755742045"}
]

# แสดงสินค้าแต่ละชิ้น
for i, product in enumerate(products):
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(product["image"], caption=product["name"])
    
    with col2:
        st.write(f"### {product['name']}")
        st.write(f"Price: ฿{product['price']}")
        st.write("Description: This is a sample product description")
        
        if st.button(f"Add to Cart", key=f"btn_{i}"):
            st.session_state.cart += 1
            st.success(f"Added {product['name']} to cart! Cart items: {st.session_state.cart}")
    
    st.divider()  # เส้นแบ่งระหว่างสินค้า
