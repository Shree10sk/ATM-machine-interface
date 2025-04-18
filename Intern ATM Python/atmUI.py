import streamlit as st

# Page title
st.title("🏦 ATM Machine Interface")
st.subheader("Made by Shree")

# Session state to store PIN, balance, and login status
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'balance' not in st.session_state:
    st.session_state.balance = 10000
if 'pin' not in st.session_state:
    st.session_state.pin = 1010

# Login Section
if not st.session_state.authenticated:
    pin_input = st.text_input("Please enter your ATM PIN:", type="password")
    if st.button("Login"):
        try:
            if int(pin_input) == st.session_state.pin:
                st.session_state.authenticated = True
                st.success("✅ Login successful!")
            else:
                st.error("❌ Incorrect PIN. Try again.")
        except:
            st.error("Please enter numbers only.")

# Main ATM Functions
if st.session_state.authenticated:
    st.markdown("---")
    st.header("Choose an option:")

    option = st.selectbox("Select Action", ["Check Balance", "Withdraw", "Deposit", "Logout"])

    if option == "Check Balance":
        st.info(f"💰 Your current balance is ₹{st.session_state.balance}")

    elif option == "Withdraw":
        withdraw_amount = st.number_input("Enter amount to withdraw", min_value=1, step=1)
        if st.button("Withdraw"):
            if withdraw_amount > st.session_state.balance:
                st.error("⚠️ Insufficient balance")
            else:
                st.session_state.balance -= withdraw_amount
                st.success(f"✅ ₹{withdraw_amount} withdrawn successfully")
                st.info(f"Updated Balance: ₹{st.session_state.balance}")

    elif option == "Deposit":
        deposit_amount = st.number_input("Enter amount to deposit", min_value=1, step=1)
        if st.button("Deposit"):
            st.session_state.balance += deposit_amount
            st.success(f"✅ ₹{deposit_amount} deposited successfully")
            st.info(f"Updated Balance: ₹{st.session_state.balance}")

    elif option == "Logout":
        st.session_state.authenticated = False
        st.success("🔒 You have been logged out. Please re-enter your PIN.")
