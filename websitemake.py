import streamlit as st

# st.title("Welcome to naman")
# st.header("Python")
# st.subheader("Java")
# st.markdown("I love Python")
# st.code("""for i in range(1,5,1):
#         print("hello")
#         """)

# import pandas as pd
# dataset=pd.read_csv("onlinefoods.csv")
# st.dataframe(dataset)


name=st.text_input("Enter your name: ")
fname=st.text_input("Enter your Father name: ")
adr=st.text_area("Enter Your Text: ")
classdata=st.selectbox("Enter your class: ",(1,2,3,4))

button=st.button("Done")
if button:
    st.markdown(f"""
     Name : {name}
     Father Name : {fname}
     address : {adr}
     class : {classdata}""")