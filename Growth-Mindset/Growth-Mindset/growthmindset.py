# streamlit
import streamlit as st 

st.set_page_config(page_title="Growth Mindset Project", page_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("Welcome to Your Growth Journey")
st.write("Embrace Challenges, Learn from mistakes, and Unlock Your Potential. This AI-powered App Help You to Build a Growth Mindset with Reflaction, Challenges, and Achievements!☆")

# quote section
st.header("✌ Today's Growth Mindset Quote")
st.write("Success is not Final, failure is not fatel: It is the Courage to Continue that Counts.- Winston Churchill")

st.header(" What's Your Challenge Today?")
user_input = st.text_input("Describe a Challenge You're Facing:")


#condition
if user_input:
    st.success( f"💪🏽 you're facing: {user_input}. Keep Persuing Forward Towards Tour Goal!🚀")
else:
    st.warning("Tell  us About Your Challenge to Get Started!")

#reflexing
st.header("Reflect on Your Learning")
reflection = st.text_area("Write Your Reflections Here:")

if reflection:
    st.success(f"🏋️‍♂️Great Insight! Your Reflection: {reflection}")
else: 
    st.info("Reflecting on Past Experience Help You Grow! Share your Difficulties")

#acheivements
st.header("🏆♛ Celebrate Your Wins!")
acheivment = st.text_input("Share Something You've Recently Accomplished:")

if acheivment: 
    st.success(f"🌹Amazing! You Achieved:{acheivment}")
else:
    st.info("Big or Small , Every Acheivement Counts! Share One now🍀")


#footer
st.write("- - -")
st.write("🚀Keep Beliveing in Yourself. Growth is a Journey, not a Destination!💐")
st.write("**🌼Develop by Osama Nadeem**")

