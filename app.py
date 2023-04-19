import streamlit as st
st.header('Greatest among three numbers'
)

st.subheader('Input three numbers')

#def input_numbers():
a = st.number_input("First number",step=1)
b = st.number_input("Second number",step=1)
c = st.number_input("Third number",step=1)


if a>b :
  if a>c :
    st.subheader(a)
    st.write('is greatest')
  else:
    st.subheader(c)
    st.write('is greatest')
else:
  if b>c:
    st.subheader(b)
    st.write('is greatest')
  else:
    st.subheader(c)
    st.write('is greatest')



