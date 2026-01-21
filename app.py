import streamlit as st

#streamlit UI
st.title("Welcome to Power calculator")
st.write("Enter a number to calculate its square, cube, and fifth power")

# Input from user
n=st.number_input("Enter an integer:", value=1, step=1)
if st.button("Calculate Powers"):
    square = n ** 2
    cube = n ** 3
    fifth_power = n ** 5

    st.write(f"The square of {n} is: {square}")
    st.write(f"The cube of {n} is: {cube}")
    st.write(f"The fifth power of {n} is: {fifth_power}")