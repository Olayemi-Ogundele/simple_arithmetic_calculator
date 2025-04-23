import streamlit as st

st.title("Simple Arithmetic Calculator")
# st.sidebar.header("Enter Your Value Below")

# Initialize session state
if "result" not in st.session_state:
    st.session_state.result = None

# Take and store the user input
with st.form("Calculate_form"):
    num1 = st.text_input("Enter your first value here:", "0")
    num2 = st.text_input("Enter your second value here:", "0")
    operations = st.selectbox("Choose the Operation:", [
                              "addition", "subtraction", "multiplication", "exponential", "division"])

    # create submission
    submitted = st.form_submit_button("Calculate")

    # defining the function
    # def calculator(a,b):

    if submitted:
        try:
            a = float(num1)
            b = float(num2)

            if operations == "addition":
                st.session_state.result = a + b
            elif operations == "subtraction":
                st.session_state.result = a - b
            elif operations == "multiplication":
                st.session_state.result = a * b
            elif operations == "exponential":
                st.session_state.result = a ** b
            elif operations == "division":
                if b == 0:
                    st.session_state.result = "Math Error: Cannot divide by Zero"
                else:
                    st.session_state.result = a / b
        except ValueError:
            st.session_state.result = "Error: Please Enter Valid Number"

# Display the result
if st.session_state.result is not None:
    if isinstance(st.session_state.result, str):
        st.error(st.session_state.result)
    else:
        st.success(f"Result: {st.session_state.result}")
